from aiogram.utils.keyboard import InlineKeyboardBuilder

async def inline_keyboard_plan():
    builder = InlineKeyboardBuilder()
    builder.button(text='Best', callback_data='best_plan')
    builder.button(text='Prime', callback_data='prime_plan')
    builder.button(text='Premium', callback_data='premium_plan')
    builder.adjust(2,1)
    key_board=builder.as_markup()
    return key_board