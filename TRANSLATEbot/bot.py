import logging

from aiogram import Bot, Dispatcher, types, executor
from utils import translate_user_text
from bot_keyboards import choose_lang_btn

logging.basicConfig(level=logging.INFO)


BOT_TOKEN = "5968257852:AAEjUfVagNAJwolzAJwbMbwVHGD7h-v8VEw"

bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)



@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.answer("Assalomu alekum Hurmatli, ! ")



@dp.message_handler(content_types=['text'])
async def get_user_text(message: types.Message):
    text = message.text
    result = await translate_user_text(text, "uz")
    btn = await choose_lang_btn()
    await message.answer(result, reply_markup=btn)


# @dp.callback_query_handler(text="lang_ru")
# async def to_ru(call: types.Message):
#     text = call.message.text
#     result = await translate_user_text(text, "ru")
#     btn = await choose_lang_btn()
#     await call.message.edit_text(result, reply_markup=btn)






# @dp.callback_query_handler(text="lang_en")
# async def to_en(call: types.Message):
#     text = call.message.text
#     result = await translate_user_text(text, "en")
#     btn = await choose_lang_btn()
#     await call.message.edit_text(result, reply_markup=btn)



@dp.callback_query_handler(text_contains="lang")
async def trans_user_text(call: types.CallbackQuery):
    lang = call.data.split("_")[1]
    text = call.message.text
    result = await translate_user_text(text, lang)
    if text != result:
        btn = await choose_lang_btn()
        await call.message.edit_text(result, reply_markup=btn)
    


if __name__== "__main__":
    executor.start_polling(dp)

# pip install googletrans 3.1.0a0