from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Merhabalar {message.from_user.mention()} !**\n
💭 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **Botu gruba ekleyerek şarkı dinleyebilir, video izleyebilirsiniz. Ayrıca discord sunucumuza katılmak için discord.gg/flexgang**

Daha fazla bilgi için aşağıdaki butonları kullanın👇
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Beni Grubuna Ekle ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("Bilgi", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Komutlar", callback_data="cbcmds"),
                    InlineKeyboardButton("🧑‍💻 Sahip", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "Destek Grubu 🔰", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "Mool Rehber 📣", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Grubunuza Özel Bot Yaptırmak İçin", url="https://t.me/Zep_Unb"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Destek Grubu 🔰", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "Mool Rehber 📣", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**Merhaba {message.from_user.mention()}, ben {BOT_NAME}**\n\n✨ Bot is working normally\n🍀 My Master: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ Bot Version: `v{__version__}`\n🍀 Pyrogram Version: `{pyrover}`\n✨ Python Version: `{__python_version__}`\n🍀 PyTgCalls version: `{pytover.__version__}`\n✨ Uptime Status: `{uptime}`\n\n**Thanks for Adding me here, for playing video & music on your Group video chat** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `Poonggg!!`\n" f" `Bot {delta_ping * 1000:.3f} ms hızında çalışıyor.`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        """Grubunuza özel bot yaptırmak için iletişim=> @Zep_Unb

» /play => istediğin şarkıyı direk dinletir
» /vplay => istedigin filmi indirip izletir
» /search => video indirir
» /indir => music indirir 

NOT : /play komutu normal şarkı oynatır /vplay ise görüntülü içerik oynatır.

» /pause - Botu durdurur
» /resume - Botu devam ettirir.
» /skip - Bir sonraki şarkıya, videoya geçer.
» /stop - sesten düşer herşeyi durdurur
» /reload - Botu yeniden başlatır.
» /katil - Gruba katılır.
» /cik - Gruptan çıkar."""
        )
