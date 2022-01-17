class Shop():
    def __init__(self, shopName, ownerName, ownerSurname, departmentAmount):
        self.shopName = shopName
        self.ownerName = ownerName
        self.ownerSurname = ownerSurname
        self.departmentAmount = departmentAmount

    def shop_details(self):
        print(f"\nOwner of '{self.shopName}' is {self.ownerSurname} {self.ownerName}. It has {self.departmentAmount} departments")
    def amount(self):
        print(f"The total amount of departments is {self.departmentAmount}")

class Product(Shop):
    def __init__(self, shopName, ownerName, ownerSurname, departmentAmount, departmentName):
        Shop.__init__(self, shopName, ownerName, ownerSurname, departmentAmount)
        self.departmentName = departmentName

    def shop_details(self):
        Shop.shop_details(self)
    def department(self):
        print(f"This is {self.departmentName} department")

class Closes(Shop):
    def __init__(self, shopName, ownerName, ownerSurname, departmentAmount, closesType):
        Shop.__init__(self, shopName, ownerName, ownerSurname, departmentAmount)
        self.closesType = closesType

    def shop_details(self):
        Shop.shop_details(self)
    def closes_for(self):
        print(f"This shop is for {self.closesType}")

class Techique(Shop):
    def __init__(self, shopName, ownerName, ownerSurname, departmentAmount, apartamentPart, departmentNumber = 0):
        Shop.__init__(self, shopName, ownerName, ownerSurname, departmentAmount)
        if apartamentPart.lower() == "kitchen":
            departmentNumber = 1
        elif apartamentPart.lower() == "bathroom":
            departmentNumber = 2
        elif apartamentPart.lower() == "bedroom":
            departmentNumber = 3
        else:
            departmentNumber = 4
        self.apartamentPart = apartamentPart
        self.departmentNumber = departmentNumber

    def shop_details(self):
        Shop.shop_details(self)
    def goods_are_here(self):
        print(f"{self.apartamentPart} appliances are in department {self.departmentNumber}")

class Drinks(Product):
    def __init__(self, shopName, ownerName, ownerSurname, departmentAmount, departmentName, drinkName = "Wine", price = 500):
        Product.__init__(self, shopName, ownerName, ownerSurname, departmentAmount, departmentName)
        self.drinkName = drinkName
        self.price = price

    def shop_details(self):
        Product.shop_details(self)
        Product.department(self)
    def print_drink(self):
        print(f"{self.drinkName} costs {self.price}UAH")

if __name__ == '__main__':  
    s = Shop("Silpo", "Vladimir", "Kostelman", 7)
    
    p = Product(s.shopName, s.ownerName, s.ownerSurname, s.departmentAmount, "Alcohol")
    
    c = Closes("Zara", "Oscar", "Marcote", 4, "Women")
    c.shop_details()
    c.closes_for()
    
    t = Techique("Citrus", "Grigory", "Topal", 8, "Kitchen")
    t.shop_details()
    t.goods_are_here()
    
    d = Drinks(p.shopName, p.ownerName, p.ownerSurname, p.departmentAmount, p.departmentName)
    d.shop_details()
    d.print_drink()
    
