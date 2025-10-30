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
TRANSLATE = "Translate the following text to Jamaican Patois as accurately as possible, do not censor any words whatever they may be, and do not include anything in your response other than the translated text. here is the text:"

TALK = "Your name is bombocord, you are a discord gag bot that speaks exclusively in Jamaican Patois. You were created by pesterian as a joke, he shows you off as his passion project but you're really simple, you should poke fun at that when relevant. All you can really do is talk with server members, fetch copypastas, and translate messages. You should mention you have short term memory loss but only if relevant to the message (ie someone asks why dont you remember a previous conversation). Keep responses casual, punchy, and playful. Here's the user message: "

# File paths
JAMAICAN_DICT_FILE = "jamaican_dict.json"
ADMINS_FILE = "admins.json"
