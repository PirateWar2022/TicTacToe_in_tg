from aiogram import types
from aiogram.types import ReplyKeyboardRemove
import logic.geniral_g as g
from random import choice
from keyboards.bot_keyboard1 import bot_go
from aiogram.utils.exceptions import MessageTextIsEmpty


cnt = 0
cnt2 = ""
all_ns = " 012345678"



def choose_from(ground):
    onl_n = []
    for i in ground:
        if i != "X" and i != "O":
            onl_n.append(int(i))
        else:
            pass

    return onl_n



async def from_user(ms: types.Message):
    global cnt, cnt2
    try:
        if all_ns.find(ms.text) != -1:
            if cnt % 2 == 0 or cnt == 0:
                await ms.answer('Now go you ( X )')
                g.ground[int(ms.text)] = "X"
                cnt2 += ms.text
                cnt += 1
                await ms.answer(g.format(),
                                reply_markup=bot_go())
                if g.check_check() == None:
                    return await ms.answer(g.check_check())
                else:
                    return await ms.answer(g.check_check(),
                                        reply_markup=ReplyKeyboardRemove())

        else:
            print("Tun tun...")

    except MessageTextIsEmpty:
        pass


async def from_bot(ms: types.Message):
    global cnt, cnt2
    await ms.answer('Now go bot( O )')
    random_num = choice(choose_from(g.ground))
    g.ground[random_num] = "O"
    cnt2 += ms.text
    cnt += 1
    await ms.answer(g.format())
    if g.check_check() == None:
        return await ms.answer(g.check_check())
    else:
        return await ms.answer(g.check_check(),
                               reply_markup=ReplyKeyboardRemove())









