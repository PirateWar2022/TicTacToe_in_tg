from aiogram.types import ReplyKeyboardRemove
from aiogram import types
import logic.geniral_g as g




async def arrange(ms: types.Message):
    global cnt, cnt2, all_ns

    if all_ns.find(ms.text):
        if cnt == 0 or cnt % 2 == 0 and cnt2.find(ms.text) == -1:
            try:
                await ms.answer('Now go X')
                g.ground[int(ms.text)] = "X"
                cnt2 += ms.text
                cnt += 1
                await ms.answer(g.format())
                if g.check_check() == None:
                    return await ms.answer(g.check_check())
                else:
                    return await ms.answer(g.check_check(),
                                           reply_markup=ReplyKeyboardRemove())


            except:
                pass

        elif cnt % 2 != 0 and cnt2.find(ms.text) == -1:
            try:
                await ms.answer('Now go O')
                g.ground[int(ms.text)] = "O"
                cnt2 += ms.text
                cnt += 1

                await ms.answer(g.format())
                return await ms.answer(g.check_check())


            except:
                pass

        else:
            await ms.answer("Oh no no no....")









