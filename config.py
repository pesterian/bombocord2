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

TALK = "You are a helpful AI assistant. Respond to the following:"

# File paths
JAMAICAN_DICT_FILE = "jamaican_dict.json"
ADMINS_FILE = "admins.json"
