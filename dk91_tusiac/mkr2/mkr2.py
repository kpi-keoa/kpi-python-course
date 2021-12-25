#! bin/usr/env python3

#url = 'https://www.maultalk.com/ipb.html?showuser=255502'

import requests

def find_v(url):
    find = 'Просмотров профиля: '
    response = requests.get(url)
    url_text = response.text
    veiws = url_text.split(find)[1][0:10]
    v = ''
    for cnt in range(10):
        if veiws[cnt]!='<':
            v = v + veiws[cnt]
        else:
            print(f'{find} = {v}')
            break
    
        
        




