import datetime
import asyncio
import re
import configparser
from dateutil.relativedelta import relativedelta
from pyrogram import Client

config = configparser.ConfigParser()
config.read("config.ini")

api_id   = config['Telegram']['API_ID']
api_hash = config['Telegram']['API_HASH']
username = config['Telegram']['USERNAME']

start_date = datetime.datetime.now() - relativedelta(days=2) # Формируем дату на нужное количество дней назад
limit = 10 # Максимальное количество сообщений из каждого телеграм-канала, в которых будет поиск

with open('keywords.txt', 'r') as file:
	keywords_list=file.read().lower().splitlines() # список ключевых слов прочитали построчно из файла, привели к нижнему регистру

with open('chats.txt', 'r') as file:
	chat_list=file.read().splitlines() # список ключевых слов прочитали построчно из файла, привели к нижнему регистру

app = Client(name=username, api_id=api_id, api_hash=api_hash)

async def main():
	async with app:
		for chat in chat_list:
			async for message in app.get_chat_history(chat, limit=limit):
				if message.date >= start_date: # Только сообщения, которые появились после нужной даты
					if not message.text:
						if message.photo and message.caption:
							message_text = message.caption
						else:
							return
					else:
						message_text = message.text
					message_words_list = re.sub("[^a-zа-яёїієґ0-9_-]", " ",  message_text.lower()).split() # Очищаем текст сообщения от символов и пунктуации, разбиваем на слова
					if any(word in keywords_list for word in message_words_list): # Проверяем вхождение каждого из ключевых слов в тексте сообщения
						print(f'==== {message.date} https://t.me/{chat}/{message.id}')
					await asyncio.sleep(1)

app.run(main())