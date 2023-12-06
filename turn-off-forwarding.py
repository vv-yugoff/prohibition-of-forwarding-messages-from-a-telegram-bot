# ----------------------------------------------------------------------------------------------------
# Main menu btn
@dp.message_handler(text='Трансфер')
async def handle_btn6(message: types.Message, protect_content=True):

    transfer_text = 'Деловой квартал:'
    transfer_keyboard = types.InlineKeyboardMarkup()
    transfer_keyboard.add(types.InlineKeyboardButton('Ссылка на трансфер', url='https://dk-park.ru/directions/corporate-buses'))

    await bot.send_message(message.chat.id, transfer_text, reply_markup=transfer_keyboard, parse_mode='HTML', protect_content=protect_content)
# ----------------------------------------------------------------------------------------------------