class Shop():
    def __init__(self, shopName, ownerName, ownerSurname, departmentAmount):
        self.shopName = shopName
        self.ownerName = ownerName
        self.ownerSurname = ownerSurname
        self.departmentAmount = departmentAmount

    def shop_name_validator(self):
        if isinstance(self.shopName, str):
            return True
        print("Please, enter a valid shop's name")
    def owner_surname_validator(self):
        if isinstance(self.ownerSurname, str):
            return True
        print("Please, enter a valid owner's surname")
    def owner_name_validator(self):
        if isinstance(self.ownerName, str):
            return True
        print("Please, enter a valid owner's name")
    def department_amount_validator(self):
        if isinstance(self.departmentAmount, int) and self.departmentAmount > 0:
            return True
        print ("Please, enter a valid amount of departments")
    def shop_details(self):
        if self.shop_name_validator() and self.owner_surname_validator() and self.owner_name_validator() and self.department_amount_validator():
            print(f"\nOwner of '{self.shopName}' is {self.ownerSurname} {self.ownerName}. It has {self.departmentAmount} departments")
        return     
    def amount(self):
        if self.department_amount_validator():
            print(f"The total amount of departments is {self.departmentAmount}")
        return
    
class Product(Shop):
    def __init__(self, shopName, ownerName, ownerSurname, departmentAmount, departmentName):
        super().__init__(shopName, ownerName, ownerSurname, departmentAmount)
        self.departmentName = departmentName

    def shop_details(self):
        super().shop_details()
    def department(self):
        print(f"This is {self.departmentName} department")

class Clothes(Shop):
    def __init__(self, shopName, ownerName, ownerSurname, departmentAmount, clothesType):
        super().__init__(shopName, ownerName, ownerSurname, departmentAmount)
        self.clothesType = clothesType

    def shop_details(self):
        super().shop_details()
    def clothes_for(self):
        print(f"This shop is for {self.clothesType}")

class Techique(Shop):
    def __init__(self, shopName, ownerName, ownerSurname, departmentAmount, apartamentPart, departmentNumber = 0):
        super().__init__(shopName, ownerName, ownerSurname, departmentAmount)
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
        super().shop_details()
    def goods_are_here(self):
        print(f"{self.apartamentPart} appliances are in department {self.departmentNumber}")

class Drinks(Product):
    def __init__(self, shopName, ownerName, ownerSurname, departmentAmount, departmentName, drinkName = "Wine", price = 500):
        super().__init__(shopName, ownerName, ownerSurname, departmentAmount, departmentName)
        self.drinkName = drinkName
        self.price = price

    def shop_details(self):
        super().shop_details()
        super().department()
    def print_drink(self):
        print(f"{self.drinkName} costs {self.price}UAH")

if __name__ == '__main__':  
    s = Shop("Silpo", "Vladimir", "Kostelman", 7)
    
    p = Product(s.shopName, s.ownerName, s.ownerSurname, s.departmentAmount, "Alcohol")
    
    c = Clothes("Zara", "Oscar", "Marcote", 4, "Women")
    c.shop_details()
    c.clothes_for()
    
    t = Techique("Citrus", "Grigory", "Topal", 8, "Kitchen")
    t.shop_details()
    t.goods_are_here()
    
    d = Drinks(p.shopName, p.ownerName, p.ownerSurname, p.departmentAmount, p.departmentName)
    d.shop_details()
    d.print_drink()
    
