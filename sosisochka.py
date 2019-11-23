import telebot
from telebot import apihelper
import requests
from datetime import date
import calendar
import time
from bs4 import BeautifulSoup
from typing import List, Tuple

token = '931957752:AAEgcqI9NDRG4uwaZTWcSqzPk5YYG0j4By8'
apihelper.proxy = {'https': 'https://141.125.82.106:80'}
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['near'])
def say_hi(message):
    resp = '{}: Привет, я Сосисочка Бот \n'
    resp += '{}: Моей ключевой обязанностью является знать расписание студентов Университета ИТМО \n'
    resp += '{}: Я умею выполнять несколько команд: \n'
    return bot.send_message(message.chat.id, resp, parse_mode='HTML')

def get_page(group: str, week: str = '') -> str:
    dom = 'http://www.ifmo.ru/ru/schedule'
    if week:
        week = str(week) + '/'
    url = '{domain}/0/{group}/{week}raspisanie_zanyatiy_{group}.htm'.format(
        domain=dom,
        week=week,
        group=group
    )
    response = requests.get(url)
    web_page = response.text
    return web_page


def parse_schedule_for_a_day(web_page: str, day: str) -> Tuple[List[str], List[str], List[str]]:
    soup = BeautifulSoup(web_page, "html5lib")
    if day == 'monday':
        schedule_table = soup.find("table", attrs={"id": "1day"})
    if day == 'tuesday':
        schedule_table = soup.find("table", attrs={"id": "2day"})
    if day == 'wednesday':
        schedule_table = soup.find("table", attrs={"id": "3day"})
    if day == 'thursday':
        schedule_table = soup.find("table", attrs={"id": "4day"})
    if day == 'friday':
        schedule_table = soup.find("table", attrs={"id": "5day"})
    if day == 'saturday':
        schedule_table = soup.find("table", attrs={"id": "6day"})
    if day == 'sunday':
        schedule_table = None

    if schedule_table == None or day == 'sunday':
        times_list = ['']
        locations_list = ['']
        lessons_list = ['']
        return times_list, locations_list, lessons_list

    # Время проведения занятий
    times_list = schedule_table.find_all("td", attrs={"class": "time"})
    times_list = [time.span.text for time in times_list]

    # Место проведения занятий
    locations_list = schedule_table.find_all("td", attrs={"class": "room"})
    locations_list = [room.span.text for room in locations_list]

    # Название дисциплин и имена преподавателей
    lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
    lessons_list = [lesson.text.split('\n\n') for lesson in lessons_list]
    lessons_list = [', '.join([info for info in lesson_info if info]) for lesson_info in lessons_list]

    return times_list, locations_list, lessons_list


