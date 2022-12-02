from aiogram import types, Dispatcher

import commands


def registret_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])
    #dp.register_message_handler(commands.stop, commands=['stop'])
    dp.register_message_handler(commands.player_turn)