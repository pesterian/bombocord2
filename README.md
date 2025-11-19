# Bombocord2

a silly discord bot that started as a joke, technically a ripoff of another discord bot but with extended functionality written from the ground up. the OG bombocord should be considered legacy and will not be updated any further
this is the experimental ai branch, you should probably know what youre doing to set this version up

## AI Setup (for the core functionality setup check the 'master' branch)

   **Install Ollama** (for AI features)
   - Make sure your hardware is compatible (requires GPU/CPU that supports local LLM inference) - I can't help you with this one
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


   **Run the Bot**
   ```bash
   python3 main.py
   ```

## Configuration

Edit `config.py` to customize:
- **API** The port that will be listening for ollama's local API
- **Rate Limiting**: Adjust `RATE_LIMIT_CALLS` and `RATE_LIMIT_PERIOD`
- **AI Prompts**: Modify `TALK` and `TRANSLATE` system prompts

## Features exclusive to the ai branch
- Rate limiting per user
- Logging to `bombo.log`
