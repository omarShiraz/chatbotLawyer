import discord
import requests

# Initialize the Discord client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Flask API endpoint URL
API_URL = 'https://2fdb-34-69-144-159.ngrok-free.app/generate_response'

# Discord bot token
TOKEN = ''

# Event: Triggered when the bot is ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Event: Triggered when the bot receives a message
@client.event
async def on_message(message):
    formatted_responses = ""
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Get the message content sent by the user
    prompt = message.content

    # Send a POST request to your Flask API
    response = requests.post(API_URL, json={"prompt": prompt})

    # Parse the JSON response
    data = response.json()

    # Get the response from the API
    bot_response = data.get('response', 'No response received from the server.')


    # Extract the relevant portion before "### Response:"
    response_lines = bot_response.split("### Response:")

    for i, response in enumerate(response_lines[:2]):
        # Add the formatted response to the string
        formatted_responses += f"Legal Insight {i + 1}:\n{response.strip()}\n\n"
    # Send the relevant portion to the Discord channel
    await message.channel.send(formatted_responses)

    username = str(message.author)
    userMessage = str(message.content)
    userChannel = str(message.channel)

    print(f"{username} said '{userMessage}' ({userChannel}) ")

# Run the bot
client.run(TOKEN)
