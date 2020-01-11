import time
import requests

from api_models import User

import config


def get(url, params={}, timeout=5, max_retries=5, backoff_factor=0.3):
    """ Выполнить GET-запрос

    :param url: адрес, на который необходимо выполнить запрос
    :param params: параметры запроса
    :param timeout: максимальное время ожидания ответа от сервера
    :param max_retries: максимальное число повторных запросов
    :param backoff_factor: коэффициент экспоненциального нарастания задержки
    """
    delay = 2
    for tryes in range(max_retries):
        try:
            response = requests.get(url, params=params, timeout=timeout)
        except requests.exceptions.RequestException:
            if tryes == max_retries - 1:
                raise
        else:
            return response
        time.sleep(delay)
        delay = backoff_factor * (2 ** tryes)


def get_friends(user_id, fields):
    """ Returns a list of user IDs or detailed information about a user's friends """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"

    domain = "https://api.vk.com/method"
    access_token = '949de9049e46bce7b329236f68f0f6f94d2fc0656ef260dde73273342572c4f62a837405b5b769f0c501d'
    user_id = user_id
    fields = fields
    v = '5.103'

    q_params = {
        'domain': domain,
        'access_token': access_token,
        'user_id': user_id,
        'fields': fields,
        'v': v
    }

    query = f"{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v={v}".format(
        **q_params)
    response = get(query).json()


    try:
        response = response['response']['items']
    except:
        return []


    for num, friend in enumerate(response):
        user = User(id=friend['id'], first_name=friend['first_name'],
                    last_name=friend['last_name'], online=friend['online'])
        try:
            user.bdate = friend['bdate']
        except:
            pass
        response[num] = user
    return response

