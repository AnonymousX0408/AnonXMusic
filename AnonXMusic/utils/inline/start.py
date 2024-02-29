from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Wᴀɴɴᴀ ᴀᴅᴅ ᴍᴇ ʙᴀʙᴇ? 🥂", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="💖 Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url="https://t.me/ProCoderZBots"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Wᴀɴɴᴀ ᴀᴅᴅ ᴍᴇ ʙᴀʙᴇ? 🥂",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="🍁 Oᴡɴᴇʀ ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="🍹 Sᴜᴘᴘᴏʀᴛ ", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url="https://t.me/ProCoderZBots"),
            InlineKeyboardButton(text="Oғғɪᴄɪᴀʟ Cʜᴀɴɴᴇʟ", url="https://t.me/Pro_CoderZ"),
        ],
    ]
    return buttons
