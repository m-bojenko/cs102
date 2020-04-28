from bottle import route, run, template, request, redirect
from scraputils import get_news
from database import News, session

from bayes import NaiveBayesClassifier


@route('/news')
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route('/add_label/')
def add_label():
    # 1. Получить значения параметров label и id из GET-запроса
    # 2. Получить запись из БД с соответствующим id (такая запись только одна!)
    # 3. Изменить значение метки записи на значение label
    # 4. Сохранить результат в БД

    our_label = request.query.label

    our_id = request.query.id

    s = session()
    our_news = s.query(News).filter(News.id == our_id).one()  # т. о. это объект класса News
    our_news.label = our_label  # обновление записи (не факт, что работает)

    s.commit()
    redirect('/news')


@route('/update')
def update_news():

    # 1. Получить данные с новостного сайта
    # 2. Проверить, каких новостей еще нет в БД. Будем считать,
    #    что каждая новость может быть уникально идентифицирована
    #    по совокупности двух значений: заголовка и автора
    # 3. Сохранить в БД те новости, которых там нет

    news_ar = get_news('https://news.ycombinator.com/newest', n_pages=1)
    s = session
    news_in_base = s.query(News).all()
    for new in news_ar:
        counter = 0
        for new_in_base in news_in_base:
            if (new['title'] == new_in_base.title) and (new['author'] == new_in_base.author):
                counter = 1
        if counter == 0:
            new_new = News(title=new['title'],
                           author=new['author'],
                           url=new['url'],
                           comments=new['comments'],
                           points=new['points'])
            s.add(new_new)
            s.commit()

    redirect('/news')


@route('/classify')
def classify_news():
    s = session()
    news = s.query(News).filter(News.label != None).all()
    titles = [new.title for new in news]
    labels = [new.label for new in news]

    classificator = NaiveBayesClassifier(titles, labels)

    return classificator


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/recommendations')
def recommendations():
    # 1. Получить список неразмеченных новостей из БД
    # 2. Получить прогнозы для каждой новости
    # 3. Вывести ранжированную таблицу с новостями
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    titles = [row.title for row in rows]
    new_labels = classify_news().predict(titles)
    for i in range(len(new_labels)):
        rows[i].label = new_labels[i]
        s.commit()
    return template('news_recommendations', rows=rows)


if __name__ == "__main__":
    run(host='localhost', port=8080)
