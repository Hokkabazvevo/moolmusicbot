# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👋__Hoşgeldin [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !__\n
🤖 __[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Telegramda film, dizi, video gibi görüntülü içerikleri izlemenize veya şarkı dinlemenize olanak sağlar.__**

ℹ __Komutlar butonuna tıklayarak bot komutlarını ve çalışma prensiplerine ulaşabilirsiniz.__

🔖 __Botun kullanma talimatına ulaşmak için **Basit Komutlar** butonuna tıkla__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Beni Grubuna Ekle ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("Basit Komutlar", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📜 Komutlar", callback_data="cbcmds"),
                    InlineKeyboardButton("👨‍💻 Bot Sahibi ", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "Destek Grubu 🔰", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "Mool Rehber 📣", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Botu kullanmak için basit bilgi**

__İlk olarak beni grubunuza ekleyin.__

__Grupta daha stabil çalışabilmem için gerekli olan yetkileri verin.__

__Yetki verdikten sonra verilerini yenilemek için grubunuzda /reload komutunu çalıştırın.__

__Grubunuza @{ASSISTANT_NAME} asistan botunu ekleyin veya onu davet etmek için grubunuzda /userbotjoin yazın.__

__Video/Müzik oynatmaya başlamadan önce görüntülü sohbeti açın.__

__Botun bozulma ya da takılma sorunları olması durumunda /reload komutunu kullanın.__

__Bot hakkında sorunuz, öneriniz varsa ya da grubunuza özel bot yaptırmak istiyorsanız iletişim. [Zephyrus](https://t.me/Zep_Unb)**

⚡ __Tüm hakları saklıdır. {BOT_NAME} A.Ş__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Geri 🔙", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Selam [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) hangi komutu seçmek istiyorsun?**


© __Tüm hakları saklıdır. {BOT_NAME} A.Ş__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Admin Komutları", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Sahip ", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Basit Komutlar", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("Geri 🔙", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Basit Komutlar:

» /play => Şarkı dinlemenize yarar.

» /vplay => Film/video izlemenize yarar.

» /ara => Video indirir.

» /indir => Müzik indirir. 

© __Tüm hakları saklıdır {BOT_NAME} A.Ş__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Geri 🔙", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Admin Komutları

» /pause - Botu durdurur.

» /resume - Botu devam ettirir.

» /skip - Sonraki şarkıya geçer.

» /stop - Botu kapatır.

» /reload - Botu yeniden başlatır.

» /katil - Bot gruba katılır.

» /cik - Bot gruptan çıkar.

© __Tüm hakları saklıdır. {BOT_NAME} A.Ş__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Geri 🔙", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""@Zep_Unb

© __Tüm hakları saklıdır. {BOT_NAME} A.Ş__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Geri 🔙", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
