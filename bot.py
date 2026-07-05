import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8920973557:AAFui219YyioOJQv3mD7NvUUrFsjoHk8wOQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ===== КНОПКИ =====
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👋 Привет"), KeyboardButton(text="ℹ️ Помощь")],
        [KeyboardButton(text="💬 Эхо")]
    ],
    resize_keyboard=True
)

# ===== START =====
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот 🤖", reply_markup=menu)

# ===== КНОПКИ =====
@dp.message(lambda message: message.text == "👋 Привет")
async def hi(message: types.Message):
    await message.answer("Привет 😎")

@dp.message(lambda message: message.text == "ℹ️ Помощь")
async def help_cmd(message: types.Message):
    await message.answer("Я умею:\n- кнопки\n- эхо\n- команды")

@dp.message(lambda message: message.text == "💬 Эхо")
async def echo_mode(message: types.Message):
    await message.answer("Пиши сообщение 👇")

# ===== ЭХО =====
@dp.message()
async def echo(message: types.Message):
    if message.text and message.text.startswith("/"):
        return
    await message.answer(f"🔁 {message.text}")

# ===== ЗАПУСК =====
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
