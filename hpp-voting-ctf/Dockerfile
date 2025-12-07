FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m ctfuser
USER ctfuser

EXPOSE 5008

CMD ["gunicorn", "--bind", "0.0.0.0:5008", "app:app"]
