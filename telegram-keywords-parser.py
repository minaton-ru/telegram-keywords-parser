import datetime
import configparser
from dateutil.relativedelta import relativedelta
# import messages
from pyrogram import Client
from pyrogram import enums
from pyrogram.raw.functions import messages

config = configparser.ConfigParser()
config.read("config.ini")

api_id   = config['Telegram']['API_ID']
api_hash = config['Telegram']['API_HASH']
username = config['Telegram']['USERNAME']

start_date = datetime.datetime.now() - relativedelta(days=1)
chat = 'javascript_jobs_feed'
mylimit = 4
query='Григорий'

app = Client(name=username, api_id=api_id, api_hash=api_hash)

async def main():
	async with app:
		search_result = await app.invoke(
			messages.Search(
				peer=chat, 
				q=query, 
				limit=mylimit, 
				min_date=start_date, 
				max_date=0, 
				filter=enums.MessagesFilter.EMPTY,
				offset_id=0,
				add_offset=0,
				min_id=0,
				max_id=0,
				hash=0
			)
		)
		for message in search_result:
			print(message.text)
			print('_______')

app.run(main())