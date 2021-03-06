==============================
Широков Владислав Вікторович
==============================


#. Що таке "fork" в термінології Git. Вкажіть принципи роботи з fork'ами. Наведіть команду для створення локальної копії віддаленого
   репозиторію https://github.com/kpi-keoa/kpi-embedded-linux-course

- Fork, грубо говоря, копия репозитория.
Fork нужен для тех же целей, что и branch в Git. С помощью него создается точная копия оригинального репозитория, только на сервисе GitHub. В копии репозитория можно вносить свои собственные изменения, редактировать файлы или удалять директории.
Как только все изменения будут внесены, то можно поделиться ими - отправить авторам оригинального репозитория запрос на слияние вашего измененного репозитория с их оригинальным репозиторием. Такой запрос называется pull request.
Command: git clone https://github.com/kpi-keoa/kpi-embedded-linux-course

#. Як підтягнути зміни, що відбулись у віддаленому upstream-репозиторії (гілка master) до локального репозиторію? Наведіть команду.

- git marge upstream/master 
  git checkout master 
  git checkout -b branch name
  git add -A git commit -m "my" 
  git push origin branch name

#. Перерахуйте та коротко окресліть відомі вам **базові** типи даних Python.

- Numbers (числа). Числа в языке Python представлены тремя встроенными типами: целые ( int ), вещественные ( float ) и комплексные ( comlex ), а так же двумя типами чисел, которые предоставляет его стандартная библиотека: десятичные дроби неограниченной точности ( Decimal ) и обыкновенные дроби ( Float ).
	Strings (строки). Строка в Python – это последовательный набор символов, который может состоять как из цифр, так и из букв, и разделителей.
	Lists (списки). Списки в Python - упорядоченные изменяемые коллекции объектов произвольных типов (почти как массив, но типы могут отличаться). Список может содержать любое количество любых объектов (в том числе и вложенные списки), или не содержать ничего.
	Dictionaries (словари). Словари в Python - неупорядоченные коллекции произвольных объектов с доступом по ключу. Их иногда ещё называют ассоциативными массивами или хеш-таблицами. 
	Tuples (кортежи). Кортежи в Python – это те же списки за одним исключением. Кортежи неизменяемые структуры данных. Так же как списки они могут состоять из элементов разных типов, перечисленных через запятую. 
	Sets (множества). Множество в языке Python — это структура данных, эквивалентная множествам в математике. Множество может состоять из различных элементов, порядок элементов в множестве неопределен. Это позволяет выполнять операции типа “проверить принадлежность элемента множеству” быстрее, чем просто перебирая все элементы множества.
	Boolean (логический тип данных). В Python, как и в других языках, есть логический тип переменных bool, который имеет всего два значения: True (истина) и False (ложь). Его возвращают логические операторы (например сравнение чисел или проверка присутствия элемента в списке), и именно этот тип обычно используется в if и while.

#. Якому емодзі відповідає байтова строка ``b'\xff\xfe=\xd8\r\xdc'`` (UTF-16)? Що значить даний запис байтової строки?
   Наведіть приклад коду, що перекодує дану строку в UTF-8 та вкажіть результат у вигляді коментаря

#. Аргументи функцій. Які типи (концептуально) аргументів бувають? Наведіть приклад функції, яка виводить свої аргументи.

-При вызове функции аргументы можно передавать двумя способами:
	1) как позиционные - передаются в том же порядке, в котором они определены при создании функции. То есть, порядок передачи аргументов определяет, какое значение получит каждый аргумент. Позиционные аргументы при вызове функции надо передать в правильном порядке
	2) как ключевые - передаются с указанием имени аргумента и его значения. В таком случае, аргументы могут быть указаны в любом порядке, так как их имя указывается явно.

#. Аргументи функцій. Яким чином задати значення аргументу за замовчуванням, якщо таким аргументом є порожній список? Коли це не спрацює?
   Наведіть приклад (пов'язаний з галуззю електроніки, наприклад, розрахунок за формулою).

#. Конструкція умовного виконання Python. Яким чином можна реалізувати приорітетну логіку перевірок з її допомогою?
   Наведіть приклад коду, де спочатку перевіряється виконання логічного виразу *A та B*, далі виразу *лише A*.
   Якщо виконується перша умова *A та B*, вивести "ONE"; якщо наступна *лише А*, вивести "TWO"; якщо жодна з умов, вивести "FAIL".
#. Які цикли Python вам відомі? Яким чином можна зімітувати функціонал циклу do-while з мови С в Python?

- For - Этот цикл проходится по любому итерируемому объекту (например строке или списку), и во время каждого прохода выполняет тело цикла.
While - Цикл while будет запускать фрагмент кода, пока условие истинно. 

Do while Уникальность циклов do while заключается в том, что код в блоке цикла будет выполнен хотя бы один раз.
Код в операторе выполняется один раз, а затем условие проверяется только после выполнения кода.
Таким образом, код сначала запускается один раз, а затем проверяется условие. Если проверяемое условие истинно, цикл продолжается.
Password = "python"
counter = 0

while True:
    word = input ("Enter the password: ").lower()
    counter = counter + 1
    if word == password:
        break
    if word != password and counter > 7: 
        break

