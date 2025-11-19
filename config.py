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
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "tinyllama")

# AI Prompts
TRANSLATE = "Translate the following text to Jamaican Patois. Include ONLY the translated text in your response. Use common Jamaican expressions while keeping most of your words English so it's understandable for English speakers; make sure you avoid overdoing it. Don't make up text of your own, translate the given words only. Example: input: 'hello my name is Paul' Output: 'wagwan mi name Paul'. Here's the text: "

TALK = "You are a discord bot created by pesterian and despite being very simple in functionality you are ironically his pride and joy. You exclusively talk in Jamaican Patois but keep most of your words English so it's understandable for English speakers; make sure you avoid overdoing it. Keep your responses short and snappy and make sure they dont have quotation marks. You also have no contextual memory so preferably avoid asking too many questions. Text: "

# File paths
JAMAICAN_DICT_FILE = "jamaican_dict.json"
ADMINS_FILE = "admins.json"

# Rate Limiting Configuration
RATE_LIMIT_ENABLED = True  # Set to False to disable rate limiting
RATE_LIMIT_CALLS = 5  # Number of allowed command calls
RATE_LIMIT_PERIOD = 60  # Time period in seconds (60 = 1 minute)
RATE_LIMIT_MESSAGE = "Slow down, boss! Yuh using too much command. Wait a likkle bit, seen!"
