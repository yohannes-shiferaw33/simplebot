from aiogram.utils.keyboard import ReplyKeyboardBuilder

async def reply_keyboard_name(name: str):
    builder = ReplyKeyboardBuilder()
    builder.button(text=name)
    builder.adjust(1)
    keyboard=builder.as_markup(resize_keyboard=True,
                               one_time_keyboard=True,
                               input_field_placeholder='Enter your name or click the reply button')
    return keyboard

async def reply_keyboard_last_name(last_name: str):
    builder = ReplyKeyboardBuilder()
    builder.button(text=last_name)
    builder.adjust(1)
    keyboard=builder.as_markup(resize_keyboard=True,
                               one_time_keyboard=True,
                               input_field_placeholder='Enter your last name or click the reply button')
    return keyboard

async def reply_keyboard_contact():
    builder = ReplyKeyboardBuilder()
    builder.button(text='Send contact', request_contact=True)
    builder.adjust(1)
    keyboard=builder.as_markup(resize_keyboard=True,
                               one_time_keyboard=True,
                               input_field_placeholder='Enter your contact or click the reply button')
    return keyboard

async def reply_keyboard_location():
    builder = ReplyKeyboardBuilder()
    builder.button(text='Send location', request_location=True)
    builder.adjust(1)
    keyboard=builder.as_markup(resize_keyboard=True,
                               one_time_keyboard=True,
                               input_field_placeholder='Enter your location by clicking the reply button')
    return keyboard