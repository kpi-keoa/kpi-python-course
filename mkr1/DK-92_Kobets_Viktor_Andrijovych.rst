==============================
Кобець Віктор Андрійович
==============================


#. Гілки в Git: для чого використовуються, який принцип роботи з гілками. Наведіть команди для створення нової гілки та переключення
   між гілками.

   -Відповідь
      Гілки потрібні розгалудження проекту

      $ git branch (-NAME-) - створення нової гілки
      $ git checkout (-NAME-) - переключення між гілками

#. Як підтягнути зміни, що відбулись у віддаленому upstream-репозиторії (гілка master) до локального репозиторію? Наведіть команду.

   -Відповідь
      git pull - стягуємо всі оновлення.
   
      git merge master - синхронізуємо в нашу гілку с гілкою мастер.

      git rebase master - якщо особиста гілка можно так.

#. Множина (set). Для чого слугує? Чим відрізняється від списку (list) та кортежа (tuple)? Наведіть приклади використання.

   -Відповідь
      Множина(set) — невпорядкована послідовність, що не індексується. Однакові елементи не допускаються. 

      Кортеж(tuple) - послідовність, яка впорядкована, але не змінюється. Допускаються однакові елементи.

      Список(list) — впорядкована послідовність, яку можна змінювати. Допускаються однакові елементи.

      exemple = {"Kobets", "Vity", "Viktor", "Viktor"}
      print(exemple)

      Вивод:

      {"Kobets", "Viktor", "Vity"}

#. Яким чином можна виконати замір швидкості виконання блоку коду Python?
   Що є швидшим для розрахунку квадратного кореня: оператор піднесення до степеню, функція піднесення для степеню з бібліотеки
   ``math`` чи спеціалізована функція взяття квадратного кореню з ``math``? Наведіть приклад коду, що визначає швидкість виконання
   для кожного з випадків.

   -Відповідь
   import datetime
   import math

   start = datetime.datetime.now()
   
   num = 25
   sqrt = num ** (0.5)
   print("Квадратный корень из числа "+str(num)+" это "+str(sqrt))
   
   finish = datetime.datetime.now()
   print finish-start
   
   start = datetime.datetime.now()
  
   num = 25
   sqrt = math.sqrt(num)
   print("Квадратный корень из числа " + str(num) + " это " + str(sqrt))
   
   finish = datetime.datetime.now()
   print finish-start

#. Аргументи функцій. Які типи (концептуально) аргументів бувають? Наведіть приклад функції, яка виводить свої аргументи.

   -Відповідь
      позиційні - передаються у тому порядку, у якому визначено під час створення функції. Тобто порядок передачі аргументів визначає, яке значення набуде кожен аргумент
      
      ключові - передаються із зазначенням імені аргументу та його значення. У такому разі аргументи можуть бути вказані в будь-якому порядку, тому що їх ім'я вказується явно.
      
      Спочатку завжди йдуть позиційні.

      def Argument(v):
         print('Argument.v = ', v)
         return

#. Наведіть приклад функції, що **коректно** приймає в якості значення за замовчанням immutable-об'єкт.
   Чому коректно робити саме так?

   -Відповідь
      Функції що **коректно** приймає в якості значення за замовчанням immutable-об'єкт - bool, int, float, tuple, str, frozenset.

      Об'єкти вбудованих типів, таких як (int, float, bool, str, tuple, frozenset) є незмінними. 
      Об'єкти вбудованих типів, таких як (list, set, dict) змінюються. 
      Користувальницькі класи зазвичай змінюються. Щоб змоделювати незмінність у класі, необхідно перевизначити встановлення та видалення атрибутів, щоб викликати винятки.


#. Конструкція умовного виконання Python. Яким чином можна реалізувати перевірку логічного виразу *A x B*, де x – XOR.
   Наведіть приклад коду.

   -Відповідь
      a = int(input())
      b = int(input())

      if a!= b:
         print("1")
      else:
         print("0")

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
      class Animal:
         likes_water
 
      class Mammal(Animal):
         def milk()
         {name}: delicious!"

      class Cat(Mammal):
         

      class Dog(Mammal):
         def swim()
         {name}: swimming makes me feel good

      class Amphibian(Animal):
         def swim()
         {name}: swimming makes me feel good
