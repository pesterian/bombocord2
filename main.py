import discord
from discord import app_commands
from config import (
    DISCORD_TOKEN, COMMAND_PREFIX, JAMAICAN_DICT_FILE, ADMINS_FILE,
    OLLAMA_BASE_URL, OLLAMA_MODEL, TRANSLATE, TALK
)
from func import (
    get_dict_entry, get_all_keys, add_dict_entry, 
    remove_dict_entry, update_dict_entry, is_admin, get_random_entry,
    query_ollama
)

# Create bot client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Store pending confirmations: {user_id: {'action': 'remove/update', 'key': str, 'value': str}}
pending_confirmations = {}


@client.event
async def on_ready():
    await tree.sync()
    print(f'Bot is ready! Logged in as {client.user}')


@client.event
async def on_message(message):
    # Ignore bot's own messages
    if message.author == client.user:
        return
    
    # Check if message starts with prefix
    if message.content.startswith(COMMAND_PREFIX):
        key = message.content[len(COMMAND_PREFIX):].strip().lower()
        
        if not key:
            return
        
        # Get the value from dictionary
        value = get_dict_entry(key, JAMAICAN_DICT_FILE)
        
        if value:
            # Check if the user's message is a reply
            if message.reference and message.reference.message_id:
                # Reply to the same message the user replied to
                try:
                    replied_message = await message.channel.fetch_message(message.reference.message_id)
                    await replied_message.reply(value, mention_author=False)
                except:
                    await message.channel.send(value)
            else:
                # Just send normally
                await message.channel.send(value)
    
    # Check for confirmation responses
    if message.author.id in pending_confirmations:
        response = message.content.lower().strip()
        if response in ['yes', 'no']:
            confirmation = pending_confirmations[message.author.id]
            
            if response == 'yes':
                if confirmation['action'] == 'remove':
                    success, msg = remove_dict_entry(confirmation['key'], JAMAICAN_DICT_FILE)
                    if success:
                        await message.channel.send(f"✅ Mi delete '{confirmation['key']}' from di book, seen?")
                    else:
                        await message.channel.send(f"❌ Somet'ing go wrong, boss!")
                elif confirmation['action'] == 'update':
                    success, msg = update_dict_entry(confirmation['key'], confirmation['value'], JAMAICAN_DICT_FILE)
                    if success:
                        await message.channel.send(f"✅ Mi update '{confirmation['key']}' inna di book, seen?")
                    else:
                        await message.channel.send(f"❌ Somet'ing go wrong, boss!")
            else:
                await message.channel.send("❌ Aight, mi cancel dat fi yuh.")
            
            del pending_confirmations[message.author.id]


@tree.command(name="list", description="List all available dictionary keys")
async def list_keys(interaction: discord.Interaction):
    """List all keys in alphabetical order."""
    keys = get_all_keys(JAMAICAN_DICT_FILE)
    
    if not keys:
        await interaction.response.send_message("📝 Di dictionary empty out, boss!")
        return
    
    # Split into chunks if too long
    chunk_size = 50
    chunks = [keys[i:i + chunk_size] for i in range(0, len(keys), chunk_size)]
    
    embed = discord.Embed(
        title="📚 All Di Keys Dem",
        description=f"Total: {len(keys)} tings inna di book",
        color=discord.Color.blue()
    )
    
    for i, chunk in enumerate(chunks):
        key_list = ", ".join([f"`{k}`" for k in chunk])
        embed.add_field(
            name=f"Page {i+1}" if len(chunks) > 1 else "Keys",
            value=key_list,
            inline=False
        )
    
    await interaction.response.send_message(embed=embed)


@tree.command(name="add", description="[ADMIN] Add a new dictionary entry")
@app_commands.describe(key="The key to add", value="The value/text for this key")
async def add_entry(interaction: discord.Interaction, key: str, value: str):
    """Add a new entry to the dictionary (admin only)."""
    if not is_admin(interaction.user.id, ADMINS_FILE):
        await interaction.response.send_message("❌ Yuh nuh have nuh permission fi dis, star!", ephemeral=True)
        return
    
    success, message = add_dict_entry(key, value, JAMAICAN_DICT_FILE)
    if success:
        await interaction.response.send_message(f"✅ Mi add '{key}' to di book, seen?")
    else:
        await interaction.response.send_message(f"❌ Dat key '{key}' already deh yah, boss!")


@tree.command(name="remove", description="[ADMIN] Remove a dictionary entry")
@app_commands.describe(key="The key to remove")
async def remove_entry(interaction: discord.Interaction, key: str):
    """Remove an entry from the dictionary (admin only)."""
    if not is_admin(interaction.user.id, ADMINS_FILE):
        await interaction.response.send_message("❌ Yuh nuh have nuh permission fi dis, star!", ephemeral=True)
        return
    
    # Check if key exists
    value = get_dict_entry(key, JAMAICAN_DICT_FILE)
    if not value:
        await interaction.response.send_message(f"❌ Mi cyaan find `{key}` inna di book, boss!")
        return
    
    # Store confirmation request
    pending_confirmations[interaction.user.id] = {
        'action': 'remove',
        'key': key,
        'value': None
    }
    
    await interaction.response.send_message(
        f"⚠️ Yuh sure yuh waan delete `{key}`, breda?\n"
        f"Current ting: {value[:100]}{'...' if len(value) > 100 else ''}\n\n"
        f"Type `yes` fi go through wid it or `no` fi cancel."
    )


