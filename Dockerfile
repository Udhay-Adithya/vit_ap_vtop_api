# syntax=docker/dockerfile:1

# Specify Python version
ARG PYTHON_VERSION=3.11.5
FROM python:${PYTHON_VERSION}-slim

# Set working directory inside the container
WORKDIR /code

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt gunicorn

# Copy application code into the container
COPY . .

# Expose the port that Gunicorn will bind to
EXPOSE 8080

# Run Gunicorn with the correct module path and configuration
CMD ["gunicorn", "--bind", ":8080", "--workers", "1", "--threads", "8", "--timeout", "0", "src.app:app"]