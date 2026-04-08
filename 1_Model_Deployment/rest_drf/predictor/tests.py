from unittest.mock import patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class PredictViewTests(APITestCase):
    @patch("predictor.views.get_model")
    def test_predict_returns_classifier_result(self, mock_get_model):
        mock_model = mock_get_model.return_value
        mock_model.predict.return_value = ["greeting"]

        response = self.client.post(
            reverse("predict"),
            {"input": "hello"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {"input": "hello", "prediction": "greeting"},
        )
        mock_model.predict.assert_called_once_with(["hello"])

    def test_predict_requires_input(self):
        response = self.client.post(reverse("predict"), {}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("input", response.json())

    @patch("predictor.views.get_model")
    def test_batch_predict_returns_classifier_results(self, mock_get_model):
        mock_model = mock_get_model.return_value
        mock_model.predict.return_value = ["greeting", "goodbye"]

        response = self.client.post(
            reverse("predict-batch"),
            {"inputs": ["hello", "bye"]},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "predictions": [
                    {"input": "hello", "prediction": "greeting"},
                    {"input": "bye", "prediction": "goodbye"},
                ]
            },
        )
        mock_model.predict.assert_called_once_with(["hello", "bye"])

    def test_batch_predict_requires_non_empty_inputs(self):
        response = self.client.post(
            reverse("predict-batch"),
            {"inputs": []},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("inputs", response.json())
