# Use Fedora as the base image
FROM registry.fedoraproject.org/f33/python3 as builder

USER root

# Set the working directory inside the container
WORKDIR /application

# Copy the requirements file
COPY requirements.txt /application/

# Install Python dependencies
RUN pip install --upgrade pip==19.3.1
RUN pip install --no-cache-dir -r requirements.txt --upgrade

# Copy all application files to /application
COPY . /application/

# Expose Flask's default port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV PYTHONPATH=/application 

# Use the entrypoint script
ENTRYPOINT ["./entrypoint.sh"]
