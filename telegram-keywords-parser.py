import configparser
# import messages
from pyrogram import Client

config = configparser.ConfigParser()
config.read("config.ini")

api_id   = config['Telegram']['API_ID']
api_hash = config['Telegram']['API_HASH']
username = config['Telegram']['USERNAME']

chat = 'your telegram chat name'
limit = 4
query='your text to search'

app = Client(name=username, api_id=api_id, api_hash=api_hash)

async def main():
	async with app:
		async for message in app.search_messages(chat, query, limit):
			print(message.text)
			print('_______')

app.run(main())