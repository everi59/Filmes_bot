from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from config.config import Config, load_config
from keyboards.keyboards import create_inline_kb, PointsCallbackFactory
from services.services import get_points
from random import randint

config: Config = load_config()
router = Router()


# MAIN_MENU
@router.callback_query(PointsCallbackFactory.filter())
async def film_rate(callback: CallbackQuery,
                    callback_data: PointsCallbackFactory):
    await callback.message.edit_text(text=f'{callback_data.film} (жанр)\nОценка: {callback_data.point}')
    name_of_film = f'Название фильма #{randint(1, 100)}'
    points = get_points(name_of_film)
    points['skip'] = 'Пропустить'
    keyboard = create_inline_kb(1, dct=points)
    await callback.message.answer(text=f'Оцени фильм: {name_of_film} (жанр)', reply_markup=keyboard)


@router.callback_query(F.data == 'skip')
async def film_skip(callback: CallbackQuery):
    name_of_film = f'Название фильма #{randint(1, 100)}'
    points = get_points(name_of_film)
    points['skip'] = 'Пропустить'
    keyboard = create_inline_kb(1, dct=points)
    await callback.message.edit_text(text=f'Оцени фильм: {name_of_film} (жанр)', reply_markup=keyboard)
