FROM python:3.11-slim

WORKDIR /app

COPY circle.py .
COPY script.py .
COPY square.py .
COPY .env .

ENV a=5 r=3

ENTRYPOINT [ "python" ]
CMD ["script.py"]