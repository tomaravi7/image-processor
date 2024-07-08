# Use an official Python runtime as a parent image
FROM python:3-slim

# Set environment variables
ENV PORT=5100
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . /app

# Expose the port the app runs on
EXPOSE $PORT

# Start the application with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5100", "app:app"]
