FROM python:3.10-slim

WORKDIR /app

# Install pipenv
RUN python3 -m ensurepip --upgrade
RUN pip install pipenv

# Copy Pipfile and Pipfile.lock (if present)
COPY Pipfile Pipfile.lock ./

# Install dependencies using Pipenv
RUN pipenv install --deploy-dev

COPY . .

# Set the working directory for the application
WORKDIR /app/src

CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
