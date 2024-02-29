from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ Mᴇ 🥂", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="✭ ᴜᴘᴅᴀᴛᴇs ✭", url="https://t.me/ProCoderZBots"),
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
        [InlineKeyboardButton(text="❀⋟ ʜᴇʟᴘ ⋞❀", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="✮ ᴏᴡɴᴇʀ ✮", user_id=config.OWNER_ID),
        ],
        [
            InlineKeyboardButton(text="✭ ᴜᴘᴅᴀᴛᴇs ✭", url="https://t.me/ProCoderZBots"),
            InlineKeyboardButton(text="✭ ᴄʜᴀɴɴᴇʟ ✭", url="https://t.me/Pro_CoderZ"),
        ],
    ]
    return buttons
