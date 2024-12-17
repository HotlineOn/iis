FROM python:3.11-slim

COPY . /app
WORKDIR /app

RUN pip install requests

CMD ["python3", "req.py"]

# docker build . --tag request_service:0
# docker run request_service:0