FROM python:3-slim

# Install dependencies
COPY requirements.txt /app/requirements.txt
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 80

CMD ["python", "app.py"]
