from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def keyboard1() -> ReplyKeyboardMarkup:
    kb0 = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton("0")],
        [KeyboardButton("1")],
        [KeyboardButton("2")],
        [KeyboardButton("3")],
        [KeyboardButton("4")],
        [KeyboardButton("5")],
        [KeyboardButton("6")],
        [KeyboardButton("7")],
        [KeyboardButton("8")],
        [KeyboardButton("/restart")]
    ])

    return kb0




def start_keyboard() -> ReplyKeyboardMarkup:
    kb2 = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton("/start_play")]
    ])

    return kb2

def start_keyboard1() -> ReplyKeyboardMarkup:
    kb2 = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton("/start_play1")]
    ])

    return kb2