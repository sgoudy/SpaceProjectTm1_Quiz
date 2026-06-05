# Use a Linux Python base image so the build works on Docker Desktop Linux containers
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the app files into the container
COPY . .

# Install Linux audio player for sound support and the Python dependency
RUN apt-get update && \
    apt-get install -y --no-install-recommends alsa-utils && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

# Run the game directly with Python
CMD ["python", "main.py"]
