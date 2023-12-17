from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import executor
import keyboard as kb
import pyautogui
import logging
import ctypes
import cv2
import os
from aiogram import Bot, types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import time
from config import token, admin

storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)
bot = Bot(token)
dp = Dispatcher(bot, storage=storage)

async def on_startup(dp):
	await bot.send_message(admin, "Ready")
	
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	if message.chat.id == admin:
		kb = ReplyKeyboardMarkup(resize_keyboard=True)
		b1 = KeyboardButton(text="⚙️ Control Panel")
		kb.add(b1)
		await message.answer('👋🏻 Welcome!', reply_markup=kb)

@dp.message_handler(content_types=['text'], text='⚙️ Control Panel')
async def handfler(message: types.Message, state: FSMContext):
        if message.chat.id == admin:
            keyboard = InlineKeyboardMarkup(row_width=3)
            
            b1 = InlineKeyboardButton(text="🔋 Power Options", callback_data="zero", inline=True)
            b2 = InlineKeyboardButton(text="🚫 Shutdown", callback_data="one", inline=True)
            b3 = InlineKeyboardButton(text="🔃 Reboot", callback_data="two", inline=True)
            b4 = InlineKeyboardButton(text="🌙 Sleep Mode", callback_data="three", inline=True)
            b5 = InlineKeyboardButton(text="⚙️ Control", callback_data="zero", inline=True)
            b6 = InlineKeyboardButton(text="🖥️ Screenshot", callback_data="four", inline=True)
            b7 = InlineKeyboardButton(text="📸 WebScreen", callback_data="five", inline=True)
            b8 = InlineKeyboardButton(text="📁 Collapse Windows", callback_data="six", inline=True)
            b9 = InlineKeyboardButton(text="🔓 Lock", callback_data="seven", inline=True)
            b10 = InlineKeyboardButton(text="🔈 Set Volume", callback_data="eight", inline=True)
            b11 = InlineKeyboardButton(text="🎧 On | Off BlueTooth", callback_data="nine", inline=True)
            keyboard.add(b1)
            keyboard.add(b2, b3, b4)
            keyboard.add(b5)
            keyboard.add(b6, b7, b8)
            keyboard.add(b9, b10, b11)
            await message.answer('⚙️ Welcome to the control panel!', reply_markup=keyboard)

@dp.callback_query_handler(lambda call: True)
async def cal(call, state: FSMContext):

	if 'one' in call.data:
		os.system('shutdown /s /t 1')

	elif 'two' in call.data:
		os.system('shutdown /r /t 1')

	elif 'three' in call.data:
		os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

	elif 'four' in call.data:
		screenshot_path = 'screenshot.png'
		pyautogui.screenshot(screenshot_path)
    
		with open(screenshot_path, 'rb') as photo:
			await bot.send_photo(admin, photo=InputFile(photo))

	elif 'five' in call.data:    
		cap = cv2.VideoCapture(0)

		for i in range(30):
			cap.read()
		ret, frame = cap.read()
		cv2.imwrite('cam.png', frame)   
		cap.release()
		cam = "cam.png"
		with open(cam, 'rb') as photo:
			await bot.send_photo(admin, photo=InputFile(photo))

	elif 'six' in call.data:
		pyautogui.hotkey('win', 'm')

	elif 'seven' in call.data:
		ctypes.windll.user32.LockWorkStation()

	elif 'eight' in call.data:
		await call.message.answer("Enter the desired volume (from 0 to 100):")
		await SetVolume.waiting_for_volume.set()

	elif 'nine' in call.data:
		time.sleep(1)
		new_x, new_y = 1887, 1056
		pyautogui.moveTo(new_x, new_y, duration=1)
		time.sleep(1)
		pyautogui.click()
		time.sleep(1)
		new_x, new_y = 1752, 712
		pyautogui.moveTo(new_x, new_y, duration=1)
		pyautogui.click()




class SetVolume(StatesGroup):
    waiting_for_volume = State()

@dp.message_handler(state=SetVolume.waiting_for_volume)
async def set_volume(message: types.Message, state: FSMContext):
    try:
        volume = int(message.text)
        if 0 <= volume <= 100:
            await message.answer(f"Volume set to {volume}%.")
            set_system_volume(volume)
        else:
            await message.answer("Enter a valid volume value (from 0 to 100).")

    except ValueError:
        await message.answer("Please enter a valid number.")

    finally:
        await state.finish()	

async def on_shutdown(dp):
    await bot.close()
    await dp.storage.close()
    await dp.storage.wait_closed()

def set_system_volume(volume):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None).QueryInterface(IAudioEndpointVolume)
    interface.SetMasterVolumeLevelScalar(volume / 100, None)

if __name__ == '__main__':
	executor.start_polling(dp, on_startup=on_startup, skip_updates=True)