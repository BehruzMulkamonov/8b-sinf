import logging
import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "8222700462:AAFfUuqtPTBism0TeIw6IxE7vmjBLdHgpvw"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Foydalanuvchi holatini saqlash
user_state = {}

# Valyuta kursini olish (Markaziy bank API)
def get_usd_rate():
    url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/"
    response = requests.get(url)
    data = response.json()
    return float(data[0]['Rate'])

# START
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("💵 UZS → USD", "💰 USD → UZS")

    await message.answer("Valyuta konvertatsiya botiga xush kelibsiz!", reply_markup=keyboard)

# BUTTON BOSILGANDA
@dp.message_handler(lambda message: message.text in ["💵 UZS → USD", "💰 USD → UZS"])
async def choose_mode(message: types.Message):
    if message.text == "💵 UZS → USD":
        user_state[message.from_user.id] = "uzs_to_usd"
        await message.answer("So'm miqdorini kiriting:")
    else:
        user_state[message.from_user.id] = "usd_to_uzs"
        await message.answer("Dollar miqdorini kiriting:")

# SON KIRITISH
@dp.message_handler()
async def convert_handler(message: types.Message):
    user_id = message.from_user.id

    if user_id not in user_state:
        await message.answer("Iltimos, avval button tanlang.")
        return

    try:
        amount = float(message.text)
        rate = get_usd_rate()

        if user_state[user_id] == "uzs_to_usd":
            result = amount / rate
            await message.answer(f"{amount} so'm ≈ {round(result, 2)} USD 💵")

        elif user_state[user_id] == "usd_to_uzs":
            result = amount * rate
            await message.answer(f"{amount} USD ≈ {round(result, 2)} so'm 💰")

    except:
        await message.answer("Iltimos, faqat son kiriting! ❗")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)