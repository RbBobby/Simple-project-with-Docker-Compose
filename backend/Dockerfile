# Use Python 3.9 as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the application code
COPY . /app/

# Expose port 5000
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
