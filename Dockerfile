FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /app/instance && chmod 777 /app/instance
WORKDIR /app/acmecorp
EXPOSE 5000
CMD ["python", "app.py"]