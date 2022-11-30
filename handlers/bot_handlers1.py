from main import dp
from aiogram import types, executor
from text import START_MESSAGE
from keyboards.bot_keyboards import keyboard1,  start_keyboard, start_keyboard1
from keyboards.bot_keyboard1 import choose_keyboard
import logic.user_moves as lu
import logic.bot_moves as lb
import logic.geniral_g as gl

bool1 = None

@dp.message_handler(commands=["start"])
async def start(ms: types.Message):
    await ms.answer(START_MESSAGE, parse_mode="HTML")

@dp.message_handler(commands=["tictactoe"])
async def tictactoe(ms: types.Message):
    gl.clear()
    await ms.answer("Choose",
                    reply_markup=choose_keyboard())

@dp.callback_query_handler(text='player1')
async def player(cb: types.CallbackQuery):
    global bool1
    bool1 = True
    await cb.message.answer("Click!!!",
                                   reply_markup=start_keyboard())


@dp.callback_query_handler(text='bot')
async def start2_bot(cd: types.CallbackQuery):
    global bool1
    bool1 = False
    await cd.message.answer("Click!!!",
                            reply_markup=start_keyboard1())

@dp.callback_query_handler(text = 'bot_move')
async def move(cd: types.CallbackQuery):
   await lb.from_bot(cd.message)





@dp.message_handler(commands=['start_play1'])
async def start1(ms: types.Message):
    await ms.answer("First go you (X)")
    await ms.answer(gl.format(),
                    reply_markup=keyboard1())

@dp.message_handler(commands=["start_play"])
async def start(ms: types.Message):
    await ms.answer("First go X!!!!")
    await ms.answer(gl.format(),
              reply_markup=keyboard1())


@dp.message_handler(commands=['restart'])
async def restart(ms: types.Message):
    gl.clear()
    await ms.answer("You can play again!!! /tictactoe")


@dp.message_handler()
async def start11(ms: types.Message):
    global bool1
    if bool1 == True:

        await lu.arrange(ms)

    elif bool1 == False:

        await lb.from_user(ms)




if "__main__" == __name__:
    executor.start_polling(dp,
                           skip_updates=False,
                           )

