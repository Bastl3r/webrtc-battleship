FROM python:3.12-slim

WORKDIR /app 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY index.html . 
COPY server.py . 
COPY cert.pem . 
COPY key.pem . 

EXPOSE 8443

CMD ["python", "server.py"]
