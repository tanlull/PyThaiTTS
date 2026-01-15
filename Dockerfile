# Use Python 3.9 as base image (compatible with the project requirements)
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and setup files
COPY requirements.txt setup.py README.md ./
COPY pythaitts ./pythaitts

# Install Python dependencies
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

# Install the package
RUN pip install --no-cache-dir -e .

# Copy demo script
COPY demo.py ./

# Set environment variable to avoid Python buffering
ENV PYTHONUNBUFFERED=1

# Run the demo script by default
CMD ["python", "demo.py"]
