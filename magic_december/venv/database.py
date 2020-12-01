from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///messages.db")  # экз. класса Engine, отвеч. за подключение к БД
# выбираем базу данных sqlite и она будет записана в файлик messages.db
session = sessionmaker(bind=engine)

class Messages(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    message1 = Column(String)
    message2 = Column(String)
    link = Column(String)
    photo = Column(String)
    sticker = Column(String)


Base.metadata.create_all(bind=engine)

s = session()
'''1 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''2 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''3 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''4 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''5 декабря'''
messages = Messages(message1='Хо-хо-хо! Уже догадался с кем связан сегодняшний день? Сегодня отмечается день рождения Санта Клауса!',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''6 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''7 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''8 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''9 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''10 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''11 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''12 декабря'''
messages = Messages(message1='день пряничного домика',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''13 декабря'''
messages = Messages(message1='день хажжёных свечей, день горячего какао',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''14 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''15 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''16 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''17 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''18 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''19 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''20 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''21 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''22 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''23 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''24 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''25 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''26 декабря'''
messages = Messages(message1='Приветствую! Почему так серьезно? Сегодня очень важный день месяца. 26 декабря - Международный день подарков! Не забудь закупиться подарками для всех любимых и родных! Не оставляй всё на 31 число) А Бенедикт Кэмбербетч расскажет, как правильно реагировать на подарки, которые не ответили твоим ожиданиям.',
                    message2='Лови ссылку на видос:',
                    link='https://www.youtube.com/watch?v=2x9X0Y49XlE&feature=youtu.be',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''27 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''28 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''29 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''30 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

'''31 декабря'''
messages = Messages(message1='',
                    message2='',
                    link='',
                    photo='',
                    sticker='')
s.add(messages)
s.commit()

