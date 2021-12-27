## Laboratory Work 2 OOP

Цель работы - создать несколько классов, реализовать наследие

В проекте есть:
- Родительский класс "Device"
Дочерние от него классы:
- "Laptop" - необходимые параметры: Модель, Год, Уровень заряда батареи
- "Tablet" - необходимые параметры: Модель, Год, Поколение, Подключен ли стилус, Уровень заряда батареи
- "Pencil" - необходимые параметры: Поколение, Уровень заряда батареи

**Реализован --str-- метод для вывода информации про выбранное устройство**

Для тестирования работы был написан следующий алгоритм (работает только при использовании как скрипта):
1. создан объект класса Laptop, Macbook Pro, 2019 год, 75% заряда
2. создан объект класса Tablet, IPad Pro, 2016 год, 2 поколение, стилус подключен, 98% заряда
3. создан объект класса Tablet, IPad Air, 2018 год, 3 поколение, стилус не подключен, 23% заряда
4. создан объект класса Pencil, IPencil, 1 поколение, 100% заряда
5. Получаем уровень заряда Macbook Pro
6. Смотрим поколение IPad Air
7. Проверяем, подключен ли стилус к IPad Pro
8. Устанавливаем новое значение заряда Macbook Pro - 50%
9. Подключаем к IPad Air стилус
10. Проверяем, подключен ли к IPad Air стилус сейчас
11. Для каждого объекта получаем общую информацию (текущие параметры для текущего класса)

## Результат выполнения скрипта

Macbook Pro Battery Charge: 75 %

IPad Air Device Generation: 3 

IPad Pro Pencil Connected: True 

Macbook Pro new battery charge: 50 %

IPad Air Pencil Now Connected?: True 

IPad Air Pencil Connected: True 

Device Model: Macbook Pro
Model Year: 2019
Battery Charge: 50%

Device Model: IPad Pro
Model Year: 2016
Device Generation: 2
Is Pencil Connected: True
Battery Charge: 98%

Device Model: IPad Air
Model Year: 2018
Device Generation: 3
Is Pencil Connected: True
Battery Charge: 23%

Device Model: IPencil
Device Generation: 1
Battery Charge: 100%
