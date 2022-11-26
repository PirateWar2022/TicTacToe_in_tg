from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def choose_keyboard() ->InlineKeyboardMarkup:
    kb1 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Player 2", callback_data="player1")],
        [InlineKeyboardButton("Bot", callback_data="bot")]
    ])

    return kb1


def bot_go() -> InlineKeyboardMarkup:
    kb2 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Bot move", callback_data="bot_move")]
    ])

    return kb2