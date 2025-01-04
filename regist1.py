from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import requests

API_TOKEN = '8105778922:AAGDHQqWbrJiJOltU1xjA5BCE388BfFPjFA'
REGISTER_URL = 'http://ваш_сайт/api/register'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Добро пожаловать! Введите /register, чтобы зарегистрироваться.")

@dp.message_handler(commands=['register'])
async def register(message: types.Message):
    await message.answer("Введите ваше имя, email и пароль через запятую (Пример: Иван, ivan@mail.com, 12345)")

@dp.message_handler()
async def handle_message(message: types.Message):
    try:
        # Парсим данные
        data = message.text.split(',')
        username = data[0].strip()
        email = data[1].strip()
        password = data[2].strip()

        # Отправляем данные на сервер
        response = requests.post(REGISTER_URL, json={
            "username": username,
            "email": email,
            "password": password,
            "telegram_id": message.from_user.id
        })

        if response.status_code == 200:
            await message.answer("Регистрация успешна!")
        else:
            await message.answer("Произошла ошибка при регистрации.")
    except Exception as e:
        await message.answer("Произошла ошибка. Проверьте данные и попробуйте снова.")

if __name__ == '__main__':
    executor.start_polling(dp)
