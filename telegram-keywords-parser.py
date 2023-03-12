import configparser
import messages

from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime

config = configparser.ConfigParser()
config.read("config.ini")

api_id   = config['Telegram']['API_ID']
api_hash = config['Telegram']['API_HASH']
username = config['Telegram']['USERNAME']

client = TelegramClient(username, api_id, api_hash)

client.start()

async def main():
	url = input("Введите ссылку на канал или чат: ")
	channel = await client.get_entity(url)
	await messages.dump_all_messages(channel, client)


with client:
	client.loop.run_until_complete(main())
