FROM python:3.11-slim


WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 8000

# Set PYTHONPATH to ensure the app package can be imported
ENV PYTHONPATH=/app

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]