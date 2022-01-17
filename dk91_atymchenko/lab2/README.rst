Для выполнения задания было создано родительский класс Shop,
3 наследника: Product, Closes и Techique (как разные виды магазинов),
и класс Drinks - наследник Product.

Пример вызова метода класса в другом классе: 
def shop_details(self):
        Product.shop_details(self)
        Product.department(self)

Так как Drinks является наследником Product, а Product, в свою очередь,
наследником Shop, то все три класса имеют одинаковую информацию о магазине
Поэтому, чтобы не задавать одни и те же параметры несколько раз, их
инициализация была проведена наследованием друг от друга:
s = Shop("Silpo", "Vladimir", "Kostelman", 7)
p = Product(s.shopName, s.ownerName, s.ownerSurname, s.departmentAmount, "Alcohol")
d = Drinks(p.shopName, p.ownerName, p.ownerSurname, p.departmentAmount, p.departmentName)
    
if __name__ == "__main__": Действия, описанные в этом блоке будут выполнены
при условии, что код запущен как модуль. Если же он импортирован в другой
скрипт - не выполняется.
