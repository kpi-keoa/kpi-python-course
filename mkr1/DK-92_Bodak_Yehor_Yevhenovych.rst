==============================
Бодак Єгор Євгенович
==============================
#. Як підтягнути зміни, що відбулись у віддаленому upstream-репозиторії (гілка master) до локального репозиторію? Наведіть команду.

-Відповідь
   
#. Що таке об'єднання гілок та для чого використовується? Конфлікти при об'єднанні.
   Наведіть приклад конфлікту (синтаксис) та команди для внесення змін до репозиторію після вирішення конфлікту.

   -Відповідь
   Об'еднання гілок це порівння файлів між собою де головним файлом виступає оригінал, а файл який схрещують
   має зміни які пітрібно додати. Конфлікти виникають коли при об'єднанні гілок два розробника виконують протидію, тобто 
   вносять зміни де один розробник додає файл, а інший видаляє. 

#. Перерахуйте та коротко окресліть відомі вам **базові** типи даних Python.
   -Відповідь
   int, float - числа 
   char - символ 
   string - строка
   tuple - кортеж(різні типи даних)
   list - список

#. МMножина (set). Для чого слугує? Чим відрізняється від списку (list) та кортежа (tuple)? Наведіть приклади використання.
   
   -Відповідь
   Список це послідовність елементів символів, а кортеж зберігає послідовність типів даніх кожного символа.
   Множина відрізняється тим, що не має послідовності і елементи не індексіруються.


#. Створіть функцію, яка приймає в якості першого аргументу бажаний опір паралельно з'єднаних резисторів *R* [Ом],
   а в якості подальших аргументів – величини резисторів, що є в наявності [Ом].
   Функція повертає кортеж (tuple), першим елементом якого є словник типу ``{номінал: кількість}``, а другим
   елементом – абсолютне відхилення результуючого опору від бажаного [Ом].

   -Відповідь

#. Docstring у функціях. Для чого використовуються? Наведіть приклад функції, що виконує розрахунок за певною формулою
   з області електроніки або фінансів (на власний розсуд) та містить Docsting (Coding Style – Google)
   
   -Відповідь
	""" Документація функції розрахунку частоти зрізу

	Ця функція  виконує простий розрахунок по формулі з урахуванням даних
	які вносить користувач. Зміні для запису мають тип float для того, щоб
	не ускладнювати структуру функції.
   
		$ Коефіцієнти що вказані вформулі є не змінними.
		$ Розрахунок підходить для дифренційного та інтегруючого фультру
		так як метод підключення не впливає на їх параметри, результат не змінюється

        """
	print("--Програма для розрахунку частотного зрізу RC-фільтру")

   	R = float(input("R = "))
	C = float(input("C = "))

	rez = 1.0 / (2.0 * 3.14 * R * C)

	print(R, " ",C)
	print("Rezult: F = ", rez)

#. Які цикли Python вам відомі? Яким чином можна примусово вийти з циклу?
   
   -Відповідь
   for, while - примусовий вихід може бути визваний break, або коли ми повертаємо значення return()


#. Створити клас Animal. Унаслідувати від нього два класи *Mammal* та *Amphibian*.
   Від класу *Mammal* унаслідувати два класи – *Cat* та *Dog*.
   Клас Animal передбачає наявність поля ``likes_water`` (на рівні класу, не об'єкта), яке за замовчуванням задане рівним ``False``
   і перевизначається в дочірніх класах (за необхідності).
   Для класу *Mammal* визначити метод ``milk()``, який виводитиме в стандартний вивід *"{name}: delicious!"*.
   Для *Amphibian* та *Dog* визначити метод ``swim()``, який виводитиме в стандартний вивід *"{name}: swimming makes me feel good"*.
   При написанні ``swim()`` уникати copy-paste, натомість, згрупувати єдину логіку в окрему функцію, яку викликатиме кожен клас.
   Замість *{name}* підставляти значення атрибута ``name``, який задається при створенні об'єкту.
   Навести приклад використання.

   -Відповідь
