FROM python:3.9-alpine  AS runtime

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app", "--extraction", "--input", "/docs", "--output", "dist"]
