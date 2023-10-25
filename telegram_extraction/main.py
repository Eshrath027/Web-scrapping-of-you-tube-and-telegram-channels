import telethon
from telethon import TelegramClient
import pandas as pd
from telethon.sync import TelegramClient
import datetime
from config import *


client = TelegramClient('session_name1', api_id, api_hash)

Channel_name='peter_jamess'


async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    # print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    # username = me.username
    # print(username)
    # print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    # async for dialog in client.iter_dialogs():
    #     print(dialog.name, 'has ID', dialog.id)

    # # You can print the message history of any chat:
    start_date = datetime.date(2023, 7, 1)  # Change this to your desired start date
    end_date = datetime.date(2023, 7, 2)   # Change this to your desired end date

    async for message in client.iter_messages(Channel_name):
        if start_date <= message.date.date() <= end_date:
            print(message.date, message.text)
    
    # async for u in client.iter_participants(Channel_name, aggressive=True, offset=0):
    #     print(u.id, u.first_name)



    #     # You can download media from messages, too!
    #     # The method will return the path where the file was saved.
    #     if message.photo:
    #         path = await message.download_media()
    #         print('File saved to', path)  # printed after download is done

with client:
    client.loop.run_until_complete(main())
    

