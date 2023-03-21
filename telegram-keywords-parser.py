import configparser
import messages

from telethon.sync import TelegramClient
from telethon import connection
from telethon.sessions import StringSession

# для корректного переноса времени сообщений в json
from datetime import date, datetime

config = configparser.ConfigParser()
config.read("config.ini")

api_id   = config['Telegram']['API_ID']
api_hash = config['Telegram']['API_HASH']
username = config['Telegram']['USERNAME']
session_string = config['Telegram']['SESSION_STRING']

async def main():
	url = input("Введите ссылку на канал или чат: ")
	channel = await client.get_entity(url)
	await messages.dump_all_messages(channel, client)

with TelegramClient(StringSession(session_string), api_id, api_hash) as client:
	# session_string = StringSession.save(client.session)
	# print(session_string)
	# with open('session.ini', 'w') as f:
	# 	f.write(session_string)
	client.loop.run_until_complete(main())
