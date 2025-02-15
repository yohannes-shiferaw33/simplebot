from aiogram.fsm.state import StatesGroup, State

class StepsForm(StatesGroup):
    GET_NAME=State()
    GET_LAST_NAME=State()
    GET_ZIP_CODE=State()
    GET_PLAN=State()
    GET_PHONE=State()
    GET_LOCATION=State()