@bot.message_handler(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
def get_schedule(message):
    """ Получить расписание на указанный день """
    # days_of_the_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = message.text
    day = day[1:]
    day = day.split()
    if len(day) == 1:
        return bot.send_message(message.chat.id, 'Введите номер группы', parse_mode='HTML')
    days = day[0]
    if days == 'sunday':
        return bot.send_message(message.chat.id, 'Воскресенье выходной, отдыхай', parse_mode='HTML')
    group = day[1]
    web_page = get_page(group)
    times_lst, locations_lst, lessons_lst = \
        parse_schedule_for_a_day(web_page, days)
    resp = ''
    for time, location, lesson in zip(times_lst, locations_lst, lessons_lst):
        resp += '<b>{}</b>, {}, {}\n'.format(time, location, lesson)
    return bot.send_message(message.chat.id, resp, parse_mode='HTML')


def now_time():
    clock = list()
    clock.append(time.localtime().tm_hour)
    clock.append(time.localtime().tm_min)
    return clock


def now_day():  # ДЕНЬ НЕДЕЛИ
    my_date = date.today()
    day = calendar.day_name[my_date.weekday()]
    day = day.lower()
    return day


def check_week():
    week = time.strftime("%W", time.localtime())
    if int(week) % 2 == 0:
        return '1'
    else:
        return '2'


@bot.message_handler(commands=['near'])
def get_near_lesson(message):
    """ Получить ближайшее занятие """
    clock = now_time()
    days = now_day()
    week = check_week()
    mess = message.text
    mess = mess.split()
    group = ''
    if len(mess) == 1:
        return bot.send_message(message.chat.id, 'Введите номер группы')
    if len(mess) > 1:
        group = mess[1]
    Max_time = 24, 0
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    count = day_list.index(days)
    running = True
    web_page = get_page(group)
    while running:
        times_lst, locations_lst, lessons_lst = \
            parse_schedule_for_a_day(web_page, day_list[count])
        if times_lst == ['']:
            if count < 6:
                count += 1
                clock = 0, 0
            else:
                if week == '2':
                    week = '1'
                else:
                    week = '2'
                count = 0
                clock = 0, 0
                web_page = get_page(group, week)
        else:
            count2 = 0
            block = 0, 0
            for i in range(len(times_lst)):
                temp1 = times_lst[i]
                value_time = int(temp1[6:8]), int(temp1[9:11])
                helps = value_time[0] - clock[0], value_time[1] - clock[1]
                if Max_time >= helps and helps >= block:
                    running = False
                    num = i
                    Max_time = helps
                    count2 += 1

            if count2 == 0:
                if count < 6:
                    count += 1
                    clock = 0, 0
                else:
                    if week == '2':
                        week = '1'
                    else:
                        week = '2'
                    count = 0
                    clock = 0, 0
                web_page = get_page(group, week)
    day_times = day_list[count]
    resp = ''
    resp += '{}: <b>{}</b>, {}, {}\n'.format(day_times.title(), times_lst[num], locations_lst[num], lessons_lst[num])

    return bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['tomorrow'])
def get_tomorrow(message):
    """ Получить расписание на следующий день """
    days = now_day()
    week = check_week()
    mess = message.text
    mess = mess.split()
    group = ''
    if len(mess) == 1:
        return bot.send_message(message.chat.id, 'Введите номер группы')
    if len(mess) > 1:
        group = mess[1]
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if days == 'sunday':
        if week == '1':
            week = '2'
        else:
            week = '1'
        days = 'monday'
    elif days == 'saturday':
        return bot.send_message(message.chat.id, 'Завтра воскресенье - можешь выдохнуть')
    else:
        days = day_list[day_list.index(days) + 1]
    web_page = get_page(group, week)
    times_lst, locations_lst, lessons_lst = \
        parse_schedule_for_a_day(web_page, days)
    resp = ''
    for time, location, lesson in zip(times_lst, locations_lst, lessons_lst):
        resp += '<b>{}</b>, {}, {}\n'.format(time, location, lesson)
    return bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['all'])
def get_all_schedule(message):
    """ Получить расписание на всю неделю для указанной группы """
    week = check_week()
    mess = message.text
    mess = mess.split()
    group = ''
    if len(mess) == 1:
        return bot.send_message(message.chat.id, 'Введите номер группы')
    if len(mess) > 1:
        group = mess[1]
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    resp = ''
    for i in range(7):
        days = day_list[i]
        web_page = get_page(group, week)
        times_lst, locations_lst, lessons_lst = \
            parse_schedule_for_a_day(web_page, days)
        if times_lst != [''] or locations_lst != [''] or lessons_lst != ['']:
            for time, location, lesson in zip(times_lst, locations_lst, lessons_lst):
                resp += '{}: <b>{}</b>, {}, {}\n'.format(days.title(), time, location, lesson)
        else:
            resp += '{}: У тебя выходной намечается) \n'.format(days.title())
    return bot.send_message(message.chat.id, resp, parse_mode='HTML')


if __name__ == '__main__':
    bot.polling(none_stop=True)
