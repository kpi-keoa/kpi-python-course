import requests

from random import randint

anim = requests.post('https://pic.re/image').json()

file = open(f'{randint(0, 10000)}.jpg', 'wb')

file.write(requests.get(
	anim.get('file_url')
	).content)

file.close()

