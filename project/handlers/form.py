from aiogram import Bot, Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from fsm.steps import StepsForm
from config import ADMIN_ID
from keyboard.reply import reply_keyboard_name, reply_keyboard_last_name, reply_keyboard_contact, reply_keyboard_location
from keyboard.inline import inline_keyboard_plan
from utils.db_request import Request

router=Router()

@router.message(CommandStart())
async def hello(message: Message, bot: Bot, state: FSMContext):
    button_name = await reply_keyboard_name(name=message.from_user.first_name)
    await message.answer('Hi lets have some chat, what is ur name?', reply_markup=button_name)
    await state.set_state(StepsForm.GET_NAME)

@router.message(StateFilter(StepsForm.GET_NAME))
async def get_name(message: Message, bot: Bot, state: FSMContext):
    if message.from_user.last_name:
        button_name= await reply_keyboard_last_name(last_name=message.from_user.last_name)
    else:
        button_name=await reply_keyboard_last_name(last_name='None')
    await message.answer(f'Ok, {message.text} what\'s your last name?', reply_markup=button_name)
    await state.update_data(name=message.text)
    await state.set_state(StepsForm.GET_LAST_NAME)

@router.message(StateFilter(StepsForm.GET_LAST_NAME))
async def get_last_name(message: Message, bot: Bot, state: FSMContext):
    user_data=await state.get_data()
    name=user_data.get('name')
    await message.answer(f'{name} {message.text}, enter ur zipcode', reply_markup=None)
    await state.update_data(last_name=message.text)
    await state.set_state(StepsForm.GET_ZIP_CODE)

@router.message(StateFilter(StepsForm.GET_ZIP_CODE))
async def get_zip_code(message: Message, bot: Bot, state: FSMContext):
    user_data=await state.get_data()
    name=user_data.get('name')
    last_name=user_data.get('last_name')
    try:
        zip_code=int(message.text)
    except ValueError:
        await message.answer(f'{name} {last_name} it seems like u entered a wrong zipcode', reply_markup=None)
        return
    plan_keyboard=await inline_keyboard_plan()
    await message.answer(f'okay, {name} {last_name} Choose a subscription plan ', reply_markup=plan_keyboard)
    await state.update_data(zip_code=zip_code)
    await state.set_state(StepsForm.GET_PLAN)

@router.callback_query(StateFilter(StepsForm.GET_PLAN), F.data=='best_plan')
async def get_plan(call: CallbackQuery, bot: Bot, state: FSMContext):
    await call.answer()
    user_data = await state.get_data()
    name=user_data.get('name')
    await call.message.edit_reply_markup()
    button_name=await reply_keyboard_contact()
    await call.message.answer(f'{name} enter your contact', reply_markup=button_name)
    await state.update_data(plan='Best plan')
    await state.set_state(StepsForm.GET_PHONE)

@router.callback_query(StateFilter(StepsForm.GET_PLAN), F.data=='prime_plan')
async def get_prime_plan(call: CallbackQuery, bot: Bot, state: FSMContext):
    await call.answer()
    user_data = await state.get_data()
    name=user_data.get('name')
    await call.message.edit_reply_markup()
    button_name=await reply_keyboard_contact()
    await call.message.answer(f'{name} enter your contact', reply_markup=button_name)
    await state.update_data(plan='prime plan')
    await state.set_state(StepsForm.GET_PHONE)

@router.callback_query(StateFilter(StepsForm.GET_PLAN), F.data=='premium_plan')
async def get_premium_plan(call: CallbackQuery, bot: Bot, state: FSMContext):
    await call.answer()
    user_data = await state.get_data()
    name=user_data.get('name')
    await call.message.edit_reply_markup() 
    button_name=await reply_keyboard_contact()
    await call.message.answer(f'{name} enter your contact', reply_markup=button_name)
    await state.update_data(plan='premium plan')
    await state.set_state(StepsForm.GET_PHONE)

@router.message(StateFilter(StepsForm.GET_PHONE), F.contact)
async def get_contact(message: Message, state: FSMContext):
    user_data=await state.get_data()
    name=user_data.get('name')
    button_name=await reply_keyboard_location()
    await message.answer(f'{name} send your location', reply_markup=button_name)
    await state.update_data(phone=message.contact.phone_number)
    await state.set_state(StepsForm.GET_LOCATION)

@router.message(StateFilter(StepsForm.GET_LOCATION), F.location)
async def get_location(message: Message, bot: Bot, state: FSMContext, request: Request):
    user_data=await state.get_data()
    name=user_data.get('name')
    last_name=user_data.get('last_name')
    zip_code=user_data.get('zip_code')
    plan=user_data.get('plan')
    phone=user_data.get('phone')
    longitude=message.location.longitude
    latitude=message.location.latitude
    await message.answer(f'{name} thanks for ur time! your manager will contact you')
    message_admin=f'New order arrived\r\n'\
                    f'[name]: {name}\r\n'\
                    f'[last name]: {last_name}\r\n'\
                    f'[zip code]: {zip_code}\r\n'\
                    f'[plan]: {plan}\r\n'\
                    f'[phone]: {phone}\r\n'\
                    f'[longitude]: {longitude}\r\n'\
                    f'[latitude]: {latitude}\r\n'
    await bot.send_message(chat_id=ADMIN_ID, text=message_admin)
    await state.clear()
    await request.add_data(user_id=message.from_user.id,
                           name=name,
                           last_name=last_name,
                           zip_code=zip_code,
                           plan=plan,
                           phone=phone,
                           longitude=longitude,
                           latitude=latitude)