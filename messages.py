# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest
from dateutil.relativedelta import relativedelta

import datetime
import json

async def dump_all_messages(channel, client):
    """Записывает json-файл с информацией о всех сообщениях канала/чата"""
    offset_msg = 0    # номер записи, с которой начинается считывание
    limit_msg = 10   # максимальное число записей, передаваемых за один раз
    start_date = datetime.datetime.now() - relativedelta(days=2)
    all_messages = []   # список всех сообщений
    total_messages = 0
    total_count_limit = 10  # поменяйте это значение, если вам нужны не все сообщения

    class DateTimeEncoder(json.JSONEncoder):
        '''Класс для сериализации записи дат в JSON'''
        def default(self, o):
            if isinstance(o, datetime):
                return o.isoformat()
            if isinstance(o, bytes):
                return list(o)
            return json.JSONEncoder.default(self, o)

    while True:
        async for message in client.iter_messages(channel, limit=limit_msg):
            all_messages.append(message.text)
            print(message.text)
            print('____')
        total_messages = len(all_messages)
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break
    #     history = await client(GetHistoryRequest(
    #         peer=channel,
    #         offset_id=offset_msg,
    #         offset_date=None, 
    #         add_offset=0,
    #         limit=limit_msg, max_id=0, min_id=0,
    #         hash=0))
    #     if not history.messages:
    #         break
    #     messages = history.messages
    #     for message in messages:
    #         all_messages.append(message.text)
    #         print(message.text)
    #     offset_msg = messages[len(messages) - 1].id
    #     total_messages = len(all_messages)
    #     if total_count_limit != 0 and total_messages >= total_count_limit:
    #         break
    # with open('channel_messages.json', 'w', encoding='utf8') as outfile:
    # json.dump(all_messages, outfile, ensure_ascii=False, cls=DateTimeEncoder)
    #     for message in all_messages:
    #         print(message)
        # with open(f"{channel.title}.txt", "w", encoding="utf-8") as write_file:
        #     for message in all_messages:
        #         try:
        #             write_file.writelines(f" text: {message} \n")
        #         except Exception as e:  
        #             print(e)
    print('Сбор по каналу завершен')
