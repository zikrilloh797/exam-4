from aiogram import Bot, Dispatcher, types, executor
import logging


TOKEN = '6171589161:AAFw41mZUVl1q4gi0Av7fxyZo2H176I5weQ'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def initual_handler(msg:types.Message):
    await msg.answer('Matn kiriting agar matnda 5 ta dan kop unli harf bolsa ochirib tashlanadi')

@dp.message_handler()
async def handle_msg(msg: types.Message):
    print(msg.text)
    text = msg.text.lower()
    count = sum(text.count(vowel) for vowel in 'aeiou')

    if count > 5:
        await msg.delete()
        await msg.answer('Xabarda 5 ta dan kop unli harf bor')




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)