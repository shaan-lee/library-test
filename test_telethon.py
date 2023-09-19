import configparser
import json
import re
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel

config = configparser.ConfigParser()
config.read(".cfg")
config = config["TELETHON"]

input_channel = "https://t.me/Python"

with TelegramClient(
    session="read_new_message",
    api_id=config["api_id"],
    api_hash=config["api_hash"],
) as client:
    for message in client.iter_messages(input_channel):
        if message.text:
            print(message.sender_id, ":", message.text)