@tree.command(name="update", description="[ADMIN] Update a dictionary entry")
@app_commands.describe(key="The key to update", new_value="The new value/text")
async def update_entry(interaction: discord.Interaction, key: str, new_value: str):
    """Update an existing entry in the dictionary (admin only)."""
    if not is_admin(interaction.user.id, ADMINS_FILE):
        await interaction.response.send_message("❌ Yuh nuh have nuh permission fi dis, star!", ephemeral=True)
        return
    
    # Check if key exists
    old_value = get_dict_entry(key, JAMAICAN_DICT_FILE)
    if not old_value:
        await interaction.response.send_message(f"❌ Mi cyaan find `{key}` inna di book, boss!")
        return
    
    # Store confirmation request
    pending_confirmations[interaction.user.id] = {
        'action': 'update',
        'key': key,
        'value': new_value
    }
    
    await interaction.response.send_message(
        f"⚠️ Yuh sure yuh waan update `{key}`, breda?\n\n"
        f"**Old ting:** {old_value[:100]}{'...' if len(old_value) > 100 else ''}\n"
        f"**New ting:** {new_value[:100]}{'...' if len(new_value) > 100 else ''}\n\n"
        f"Type `yes` fi go through wid it or `no` fi cancel."
    )


@tree.command(name="roulette", description="Get a random dictionary entry")
async def roulette(interaction: discord.Interaction):
    """Get a random key-value pair from the dictionary."""
    entry = get_random_entry(JAMAICAN_DICT_FILE)
    
    if not entry:
        await interaction.response.send_message("📝 Di dictionary empty out, boss!")
        return
    
    key, value = entry
    await interaction.response.send_message(value)


@tree.command(name="help", description="Show all available commands")
async def help_command(interaction: discord.Interaction):
    """Display help information about all commands."""
    is_user_admin = is_admin(interaction.user.id, ADMINS_FILE)
    
    embed = discord.Embed(
        title="🇯🇲 Bombocord Commands",
        description="All di commands yuh can use, seen?",
        color=discord.Color.gold()
    )
    
    # Prefix command
    embed.add_field(
        name=f"{COMMAND_PREFIX}[key]",
        value="Get di text fi any key from di dictionary\nExample: `*bomboclat`",
        inline=False
    )
    
    # Public slash commands
    embed.add_field(
        name="/list",
        value="Show all keys inna di dictionary (alphabetical order)",
        inline=False
    )
    
    embed.add_field(
        name="/roulette",
        value="Get a random ting from di dictionary",
        inline=False
    )
    
    embed.add_field(
        name="/talk [prompt]",
        value="Talk to the AI assistant",
        inline=False
    )
    
    embed.add_field(
        name="/translate [text]",
        value="Translate text to Jamaican Patois using AI",
        inline=False
    )
    
    embed.add_field(
        name="/help",
        value="Show dis message",
        inline=False
    )
    
    # Admin commands (only show if user is admin)
    if is_user_admin:
        embed.add_field(
            name="👑 Admin Commands",
            value="Dese commands only fi di admins, star!",
            inline=False
        )
        
        embed.add_field(
            name="/add [key] [value]",
            value="Add a new entry to di dictionary",
            inline=False
        )
        
        embed.add_field(
            name="/update [key] [new_value]",
            value="Update an existing entry inna di dictionary",
            inline=False
        )
        
        embed.add_field(
            name="/remove [key]",
            value="Delete an entry from di dictionary",
            inline=False
        )
    
    await interaction.response.send_message(embed=embed)


@tree.command(name="talk", description="Talk to the AI assistant")
@app_commands.describe(prompt="Your message or question for the AI")
async def talk(interaction: discord.Interaction, prompt: str):
    """Query the AI assistant with a custom prompt."""
    await interaction.response.defer(thinking=True)
    
    success, response = query_ollama(prompt, OLLAMA_BASE_URL, OLLAMA_MODEL, TALK)
    
    if success:
        # Discord has a 2000 character limit for messages
        if len(response) > 1900:
            # Split into chunks if too long
            chunks = [response[i:i+1900] for i in range(0, len(response), 1900)]
            await interaction.followup.send(chunks[0])
            for chunk in chunks[1:]:
                await interaction.channel.send(chunk)
        else:
            await interaction.followup.send(response)
    else:
        await interaction.followup.send(f"❌ Error: {response}", ephemeral=True)


@tree.command(name="translate", description="Translate text to Jamaican Patois using AI")
@app_commands.describe(text="The text you want to translate to Jamaican Patois")
async def translate(interaction: discord.Interaction, text: str):
    """Translate text to Jamaican Patois using AI."""
    await interaction.response.defer(thinking=True)
    
    full_prompt = f"{TRANSLATE}\n\n{text}"
    success, response = query_ollama(full_prompt, OLLAMA_BASE_URL, OLLAMA_MODEL)
    
    if success:
        # Discord has a 2000 character limit for messages
        if len(response) > 1900:
            # Split into chunks if too long
            chunks = [response[i:i+1900] for i in range(0, len(response), 1900)]
            await interaction.followup.send(chunks[0])
            for chunk in chunks[1:]:
                await interaction.channel.send(chunk)
        else:
            await interaction.followup.send(response)
    else:
        await interaction.followup.send(f"❌ Error: {response}", ephemeral=True)


# Run the bot
if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
