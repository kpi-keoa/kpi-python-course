==============================
Тимченко Аліна Олегівна
==============================


#. Що таке "fork" в термінології Git. Вкажіть принципи роботи з fork'ами. Наведіть команду для створення локальної копії віддаленого
   репозиторію https://github.com/kpi-keoa/kpi-embedded-linux-course
   
  -В термінології Git "fork" - це власне відгалуження проекту.
  Тобто, роблячи "fork", GitHub створить власну копію проекту. 
  Дана копія буде знаходитись у просторі імен власника GitHub акаунту, з якого зроблено форк, і він зможете легко робити зміни шляхом відправки (push) змін. 
  Щоб створити відгалуження проекту, потрібно зайти на сторінку проекту та натиснути кнопку «Fork», яка розташована у правому верхньому кутку.
  Результатом успішного форку є перенаправлення на власну нову проектну сторінку, яка містить копію, в якій тепер є права на запис.
  Далі, скоріш за все, ми захочемо працювати з цим репозиторієм, тому його потрібно зкопіювати на локальний комп'ютер.
  Це робиться командою git clone.
  На прикладі віддаленого репозиторію https://github.com/kpi-keoa/kpi-embedded-linux-course це буде виглялати так: 
  	1. Запускаємо cmd/GitBash у потрібній дерикторії 
  	2. Прописуємо git clone https://github.com/<GitHub username>/kpi-python-course.git
#. Наведіть команди git для додавання файлів та директорій ./dev ./dev/file.c ./.gitignore до локального репозиторію одним комітом
   (уважно).

  -git add ./.
   git commit -m "Changes in files ./dev ./dev/file.c ./.gitignore"


#. Словник (dict). Для чого використовується? Шляхи створення. 
   Як за допомогою ``dict`` зімітувати множину (``set``) та чому *зазвичай* не варто цього робити? Наведіть приклади коду.

  -Словник (dict) є структурою даних (яка ще називається асоціативним масивом), призначеною для зберігання довільних об'єктів з доступом по ключу.
   Дані у словнику зберігаються у форматі ключ – значення. Наприклад:
   d1 = dict(Oleg = "engineer", Andrew = "HR")
   або
   d2 = {"a":"149", "b":"891"}
#. Строкові типи Python. У чому відмінність між Unicode-строкою та байтовою строкою? Наведіть приклад коду, що представляє строку
   ``'вічність'`` у вигляді байтової строки з кодуванням UTF-8 та KOI8-U
  
  -У мові Python підтримуються три типи рядків:
	str – призначені для представлення тексту у форматі Unicode та інших системах кодування. Цей формат містить символи в кодуванні ASCII та символи в інших кодуваннях;
	bytes - призначені для подання двійкових даних;
	bytearray - призначені для подання двійкових даних з урахуванням змін у типі bytes.
	У версії Python 2.6 для представлення Unicode використовується тип unicode.
  Тобто, Unicode-рядок є послідовністю символів, а байтовий рядок - це просто послідовність байтів. Це не читається людиною. 
  Unicode-рядок легко зрозуміти, але він не може бути безпосередньо збережений у комп'ютері, він повинен бути спочатку закодований (перетворений на байтовий рядок)
  Існує кілька кодувань, за допомогою яких символьний рядок може бути перетворений на байтовий рядок.
  Наприклад, щоб закодувати рядок ``'вічність'`` у вигляді байтової строки з кодуванням UTF-8 потрібно написати наступний код:
  'вічність'.encode('utf8')
  Те ж саме для KOI8-U
  'вічність'.encode('koi8-u')


#. Створіть функцію, яка приймає в якості першого аргументу бажаний опір послідовно з'єднаних резисторів *R* [Ом],
   а в якості подальших аргументів – величини резисторів, що є в наявності [Ом].
   Функція повертає кортеж (tuple), першим елементом якого є словник типу ``{номінал: кількість}``, а другим
   елементом – абсолютне відхилення результуючого опору від бажаного [Ом].
#. Що таке she-bang та для чого використовується? Який she-bang буде максимально коректним для Python 3?
   Чи використовується she-bang в скриптах? Якщо так, чому? Якщо ні, коли?

  -she-bang рядок використовується для nix-систем.
  Командні оболонки зчитують початок файлу, що запускається, і визначають як його виконувати.
  Завдяки цьому в Linux, наприклад, можна не викликати інтерпретатор, передаючи йому скрипт "python test.py", а писати просто "./test.py".
  Для Python3 максимально коректний she-bang рядок виглядає таким чином: #!/usr/bin/env python3
  У скриптах she-bang використовується, щоб повідомити операційній системі, який інтерпретатор використовувати для аналізу решти частини файлу.


#. Які цикли Python вам відомі? Яким чином можна зімітувати функціонал циклу do-while з мови С в Python?
  -У Python є два типи циклів: for та while
  Написати цикл з постумовою (do-while) на мові Python можна так:
	while True:
  	 stuff()
  	if fail_condition:
    	 break
  або так:
  	stuff()
	while not fail_condition:
  	stuff()
#. Створити клас. Кожен об'єкт типу класу (instance) містить одне поле ``val``, яке задається при створенні.
   При виведенні об'єкту за допомогою ``print(...)``, формат виводу повинен відповідати *{ClassName}({val})*,
   де *{ClassName}* – ім'я класу, а *{val}* – значення поля ``val``.
