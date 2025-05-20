FROM python:3.9-slim as builder

WORKDIR /app

# Install tools to clean files
RUN apt-get update && \
    apt-get install -y dos2unix && \
    rm -rf /var/lib/apt/lists/*

# Copy and clean Python files
COPY . .
RUN find . -type f -name "*.py" -exec dos2unix {} \;

# Final stage
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy cleaned files from builder
COPY --from=builder /app .

RUN mkdir -p /app/instance && chmod 777 /app/instance

EXPOSE 5000

CMD ["python", "run.py"]