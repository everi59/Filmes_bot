from aiogram import Bot
from aiogram.types import BotCommand

from keyboards.keyboards import PointsCallbackFactory
from aiogram.fsm.state import State, StatesGroup


def get_points(film_name: str) -> dict:
    return {PointsCallbackFactory(film=film_name, point=f'{x}').pack(): str(x) for x in range(1, 6)}
