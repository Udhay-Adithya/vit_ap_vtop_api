# syntax=docker/dockerfile:1

# Use a Python version compatible with your pyproject.toml (e.g., 3.13)
ARG PYTHON_VERSION=3.13
FROM python:${PYTHON_VERSION}-slim

# Set environment variables to prevent Python from writing .pyc files and to buffer output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install git, which is required by Poetry to install git-based dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy only the files necessary for dependency installation to leverage Docker cache
COPY pyproject.toml poetry.lock ./

# Install project dependencies using Poetry
# --without dev: Excludes development dependencies (like pytest)
# --no-root: Do not install the project package itself, only its dependencies.
#            The project source code will be copied in a later step.
# --no-interaction: Do not ask any interactive questions
# --no-ansi: Disable ANSI output
# Gunicorn will be installed as part of project dependencies if added to pyproject.toml
RUN poetry install --without dev --no-root --no-interaction --no-ansi

# Copy the rest of the application code into the container
COPY . .

# Expose the port that Gunicorn will run on
EXPOSE 8080

# Command to run the application using Gunicorn
# Ensure 'src.main:app' correctly points to your FastAPI application instance
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "4", "--worker-class uvicorn.workers.UvicornWorker" "--timeout", "0", "src.main:app"]