import asyncio
import datetime
import telethon
from telethon import TelegramClient
from django.core.management.base import BaseCommand

api_id = 29704241
api_hash = 'f1514037c703e18210be4ed7513f888d'

class Command(BaseCommand):
    help = 'Fetch and print message history from a Telegram channel'

    def handle(self, *args, **options):
        async def main():
            client = TelegramClient('session_name1', api_id, api_hash)
            Channel_name = 'peter_jamess'

            async with client:
                # You can print the message history of any chat:
                start_date = datetime.date(2023, 7, 1)  # Change this to your desired start date
                end_date = datetime.date(2023, 7, 2)   # Change this to your desired end date

                async for message in client.iter_messages(Channel_name):
                    if start_date <= message.date.date() <= end_date:
                        self.stdout.write(self.style.SUCCESS(f"{message.date}: {message.text}"))

        # Run the event loop with the main function
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
