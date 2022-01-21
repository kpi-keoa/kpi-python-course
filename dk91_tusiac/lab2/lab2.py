#! usr/bin/evn python3

class House():
    def __init__(self, name, rooms, street):
        self.name = name
        self.rooms = rooms
        self.street = street

    def __str__(self):
        return 'Name the house: {}, number of rooms: {}, Name the street: {}'.format(self.name, self.rooms, self.street)

class BigHouse(House):
    def rooms_up(self):
        self.rooms += 5
    def rooms_down(self):
        self.rooms -= 5

class Trailer(House):
    def set_street(self, new_street):
        self.street = new_street
    def reset_street(self):
        self.street = 'default street'


def main():
    h1 = House('h_1', 12, 'street_1')
    h2 = BigHouse('h_2', 25, 'street_2')
    h3 = Trailer('h_3', 2, 'street_3')

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

if __name__ == '__main__':
    main()
