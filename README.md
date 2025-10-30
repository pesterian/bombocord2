# Bombocord2

a silly discord bot that started as a joke, technically a ripoff of another discord bot but with extended functionality written from the ground up.
the OG bombocord should be considered legacy and will not be updated any further

## Features

### Dictionary System
- **Prefix Commands**: Use `*[key]` to retrieve stored text/links
- **Admin Management**: Full CRUD operations for dictionary entries

### AI Features (Google Generative AI)
- **Talk**: Chat with bombocord - pretty self explanitory
- **Translate**: Translate any message to Jamaican Patois using AI

### Slash Commands

#### Public Commands
- `/list` - Display all dictionary keys in alphabetical order
- `/roulette` - Get a random dictionary entry
- `/talk [message]` - Chat with the AI bot
- `/translate` - Translate a message (reply to a message to use this)
- `/help` - Show all available commands

#### Admin Commands
- `/add [key] [value]` - Add a new dictionary entry
- `/remove [key]` - Remove an entry (requires confirmation)
- `/update [key] [new_value]` - Update an entry's value (requires confirmation)

## Quick Setup

### Prerequisites
- Python 3.8+
- Discord Bot Token ([Create one here](https://discord.com/developers/applications))
- Google Generative AI API Key (optional, for AI features) ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd bombocord2
```

2. **Create a virtual environment**
```bash
python -m venv myvenv
source myvenv/bin/activate  # On Linux/Mac
myvenv\Scripts\activate     # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the project root:
```env
DISCORD_TOKEN=your_discord_bot_token_here
GOOGLE_API_KEY=your_google_api_key_here  # Optional: needed for /talk and /translate commands
```

5. **Configure admin users**

Edit `admins.json` to add Discord user IDs who should have admin privileges:
```json
{
  "123456789012345678": true,
  "987654321098765432": true
}
```

6. **Run the bot**
```bash
python main.py
```

## Configuration

### `config.py`
- `COMMAND_PREFIX` - Default prefix for dictionary commands (default: `*`)
- `JAMAICAN_DICT_FILE` - Path to dictionary JSON file
- `ADMINS_FILE` - Path to admins JSON file
- `TRANSLATE` - AI prompt for translation to Jamaican Patois
- `TALK` - AI prompt defining bombocord's personality and behavior

### Dictionary File (`jamaican_dict.json`)
JSON format with key-value pairs:
```json
{
  "key1": "value or URL",
  "key2": "another value"
}
```
*One very useful tip is to use discord embed URLS to include pictures and videos*

## Project Structure

```
bombocord2/
├── main.py              # Discord bot logic and commands
├── func.py              # Helper functions (no Discord dependencies)
├── config.py            # Configuration and environment variables
├── jamaican_dict.json   # Dictionary storage
├── admins.json          # Admin user IDs
├── requirements.txt     # Python dependencies
└── .env                 # Environment variables (create this)
```

## Bot Permissions

When inviting the bot to your server, ensure it has:
- Send Messages
- Read Message History
- Use Slash Commands
- Embed Links

## Usage Examples

### Dictionary Commands
```
*bomboclat  # Returns the value for "bomboclat"
```

### AI Commands
```
/talk What's your purpose?
/translate          # Reply to a message first, then use this command
```

### Admin Operations
```
/add test "This is a test entry"
/update test "Updated text"
/remove test
/list
```
