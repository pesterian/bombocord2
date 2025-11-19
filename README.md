# Bombocord2

A Discord bot with dictionary management and AI chat/translation capabilities using Jamaican Patois. Originally started as a joke, it's a complete rewrite with extended functionality.

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create `.env` file**
   ```env
   DISCORD_TOKEN=your_discord_bot_token
   OLLAMA_MODEL=llama3.2:3b
   OLLAMA_BASE_URL=http://localhost:11434 #optional
   ```

3. **Install Ollama** (for AI features)
   - Make sure your hardware is compatible (requires GPU/CPU that supports local LLM inference)
   - Install Ollama:
     ```bash
     curl -fsSL https://ollama.com/install.sh | sh
     sudo systemctl start ollama
     sudo systemctl enable ollama
     ```
   - Pull the model you want to use:
     ```bash
     ollama pull llama3.2:3b
     ```
   - Ollama should now be running in the background (`ollama serve` runs automatically via systemd) 

4. **Configure Admin Users**
   - Edit `admins.json` to add Discord user IDs who can manage the dictionary

5. **Run the Bot**
   ```bash
   python3 main.py
   ```

## Configuration

Edit `config.py` to customize:
- **Rate Limiting**: Adjust `RATE_LIMIT_CALLS` and `RATE_LIMIT_PERIOD`
- **AI Prompts**: Modify `TALK` and `TRANSLATE` system prompts
- **Command Prefix**: Change the prefix for dictionary lookups (default: `*`)

## Features

- Dictionary system with prefix commands (`*key`)
- AI chat and translation to Jamaican Patois
- Rate limiting per user
- Admin controls for dictionary management
- Logging to `bombo.log`