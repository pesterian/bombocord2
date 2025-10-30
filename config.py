import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Discord Bot Configuration
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
COMMAND_PREFIX = "*"

# Google Generative AI Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# AI Prompts
TRANSLATE = ""

TALK = ""

# File paths
JAMAICAN_DICT_FILE = "jamaican_dict.json"
ADMINS_FILE = "admins.json"
