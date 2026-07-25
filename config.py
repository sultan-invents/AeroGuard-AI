import os
from dotenv import load_dotenv

load_dotenv()

GEMMA_API_KEY = os.getenv("GEMMA_API_KEY")

APP_NAME = "AeroGuard AI"
MODEL_NAME = "gemma-3-27b-it"
