# Use the official Python image as the base image
FROM python:3.12


RUN pip install --upgrade pip --root-user-action=ignore


# Set the working directory in the container
WORKDIR /Proyecto-Bokitas

# Copy the application files into the working directory
COPY . /Proyecto-Bokitas

# Install the application dependencies
RUN pip install -r requirements.txt

# Define the entry point for the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
