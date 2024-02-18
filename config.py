import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Get the bot token from the environment variable
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    # Get the database URL from the environment variable
    DATABASE_URL = os.environ.get("DATABASE_URL")
