import telebot
from datetime import date
import calendar
from typing import List, Tuple


access_token = '1469858290:AAHpCC6exxgDwV-MZA-uVs9K4UrSUE97gNk'
# Создание бота с указанным токеном доступа
bot = telebot.TeleBot(access_token)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('about', '/help')
keyboard1.row('/today')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, дружок! Я твой волшебный бот, и сделаю твой декабрь самым невероятным!')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJek1-5QUtIAp0dqfyQ9PbvaTemjcDzAAI6BAAC8n6CDKMem-mzqfIiHgQ', reply_markup=keyboard1)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Дружок, тебе нужна помощь? Давай немного объясню тебе, как я работаю. Ты можешь послать мне следующие команды: /start - для начала нашего знакомства, /today - чтоб узнать, какой сюрприз я заготовил для тебя на сегодня, /about - чтоб узнать о моём авторе')
    bot.send_message(message.chat.id, 'К сожалению, я пока еще мало чего умею, я ещё маленький) Но я постараюсь сделать твой декабрь как можно более тёплым и уютным, наполненным любовью и волшебством. А если какие-то твои проблемы я всё-таки не решил, напиши моему создателю:')

'''
# Бот будет отвечать только на текстовые сообщения
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)
    lemonade = 'Off the juice, codeine got me trippin'
    if message.text.lower() == 'hey' :
        bot.send_message(message.chat.id, lemonade)
'''

@bot.message_handler(commands=['book'])
def which_book(message):
    mess = message.text.split()
    bot.send_photo(message.chat.id, open('books/' + str(mess[1]) + '.jpg', 'rb'))


# Returning things in current day
@bot.message_handler(commands=['today'])
def magic_things(message):
    today_date = date.today()
    if today_date.day == 1:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJswl_FiA_fjlL4nj42cH3MiwMY6izPAALAAAMWQmsKlyv9IKye0NYeBA')
        bot.send_message(message.chat.id, 'Ну что? На старт, внимание... Декабрь! Самый волшебный месяц в году закончится самой волшебной ночью. Но ведь не из-за одной ночи мы так любим Новый год. Мы любим его из-за новогодней суеты, любим ходить по магагзинам в поисках подарков или рыться в интернет-маркетах, для каждого своё) Любим готовить на праздничный стол, печь пряники, пить какао в тёплой, уютной квартире, когда за окном мороз и метель, и пересматривать старые добрые фильмы. А я каждый день этого волшебного месяца буду тебя развлекать и дарить мою любовь. Думаешь боты не умеют любить? Ха! Ну давай вместе выясним! Лови мой первый подарок тебе - невероятный декабрьский календарь!')
        bot.send_document(message.chat.id, open('calendar.pdf', 'rb'))
    elif today_date.day == 2:
        pass
    elif today_date.day == 3:
        bot.send_message(message.chat.id, 'Бррр... Да уж. Уже совсем не жарко на улице. В такие дни хочется зарыться в плед, заварить горячего чая или сварить какао и почитать какую-нибудь зимнюю книжку. А я могу помочь тебе с выбором отличной книжки для прочтения. Пришли мне цифру той книги, описание которой тебе понравилось больше всего.')
        for i in range(1, 11):
            bot.send_photo(message.chat.id, open('descriptions/' + str(i) + '.png', 'rb'))

    elif today_date.day == 5:
        bot.send_message(message.chat.id, 'Привеееет! Задание для тебя на сегодня: улыбнись! Не забывай, что волшебство декабря начинается с волшебства в наших сердцах. Дари любовь, и люди будут дарить тебе её в ответ.')
        bot.send_message(message.chat.id, 'Лови ссылку на видос: https://www.youtube.com/watch?v=5F-_ADuqIsk&feature=youtu.be')
    elif today_date.day == 6:
        bot.send_message(message.chat.id, 'Хо-хо-хо! Уже догадался, с кем связан сегодняшний день? Сегодня отмечается день рождения Санта Клауса!')
    elif today_date.day == 21:
        crossword = open('Krysha_ote_lya_Grand_s_20_00_1.pdf', 'rb')
        bot.send_message(message.chat.id, 'Тааак... Твёрдое физическое состояние воды... 3 буквы... По вертикали... Уже догадался, с чем связан сегодняшний день?! Сегодня день рождения кроссворда. Поэтому предлагаю тебе вместе со мной пройти кроссворд. Найди секретное слово и отправь его мне. В случае, если ты отравишь мне правильное слово, тебя ждёт сюрприз)')
        bot.send_document(message.chat.id, crossword)
    elif today_date.day == 26:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJfIF-6gTt8qjl2XkfG88tuhFWQEJlvAAKQMgACns4LAAGmwpPjaVLGPB4E')
        bot.send_message(message.chat.id, 'Приветствую! Почему так серьезно? Сегодня очень важный день месяца. 26 декабря - Международный день подарков! Не забудь закупиться подарками для всех любимых и родных! Не оставляй всё на 31 число) А Бенедикт Кэмбербетч расскажет, как правильно реагировать на подарки, которые не ответили твоим ожиданиям:')
        bot.send_message(message.chat.id, 'Лови ссылку на видос: https://www.youtube.com/watch?v=2x9X0Y49XlE&feature=youtu.be')





if __name__ == '__main__':
    bot.polling(none_stop=True)
