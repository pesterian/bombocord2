# Bombocord2

a silly discord bot that started as a joke, technically a ripoff of another discord bot but with extended functionality written from the ground up.
the OG bombocord should be considered legacy and will not be updated any further

## TODO
 - Logging events

> **Note:** All AI functionality is maintained exclusively on the `ai` branch. This main branch focuses on core bot features without AI integration.

## Features

### Dictionary System
- **Prefix Commands**: Use `*[key]` to retrieve stored text/links
- **Admin Management**: Full CRUD operations for dictionary entries

### Slash Commands

#### Public Commands
- `/list` - Display all dictionary keys in alphabetical order
- `/roulette` - Get a random dictionary entry

#### Admin Commands
- `/add [key] [value]` - Add a new dictionary entry
- `/remove [key]` - Remove an entry
- `/update [key] [new_value]` - Update an entry's value

## Quick Setup

### Prerequisites
- Python 3.8+
- Discord Bot Token ([Create one here](https://discord.com/developers/applications))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/pesterian/bombocord2
cd bombocord2
```

2. **Create a virtual environment**
```bash
python -m venv myvenv*
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
python3 main.py #most modern mac and linux distributions use this by default 
```

## Configuration

### `config.py`
- `COMMAND_PREFIX` - Default prefix for dictionary commands (default: `*`)
- `JAMAICAN_DICT_FILE` - Path to dictionary JSON file
- `ADMINS_FILE` - Path to admins JSON file

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
*bomboclat          # Returns the value for "bomboclat"
```

### Admin Operations
```
/add test "This is a test entry"
/update test "Updated text"
/remove test
```
