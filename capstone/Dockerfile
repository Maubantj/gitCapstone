# Use a Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the Django project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

