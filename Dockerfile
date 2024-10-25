# Use the official Python image as the base image
FROM python:3.12.1


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip 


# Set the working directory in the container
WORKDIR /Proyecto-Bokitas

# Copy the application files into the working directory
COPY . .

ENV PATH=/usr/local/nginx/bin:$PATH


# Install the application dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the server port
EXPOSE 8000

# Define the entry point for the container
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Sistema_Bokitas.wsgi"]

