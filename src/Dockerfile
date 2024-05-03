FROM python:3.10

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r req.txt
RUN pip install cryptography
CMD ["python3","-u", "main.py"]
