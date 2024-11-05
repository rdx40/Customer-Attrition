# Start with Python 3.12.2 slim version
FROM python:3.12.2-slim

# Set the working directory inside the container
WORKDIR /code

# Copy requirements file to the working directory
COPY ./requirements.txt /code/requirements.txt

# Install Python dependencies without caching
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application code into the container
COPY ./app /code/app

# Expose port 80 for the application
EXPOSE 80

# Run the application with Uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

