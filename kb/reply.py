from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

r_zap = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Записаться'),
                                       KeyboardButton(text='не записываться')]],
                            resize_keyboard=True,
                            one_time_keyboard=True)