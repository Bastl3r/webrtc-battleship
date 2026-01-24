# Multi-platform build support for ARM and x86
FROM python:3.12-slim

WORKDIR /app 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY index.html . 
COPY server.py . 
COPY ./certs/cert.pem . 
COPY ./certs/key.pem . 

EXPOSE 8443

# Health check to verify server is running
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import socket; socket.create_connection(('127.0.0.1', 8443), timeout=5)"

CMD ["python", "server.py"]
