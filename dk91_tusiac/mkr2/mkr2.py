#! bin/usr/env python3

#https://www.maultalk.com/user51887.html
#https://www.maultalk.com/user34865.html
#https://www.maultalk.com/user99329.html


import requests

users = {}

def add_user(url):
    find = 'Просмотров профиля: '
    response = requests.get(url)
    url_text = response.text
    veiws = url_text.split(find)[1][0:10]
    v = ''
    for cnt in range(10):
        if veiws[cnt]!='<':
            v = v + veiws[cnt]
        else:
            print(f'Profile views = {v}')
            users_value = v
            break
    find = ' - Просмотр профиля'
    url_text = response.text
    veiws = url_text.split(find)[0][-10:]
    v = ''
    for cnt in range(9, 0, -1):
        if veiws[cnt]!='>':
            v = v + veiws[cnt]
        else:
            print(f'User name = {v}')
            users[v] = users_value
            break

    
def print_list(p_list):
    len(p_list)
    for u_key in p_list:
        print(f'{u_key} = {p_list[u_key]}')

        
def sort(the_list):
    sort_list = dict(sorted(the_list.items(), key = lambda item: int(item[1])))
    print_list(sort_list)      


    
        
        
        




