FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application files
COPY app.py .
COPY config.txt .
COPY flag_http.txt .
COPY welcome.msg .
COPY image.png .

# Copy templates directory
COPY templates/ templates/

EXPOSE 80

CMD ["python", "app.py"]
