import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Discord Bot Configuration
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
COMMAND_PREFIX = "*"

# Google Generative AI Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Ollama Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama2")

# AI Prompts
TRANSLATE = "Translate the following text to Jamaican Patois/Creole. Be authentic and use common Jamaican expressions:"

TALK = "You are a discord bot created by pesterian and despite being very simple in functionality you are ironically his pride and joy. You exclusively talk in Jamaican Patois and have short term memory loss (no contextual memory):"

# File paths
JAMAICAN_DICT_FILE = "jamaican_dict.json"
ADMINS_FILE = "admins.json"

# Rate Limiting Configuration
RATE_LIMIT_ENABLED = True  # Set to False to disable rate limiting
RATE_LIMIT_CALLS = 5  # Number of allowed command calls
RATE_LIMIT_PERIOD = 60  # Time period in seconds (60 = 1 minute)
RATE_LIMIT_MESSAGE = "Slow down, boss! Yuh using too much command. Wait a likkle bit, seen!"
