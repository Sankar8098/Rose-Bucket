# (c) @LazyDeveloperr

import os

class Config(object):
	API_ID = int(os.environ.get("23990433"))
	API_HASH = os.environ.get("e6c4b6ee1933711bc4da9d7d17e1eb20")
	BOT_TOKEN = os.environ.get("5977289238:AAGgHF_dM37XF-87o4jPX-MMx5Y5JSRNbc0")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "File_ToLinks_Bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001699570159"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "5821871362"))
	DATABASE_URL = os.environ.get("mongodb+srv://Test:1234@cluster0.2bzsp0q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001699570159")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001870015374")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
ᴛʜɪꜱ ɪꜱ ᴘᴇʀᴍᴀɴᴇɴᴛ ꜰɪʟᴇꜱ ꜱᴛᴏʀᴇ ʙᴏᴛ!
ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ ɪ ᴡɪʟʟ ꜱᴀᴠᴇ ɪᴛ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ. ᴀʟꜱᴏ ᴡᴏʀᴋꜱ ꜰᴏʀ ᴄʜᴀɴɴᴇʟ. ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴄʜᴀɴɴᴇʟ ᴀꜱ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴇᴅɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ, ɪ ᴡɪʟʟ ᴀᴅᴅ ꜱᴀᴠᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ꜰɪʟᴇ ɪɴ ᴄʜᴀɴɴᴇʟ & ᴀᴅᴅ ꜱʜᴀʀᴀʙʟᴇ ʙᴜᴛᴛᴏɴ ʟɪɴᴋ.

🤖 **ᴍʏ ɴᴀᴍᴇ:** [ꜰɪʟᴇꜱ ꜱᴛᴏʀᴇ ʙᴏᴛ](https://t.me/{BOT_USERNAME})

📝 **ʟᴀɴɢᴜᴀɢᴇ:** [PУΓHФИ3](https://www.python.org)

📚 **ʟɪʙʀᴀʀʏ:** [P͢y͢r͢o͢g͢r͢a͢m͢](https://docs.pyrogram.org)

📡 **ʜᴏꜱᴛᴇᴅ ᴏɴ:** [H͢e͢r͢o͢k͢u͢](https://heroku.com)

🧑🏻‍💻 **DΞVΞLФPΞЯ:** [L͢a͢z͢y͢D͢e͢v͢e͢l͢o͢p͢e͢r͢r](https://t.me/Sankar2k02)

👥 **šupp⊕r† gr⊕up:** [LazY-SupP⊕ЯΓ](https://t.me/SK_MoviesOffl)

📢 **U͢p͢d͢a͢t͢e͢s͢ C͢h͢a͢n͢n͢e͢l͢:** [L͢a͢z͢y͢D͢e͢v͢e͢l͢o͢p͢e͢r͢](https://t.me/SK_MoviesOffl)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 <a href='https://t.me/SK_MoviesOffl'>**ミ★- SK_MoviesOffl -★彡** </a>

<a href=''https://t.me/LazyDeveloperr>ʟᴀᴢʏᴅᴇᴠᴇʟᴏᴘᴇʀ</a> ɪꜱ ꜱᴜᴘᴇʀ ɴᴏᴏʙ 😎. ᴊᴜꜱᴛ ʟᴇᴀʀɴɪɴɢ ꜰʀᴏᴍ ᴏꜰꜰɪᴄɪᴀʟ ᴅᴏᴄꜱ. ᴘʟᴇᴀꜱᴇ ᴅᴏɴᴀᴛᴇ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ ꜰᴏʀ ᴋᴇᴇᴘɪɴɢ ᴛʜᴇ ꜱᴇʀᴠɪᴄᴇ ᴀʟɪᴠᴇ.
ᴀʟꜱᴏ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴡɪʟʟ ᴅᴇʟᴇᴛᴇ ᴀᴅᴜʟᴛ ᴄᴏɴᴛᴇɴᴛꜱ ꜰʀᴏᴍ ᴅᴀᴛᴀʙᴀꜱᴇ. ꜱᴏ ʙᴇᴛᴛᴇʀ ᴅᴏɴ'ᴛ ꜱᴛᴏʀᴇ ᴛʜᴏꜱᴇ ᴋɪɴᴅ ᴏꜰ ᴛʜɪɴɢꜱ.
[Donate Now](https://p.paytm.me/xCTH/2jym9edy) (Paytm)
"""
	HOME_TEXT = """
HΞУ, [{}](tg://user?id={})\n\nɪ'ᴍ ɪꜱ ᴘᴇʀᴍᴀɴᴇɴᴛ **ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ**.

ミ★ 𝘚𝘦𝘯𝘥 𝘮𝘦 𝘢𝘯𝘺 𝘧𝘪𝘭𝘦 𝘐 𝘸𝘪𝘭𝘭 𝘨𝘪𝘷𝘦 𝘺𝘰𝘶 𝘢 𝘱𝘦𝘳𝘮𝘢𝘯𝘦𝘯𝘵 𝘚𝘩𝘢𝘳𝘢𝘣𝘭𝘦 𝘓𝘪𝘯𝘬. 𝘐 𝘚𝘶𝘱𝘱𝘰𝘳𝘵 𝘊𝘩𝘢𝘯𝘯𝘦𝘭 𝘈𝘭𝘴𝘰! 𝘊𝘩𝘦𝘤𝘬 **A͢b͢o͢u͢t͢ B͢o͢t͢**  𝘉𝘶𝘵𝘵𝘰𝘯.
"""
