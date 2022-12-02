from aiogram import types

from create_bot import bot



async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Здравствуй молодец'
                                                 f'Хоть и выглядишь ты'
                                                 f'ты как {message.from_user.first_name}')

async def player_turn(message: types.Message):
    if 0 < message.text < 29:

        await bot.send_message(message.from_user.id, 'Отличный ход')
    else:
        await bot.send_message(message.from_user.id, 'Жадность фраера погубит')

async def anything(message: types.Message):
    await bot.send_message(message.from_user.id, 
                           f'{message.text} - это еще что за хрень?')