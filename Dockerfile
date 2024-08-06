FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY mqtt_reader.py mqtt_reader.py

CMD ["python", "mqtt_reader.py"]
