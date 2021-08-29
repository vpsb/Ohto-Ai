from pyrogram import Client, filters
from pyrogram.types import Message, Voice
from callsmusic import mp, quu, block_chat
import callsmusic
import converter
from pyrogram.errors import PeerIdInvalid, ChannelInvalid
from pyrogram.errors import exceptions
from pyrogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.decorators import authorized_users_only
from helpers.decorators import authorized_users_only2
from config import API_ID, API_HASH, BOT_TOKEN, PLAY_PIC, BOT_USERNAME, OWNER_ID, UBOT_ID
import moviepy.editor as soundex

@Client.on_message(filters.command(["stream", f"stream@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def stream_vid(client: Client, message: Message):
  video = (message.reply_to_message.video or message.reply_to_message.document) if message.reply_to_message else None
  if not video:
    return await message.reply_text('Reply to a file or a video....')
  if not (video.file_name.endswith('.mkv') or video.file_name.endswith('.mp4')):
    return await message.reply_text('Not a valid format...')
  dl = await message.reply_to_message.download()
  audio_file_name = str(dl).split('.', 1)[0]
  ext_s = soundex.VideoFileClip(dl)
  sound_clip = converter.convert(ext_s.audio.write_audiofile(f'{audio_file_name}.mp3'))
  try:
      group_call = await mp.call(message.chat.id)
  except RuntimeError:
      return await message.reply_text('The vc seems to be off.....')
  except ChannelInvalid:
      return await message.reply_text('Seems like my assistant is not in the chat!')
  except Exception as e:
      return await message.reply_text(f'{type(e).__name__}: {e}')
  group_call.input_filename = sound_clip
  await group_call.set_video_capture(dl)
  block_chat.append(message.chat.id)
