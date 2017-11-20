import telebot
import datetime 

#vars
token = '460527419:AAHsDnHf6ZHSAvZdy6Z4hv3n3NfrEU7UOkI'
bot = telebot.TeleBot(token)
#d = datetime.date.today()
#we = datetime.date(d.year, d.month, d.day)

#schedule
Monday = ["Информатика", "ОБЖ", "Алгебра", "Биология", "Элективный урок математики", "Элективный урок информатики"]
Tuesday = ['Обществознание', "Физкультура", "География", "Геометрия", "Англиский язык", "УПК"]
Wednesday = ['Англиский язык', "История", "Физика", "Литература", "Русский язык", "Элективный урок физики", "Элективный урок русского языка"]
Thursday = ['История', "Физкультура", "Алгебра", "Русский язык", "МХК", "Элективный урок математики"]
Friday = ['Англиский язык', "Физкультура", "Литература", "Геометрия", "Экономика", "УПК"]
Saturday = ['Элективный урок математики', "Химия", "Литература", "Физика", "Алгебра", "Элективный урок физики"]


def week_day(int, plus = 0):
	if we.weekday() + plus == 0:
		mess = Monday[int]
	elif we.weekday() + plus == 1:
		mess = Tuesday[int]
	elif we.weekday() + plus == 2:
		mess = Wednesday[int]
	elif we.weekday() + plus == 3:
		mess = Thursday[int]
	elif we.weekday() + plus == 4:
		mess = Friday[int]
	elif (we.weekday() == 5): mess = Saturday[int]
	elif (we.weekday() == 6) and (plus == 1): mess = Monday[int]	
	else: mess='Выходной (Занятй нет)'
	return str(mess)
		
		
		
#handlers
@bot.message_handler(commands=['start', 'help'])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, 'Приветствую тебя, я твой помощник в telegram ;_)')

@bot.message_handler(regexp='расписание на завтра')
def schedule(message):
	global d
	global we 
	d = datetime.date.today()
	we = datetime.date(d.year, d.month, d.day)
	x = 0
	while x < 10:
		try: s = week_day(x, 1)
		except IndexError: break;
		bot.send_message(message.chat.id, s)
		if week_day(x, 1) == 'Выходной (Занятй нет)':
			break;
		x = x + 1
    
@bot.message_handler(regexp='расписание')
def schedule(message):
	global d
	global we 
	d = datetime.date.today()
	we = datetime.date(d.year, d.month, d.day)
	x = 0
	while x < 10:
		try: s = week_day(x)
		except IndexError: break;
		bot.send_message(message.chat.id, s)
		if week_day(x) == 'Выходной (Занятй нет)':
			break;
		x = x + 1

@bot.message_handler(regexp='редактировать')
def schedule(message):
	bot.send_message(message.chat.id, 'Типо распиисание')
#main
if __name__ == '__main__':
    bot.polling(none_stop=True)
