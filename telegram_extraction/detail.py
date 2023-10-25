import telethon
from telethon import TelegramClient
import pandas as pd
from telethon.sync import TelegramClient
import datetime
from config import *

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()

    # Provide the username or ID of the channel
    channel_username = 'OmegaofTSbot'
    
    start_date = datetime.date(2023, 7, 1)  # Change this to your desired start date
    end_date = datetime.date(2023, 7, 2)   # Change this to your desired end date

    async for message in client.iter_messages(channel_username):
        if start_date <= message.date.date() <= end_date:
            print(message.date, message.text)

    try:
        # Get the entity object for the channel
        channel_entity = await client.get_entity(channel_username)

        # Print group metadata information
        print("Group ID:", channel_entity.id)
        # print("Group Title:", channel_entity.title)
        print("Group Username:", channel_entity.username)
        print("Group Type:", channel_entity.megagroup)
        print("Group Creation Date:", channel_entity.date)
        # print("Group Description:", channel_entity.about)
        

        # # Print invite link (if available)
        # if channel_entity.username:
        #     invite_link = f"https://t.me/{channel_entity.username}"
        #     print("Group Invite Link:", invite_link)

        # # Get the participants
        # participants = await client.get_participants(channel_entity)
        # for participant in participants:
        #     user = await client.get_entity(participant.user_id)
        #     role = participant.participant.__class__.__name__.replace("ChannelParticipant", "")
        #     print(f"User ID: {user.id}, Username: {user.username}, Role: {role}")

    except telethon.errors.rpcerrorlist.ChannelPrivateError:
        print("The channel is private and you don't have access.")

    except telethon.errors.rpcerrorlist.ChannelInvalidError:
        print("The provided channel username or ID is invalid.")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        await client.disconnect()

if __name__ == "__main__":
    client.loop.run_until_complete(main())

