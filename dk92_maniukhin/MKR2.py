#D:\FLStudio20\ASIO4ALL v2

import os
from datetime import datetime

path = input('Enter path file: ')
user_date = input('Enter the date you need (01/01/1991): ')
user_date = datetime.strptime(user_date, '%d/%m/%Y')

paths_list = []
files_date = []

for file in os.listdir(path):
    paths_list.append(os.path.join(path, file))

for item in paths_list:
    files_date.append(datetime.fromtimestamp(os.path.getctime(item)).strftime('%d/%m/%Y'))

for x in files_date:
    date = datetime.strptime(x, '%d/%m/%Y')

    if date < user_date:
        continue
    elif date > user_date:
        print(f'{item}  /-/  {date}')
    else:
        print('No such files!')





