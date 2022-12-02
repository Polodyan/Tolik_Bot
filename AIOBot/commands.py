from aiogram import types

from create_bot import bot

import model



async def start(message: types.Message):
    plaer = message.from_user
    model.set_player_id(plaer)
    await bot.send_message(message.from_user.id, f'{plaer.first_name}, привет!'
                                                 f'Сегодня будем делить конфеты')
    first_turn = random.int(0,1)
    if first_turn:
        await await_player(player)
    else:
        await enemy_turn(plaer)

async def player_turn(message: types.Message):
    plaer = message.from_user
    model.set_player_id(plaer)
    if (message.text).isdigit():
        if 0 < int(message.text) < 29:
            total_count = model.get_total_candies()
            plaer_take = int(message.text)
            total = total_count - plaer_take
            if model.chek_win(total):
                await bot.send_message(plaer.id, f'Победил {plaer.first_name}')
                return
            model.set_total_candies(total)
            await bot.send_message(player.id, f'{player.first_name} взял {plaer_take} конфет, '
                                              f'и на столе осталось {total}')
            await enemy_turn(plaer)

            #await bot.send_message(message.from_user.id, 'Отличный ход')
        else:
            await bot.send_message(message.from_user.id, 'Жадность фраера погубит')
    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, '
                                                     f'вообще-то мы конфеты считаем в цифрах')


async def enemy_turn(player):
    total_count = model.get_total_candies()
    if total_count < 29:
        enemy_take = total_count
    else:
        enemy_take = (total_count + 1)%28
    total = total_count - enemy_take
    if model.chek_win(total):
        await bot.send_message(player.id, f'Победил {player.first_name} ты проиграл, '
                                          f'тебя дернула железяка')
        return
        model.set_total_candies(total)
        await bot.send_message(player.id, f'Бот Толик взял {enemy_take} конфет, '
                                          f'и на столе осталось {total}')
        await await_player(player)



async def await_player(player):
    max_take = model.get_max_take()
    await bot.send_message(player.id, 
                           f'{player.first_name}, бери конфеты, но не больше {max_take}')