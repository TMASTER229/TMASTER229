import telebot
import phonenumbers
import csv
import json
from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier
from phonenumbers.phonenumberutil import NumberParseException
from googlesearch import search
from telebot import types
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import time

def Generate(phone, dork, amount, TOKEN, YRNUM):
	if phone:
		parse_num = phonenumbers.parse(phone, None)
		timezone_num = timezone.time_zones_for_number(parse_num)
		carrier_num = carrier.name_for_number(parse_num, "en")
		region_num = geocoder.description_for_number(parse_num, "en")
		valid_num = phonenumbers.is_valid_number(parse_num)
		possible_num = phonenumbers.is_possible_number(parse_num)
		info_num = f' PARSE_NUM: {parse_num} \n TIMEZONE_NUM: {timezone_num} \n CARRIER_NUM: {carrier_num} \n REGION_NUM: {region_num} \n VALID_NUM: {valid_num} \n POSSIBLE_NUM: {possible_num}'
		print(info_num)
		phone = phone.replace("+", "")
		info_num1 = f'TELEGRAM: https://t.me/{phone}\nWHATSAPP: https://wa.me/{phone}\nVIBER: https://viber.click/{phone}\nVK: https://find.vk.com/{phone}\nOK: https://www.phoneradar.ru/phone/{phone}'
		info_num2 = f'\nFACEBOOK: https://facebook.com/login/identify/{phone}\nOI(AI): https://www.OpenAI.com/{phone}\nTWITTER: https://twitter.com/account/{phone}\nAVITO1: https://www.avito.ru/rossiya/{phone}'
		info_num3 = f'\nAVITO2: https://www.avito.com/rossiya/{phone}\nPR: https://www.phoneradar.ru/phone/{phone}\nSKYPE: https://Skype.com/{phone}\nGC: https://GettCont.ru/{phone}'
		info_num4 = f'\nDISCORD1: https://Discord.com/{phone}\nDISCORD2: https://Discord.ru/{phone}\nDOXBIN: https://Doxbin.com/{phone}'
		print(info_num1 + info_num2 + info_num3 + info_num4)
	if dork and amount:
		requ = 0
		counter = 0

		for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=0):
			counter = counter + 1
			print ("!", counter, results)
			time.sleep(0.1)
			requ += 1
			if requ >= int(amount):
				break

	if TOKEN:
		bot = telebot.TeleBot(TOKEN)
		print("bot start")

		@bot.message_handler(commands=['start'])
		def GetPhone(message):
			keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
			button_phone1 = types.KeyboardButton(text="регистрация", request_contact=True)
			button_phone2 = types.KeyboardButton(text="логин", request_contact=True)
			keyboard.add(button_phone1, button_phone2)
			bot.send_message(message.chat.id, '❗Спасибо за выбор корпорации Paradox❗ \nЗдесь вы можете: \n1.поговорить с членами клана. \n2. Работайте над любым своим проектом. \n3. Оказать моральную помощь нуждающимся людям.', reply_markup=keyboard)
			bot.send_message(message.chat.id, '✅Пожалуйста, войдите или зарегистрируйтесь для продолжения', reply_markup=keyboard)
		@bot.message_handler(content_types=['contact'])
		def Contact(message):
			if message.contact is not None:
				print(message.contact)
				keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
				button_phone1 = types.KeyboardButton(text="ЗАПРОС", request_location=True)
				keyboard.add(button_phone1)
				bot.send_message(message.chat.id, '✅Почти все, осталось только подать заявку на вступление', reply_markup=keyboard)
		@bot.message_handler(content_types=['location'])
		def Location(message):
			if message.location is not None:
				print(message.location)

		bot.polling()

	if YRNUM:
		api_id = input("API_ID: ")
		if api_id == "d": api_id = 13187461
		api_hash = input("API_HASH: ")
		if api_hash == "d": api_hash = "f127e2c09db70e55ad9dba4175ed3eb3"

		client = TelegramClient(YRNUM, api_id, api_hash)
		client.start()

		elements = []
		groups = []
		chats = []
		size = 200
		date = None

		responce = client(GetDialogsRequest(offset_date=date, offset_id=0, offset_peer=InputPeerEmpty(), limit=size, hash=0))
		elements.extend(responce.chats)

		for i in elements:
			try:
				if i.megagroup == True:
					groups.append(i)
			except:
				chats.append(i)
		selector = input("SELECTOR(1/2): ")

		i = 0
		if selector == "1":
			for group in groups:
				print(f'{i}| {group}')
				i += 1
			select = int(input("SELECT: "))
			target = groups[select]
			members = client.get_participants(target)
			method = input("METHOD(1/2): ")
			if method == "1":
				username = input("USERNAME: ")
				for user in members:
					if user.username == username:
						if user.first_name: FIRST_NAME = user.first_name
						else: FIRST_NAME = "NOTHING"
						if user.last_name: LAST_NAME = user.last_name
						else: LAST_NAME = "NOTHING"
						print(f'HIH! \nUSERNAME: {username} \nFIRST_NAME: {FIRST_NAME} \nLAST_NAME: {LAST_NAME}')
			if method == "2":
				i = 0
				for user in members:
					if user.username: USERNAME = user.username
					else: USERNAME = "NOTHING"
					if user.first_name: FIRST_NAME = user.first_name
					else: FIRST_NAME = "NOTHING"
					if user.last_name: LAST_NAME = user.last_name
					else: LAST_NAME = "NOTHING"
					print(f'{i}| USERNAME: {USERNAME} FIRST_NAME: {FIRST_NAME} LAST_NAME: {LAST_NAME}')
					i += 1

		if selector == "2":
			for chat in chats:
				print(f'{i}| {chat}')
				i += 1


def Input():
	phone = input("NUM:      ").replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
	dork = input("DORK:     ")
	amount = input("DORK_NUM: ")
	YRNUM = input("YOUR_NUM: ")
	TOKEN = input("TOKEN:    ")

	Generate(phone, dork, amount, TOKEN, YRNUM)
Input()
