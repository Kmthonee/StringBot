from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""۞¦ اهلا بـك عزيـزي  {msg.from_user.mention}
۞¦ فـي بـوت اسـتـخـراج الـجـلـسـات
۞¦ يمكنك استخراج الجلسات الـتالية
۞¦ بايروجرام للحسابات & بايروجرام للبوتات
۞¦ بـايـروجـرام مـيوزك احـدث إصـدار 
۞¦ تيرمـكـس للحسابات & تيرمـكـس للبوتات

۞¦ بواسطـة : [𝐒𝐨𝐮𝐫𝐜𝐞 - 𝐊𝐦𝐭𝐡𝐨𝐧](t.me/Kmthon) √""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="📥 ⍆ اضغط لبدا استخراج كود ⍅ 📥", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𝐒𝐨𝐮𝐫𝐜𝐞 - 𝐊𝐦𝐭𝐡𝐨𝐧", url="https://t.me/Kmthon"),
                    InlineKeyboardButton("𝐍𝐚𝐲𝐳𝐚𝐤", user_id=5926107421)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
