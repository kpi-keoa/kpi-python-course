==============================
Хижняк Андрій Валерійович
==============================


#. Локальні та віддалені репозиторії Git. Наведіть команду для відправки локальних комітів з гілки dev до віддаленого репозиторію.

Локальний репозиторій – це ваша копія репозиторію, коміти якої ідуть з вашої папки, в результаті ви отримуєте на локальній машині готове до роботи Git сховище.  Віддалений репозиторій – репозиторій з відкритим доступом для будь яких користувачів. Команда для відправки комітів - git push shared master

#. Як підтягнути зміни, що відбулись у віддаленому upstream-репозиторії (гілка master) до локального репозиторію? Наведіть команду.

origin/master

#. Наведіть код для створення списку, що містить в якості елементів цілочисленні значення від 1 до 19 (включно) з кроком 1,
   тобто 1, 3, 5, 7, 9, 11, 13, 15, 17, 19. У відповіді вирішальне значення має оптимальність конструкції.

>>> for i in range(1, 20, 2):
…     print(i)

#. Яким чином можна виконати замір швидкості виконання блоку коду Python?
   Що є швидшим для розрахунку квадратного кореня: оператор піднесення до степеню, функція піднесення для степеню з бібліотеки
   ``math`` чи спеціалізована функція взяття квадратного кореню з ``math``? Наведіть приклад коду, що визначає швидкість виконання
   для кожного з випадків.

import timeit

code = """
….
"""

elapsed_time = timeit.timeit(code, number=100)/100
print(elapsed_time)

timeit() автоматически будет использовать time.clock()

#. Створіть функцію, яка приймає в якості першого аргументу бажаний опір послідовно з'єднаних резисторів *R* [Ом],
   а в якості подальших аргументів – величини резисторів, що є в наявності [Ом].
   Функція повертає кортеж (tuple), першим елементом якого є словник типу ``{номінал: кількість}``, а другим
   елементом – абсолютне відхилення результуючого опору від бажаного [Ом].

   -
#. Keyword та keyword-only аргументи функцій. Яким чином функція може приймати довільне значення keyword-аргументів?
   Наведіть приклад (пов'язаний з галуззю електроніки, наприклад, розрахунок за формулою).

   Функції можна визивати за допомогою keyword arguments форми kwarg=value.
Коли є останній формальний параметр форми **name, він отримує словник, що містить в собі аргументи ключового слова. Це може бути поєднано з формальним параметром форми *name, який отримує кортеж, що містить позиційні аргументи поза списком формальних параметрів.


#. Конструкція умовного виконання Python. Наведіть приклад коду, де в умові обчислюється логічний вираз
   *(A && B) || ((!C) && (!D))*. Якщо умова виконується, вивести "OK" в стандартний вивід, якщо ні – вивести "FAIL"
   -
#. Які цикли Python вам відомі? Який цикл буде виконуватися швидше та чому?
   Наведіть приклад коду для виводу списка за допомогою кожного з типів циклу.

   Відомі цикли for та while, швидшим буде цикл for.
Цикл for:
>>> words = [1, 2, 3]
>>> for w in words:
...     print(w, len(w))
Цикл while:
>>> lst = [1, 2, 3, 4, 5, 6]
>>> i = 0
>>> while i < len(lst):
…    print(lst[i])
…    i += 1
