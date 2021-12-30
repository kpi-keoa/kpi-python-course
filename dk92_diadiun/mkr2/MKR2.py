
'''4. Написать скрипт, ранжирующий пользователей по социальной активности.
   
   Скрипт принимает в качестве аргументов имена профилей в любой социальной сети
   (или на форуме).
   Скрипт делает обращение к API, определяя социальную активность каждого пользователя
   (например, по количеству лайков или сообщений на форуме).
   
   На выходе, скрипт выдает список формата "пользователь – активность".
   Список отсортирован по ниспаданию активности.
   
   Готовые реализации не использовать категорически.
   Использовать сторонние библиотеки для API-запросов разрешается'''

import requests as reqs
import json

API_KEY = "AIzaSyCFWHLMZan7mE1-M5wT-kl6w2H-AJy8kXQ"

ID = "UC0lT9K8Wfuc1KPqm6YjRf1A"


def get_sub_cnts(channel_ids, print_rating=False):
    sublist = [(None, None)] * len(channel_ids)
    wr_cnt = 0

    for cnt in range(2):
        HTTP_addr = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=' + \
                    channel_ids[cnt] + '&key=' + API_KEY
        response = reqs.get(HTTP_addr)

        response_dict = response.json()

        items = response_dict["items"]

        for items_all in items:
            sublist[cnt] = [channel_ids[cnt], int(items_all['statistics']['subscriberCount'])]

    if print_rating:
        for top_rate in range(len(channel_ids)):
            print(top_rate + 1, ' place ',
                  sublist[top_rate][0], ' : ', sublist[top_rate][1])

    return sublist


channels_top = get_sub_cnts(
    ["UC0lT9K8Wfuc1KPqm6YjRf1A", "UCEdvpU2pFRCVqU6yIPyTpMQ"], True)

"""
1  place  UC0lT9K8Wfuc1KPqm6YjRf1A  :  5240000
2  place  UCEdvpU2pFRCVqU6yIPyTpMQ  :  54500000
"""
