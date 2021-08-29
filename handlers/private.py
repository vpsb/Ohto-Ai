import os

import youtube_dl
from youtube_search import YoutubeSearch
import requests

from helpers.filters import command, other_filters2
from helpers.decorators import errors
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Voice

from config import BOT_NAME as bn
from config import START_PIC as sp 

@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f'I am **{bn}** !! I can Steram vidio for you in your voice chat!!, send /help for command list...\n[....]({sp})', parse_mode = "markdown", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Dev", url="https://t.me/AmiFutami"
                    )],[
                    InlineKeyboardButton(text = "Updates Channel", url = "https://t.me/AsmSafone"), InlineKeyboardButton(text = "Support Group", url = "https://t.me/safothebot")]
            ]
        )
    )

@Client.on_message(command("help") & other_filters2)
@errors
async def help(client, message: Message):
  text = f"I help ya all to play vidio!!\n\n ! \n\nThe commands i  currently support are:\n/stream - Replay with any mp4 vidio to steram in vc \n/reset - use this to reset everything, use when bot misfunctions[    ..      ]({sp})"
  await message.reply_text(text, parse_mode = "md")
  

