Для демонстрации владения работы с классами в python был написан скрипт.
В скрипте имеются: класс родитель - tank, классы наследники light_tank, sp_artillery, at_sp_artillery.
От класса light_tank наследуется класс medium_tank, от класса medium_tank
наследуется класс heavy_tank. Также был использован конструктор __init__ и специальный (magic-, он же dunder-) метод 
для переопределения вывода объекта в виде строки __str__ и __len__. Было предусмотрено использование скрипта как отдельного
модуля.