import os
from dotenv import load_dotenv

load_dotenv()

GROK_API_KEY = os.getenv("GROK_API_KEY")


if not GROK_API_KEY:
    print("⚠️ Warning: GROK_API_KEY not set")
