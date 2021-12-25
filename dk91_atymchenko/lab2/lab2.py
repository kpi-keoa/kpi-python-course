class Shop():
	def __init__(self, chain, owner_name, owner_surname):
		self.chain = chain
		self.name = owner_name
		self.surname = owner_surname

	def shop_name(self):
		print(f"{self.chain}|{self.owner_surname} {self.owner_name}")

class Product(Shop):
        def __init__(self, chain, owner_name, owner_surname, department_amount):
                Shop.__init__(self, chain, owner_name, owner_surname)
                self.department = department_amount

        def amount(self):
                print(f"The total amount of departments is {self.department}")

class Closes(Shop):
        def __init__(self, chain, owner_name, owner_surname, department):
                Shop.__init__(self, chain, owner_name, owner_surname)
                self.department = department

        def amount(self):
                print(f"The total amount of departments is {self.department}")

class Techique(Shop):
        def __init__(self, chain, owner_name, owner_surname, department):
                Shop.__init__(self, chain, owner_name, owner_surname)
                self.department = department

        def amount(self):
                print(f"The total amount of departments is {self.department}")

class Drinks(Product):
        def __init__(self, chain, owner_name, owner_surname, department, drink_name = "Wine", price = 500):
                Product.__init__(self, chain, owner_name, owner_surname, department)
                self.drink_name = drink_name

        def print_drink(self):
                print(f"{self.drink_name} costs {self.price}")

if __name__ == '__main__':
        s = Shop("Silpo", "Vladimir", "Kostelman")
        s.shop_name()

        p = Product("Silpo", "Vladimir", "Kostelman", 7)
        p.amount()

	c = Closes("Zara", "Oscar", "Marcote", 4)
        c.amount()

        t = Techique("Citrus", "Grigory", "Topal", 5)
        t.amount()

        d = Drinks("Silpo", "Vladimir", "Kostelman", "Alcohol")
        d.print_drink()