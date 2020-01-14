FROM python:3.7-slim

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1
WORKDIR /backend

COPY requirements-prod.txt ./
RUN pip install --no-cache-dir -r requirements-prod.txt

COPY . .

CMD gunicorn -w 3 run:app -b 0.0.0.0:5000
