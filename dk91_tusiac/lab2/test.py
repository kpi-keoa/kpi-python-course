#! usr/bin/evn python3

import lab2

h1 = lab2.House('h_1', 12, 'street_1')
h2 = lab2.BigHouse('h_2', 25, 'street_2')
h3 = lab2.Trailer('h_3', 2, 'street_3')

print(h1)
print(h2)
print(h3)

h2.rooms_up()
print('rooms_up: ', h2)
h2.rooms_down()
print('rooms_down: ', h2)

h3.set_street('new_street')
print('set_street: ', h3)
h3.reset_street()
print('reset_street: ', h3)
