import os

from fastapi import FastAPI
from aiologger.loggers.json import JsonLogger


# Access environment variables
USERS_URL = os.getenv("USERS_URL")
POSTS_URL = os.getenv("POSTS_URL")

# Configure logger
logger = JsonLogger.with_default_handlers(
            level='DEBUG',
            serializer_kwargs={'ensure_ascii': False},
        )

# Create a FastAPI instance
app = FastAPI()
