FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

#dev
CMD [ "python", "app.py" ]

#prod
#CMD [ "gunicorn", "-b", "0.0.0.0:5000", "app:app"]