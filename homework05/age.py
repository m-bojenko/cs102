import datetime as dt
from datetime import date
from statistics import median
from typing import Optional

from api import get_friends
from api_models import User


def age_predict(user_id: int) -> Optional[float]:
    """ Наивный прогноз возраста по возрасту друзей
    Возраст считается как медиана среди возраста всех друзей пользователя
    :param user_id: идентификатор пользователя
    :return: медианный возраст пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"

    friends = get_friends(user_id, 'bdate')
    count = 0
    sum = 0
    today = date.today()
    for num in range(0, len(friends)):
        try:
            birthd = friends[num].bdate.split('.')
        except:
            pass
        else:
            print(birthd)
            try:
                year = int(birthd[2])
            except:
                pass
            else:
                year = today.year - year
                if today.month < int(birthd[1]) or today.month == int(birthd[1]) and today.day < int(birthd[0]):
                    year -= 1
                count += 1
                sum += year


    if count > 0:
        return sum / count
    else:
        return None

print(age_predict(84213446))
