# (c) @AbirHasan2005

import asyncio
from bot.client import Client
from bot.core.db.add import (
    add_user_to_database
)
from pyrogram import (
    filters,
    types
)


@Client.on_message((filters.video | filters.audio | filters.document) & ~filters.channel & ~filters.edited)
async def on_media_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await add_user_to_database(c, m)
    await asyncio.sleep(3)
    dosya = m.document
    isim = dosya.file_name
    await m.reply_text(text=isim,quote=True)
    return isim
