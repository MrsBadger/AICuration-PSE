FROM python:3.10

WORKDIR /app

# Install pipenv
RUN python3 -m ensurepip --upgrade
RUN pip install pipenv

# Install dependencies using Pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy --system

COPY . .

# Set the working directory for the application
WORKDIR /app/src

CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
