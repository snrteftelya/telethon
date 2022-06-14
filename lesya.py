from telethon import TelegramClient, sync
from telethon.sync import TelegramClient, events
import asyncio


api_id = 19316324
api_hash = "3a7f2302c5461fcf18909471455ea9fc"
client = TelegramClient('session_name', api_id, api_hash)
client.start()


@client.on(events.NewMessage(chats=('t.me/physicskapbot')))
async def handler(event):
    if event.message.message == "Введите номер задания":
        for i in range(1, 2000):
            await asyncio.sleep(1)
            await client.send_message('t.me/physicskapbot', f'{i}')
            await asyncio.sleep(7)
            message = await client.get_messages('t.me/physicskapbot')
            await asyncio.sleep(1)
            await message[0].click()
            await asyncio.sleep(1)
            i += 1

client.run_until_disconnected()
