from aiogram import Bot, Dispatcher, executor
from ENV import Tgtoken



bot = Bot(Tgtoken.TOKEN)
dp = Dispatcher(bot)


def start():
    if __name__ == "__main__":
        executor.start_polling(dp)
