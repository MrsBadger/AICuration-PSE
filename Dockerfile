# Base image
FROM python:3.10-slim

# Set the working directory for the application
WORKDIR /tmp

# Set environment variables
ENV PYTHONUNBUFFERED=0

# Install pipenv
RUN python3 -m ensurepip --upgrade
RUN pip install pipenv

# Install python dependencies
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile

# Set non-root user for security
RUN adduser non-root-user --system && \
    addgroup non-root && \
    adduser non-root-user non-root

# Switch to non-root-user
USER non-root-user

# Copy main directory 
COPY app app/

# Set command to start after `docker run`
CMD ["python", "app/main.py"]
