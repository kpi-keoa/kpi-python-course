def Index(index_cod, list_cod, rotor_dict):
    """Данная функция ищет индексы по елементам в словаре. 
    
    Она нужна для более легкого поиска и оброботки значений. 
    
    """
    index_cod = [
        key 
        for el in list_cod 
        for key, value in rotor_dict.items()
        if el == value
    ]
    
    return index_cod


def Rotor_norm(index_cod, sum): 
    """ Функция выступает 3-тим фиксированым ротором."""

    result = [sum - x for x in index_cod]

    return result


def Rotor_in(index_key,index_cod):
    """Начало входа в первую часть роторов(начало шифровки)."""
    result_list = [
        value 
        for _ in range(len(index_cod)) 
        for value in index_key
        ]  
    
    result = [
        x - y 
        for x, y in zip(index_cod, result_list)
        ]

    return result


def Rotor_out(index_key, index_cod, count):
    """Выход и обработки значени(конец шифроки)."""
    result_list = [
        symbol 
        for _ in range(len(index_cod)) 
        for symbol in index_key
        ]   

    result=[x + y for x, y in zip(index_cod, result_list)]

    return result  


def Sum_chek(index_cod):
    """Отдельная функция для проверки диапазона кодируемых индексов."""
    for key in range(len(index_cod)):

        if index_cod[key] < 0:
           index_cod[key] = index_cod[key] + 38

        elif index_cod[key] > 38:
           index_cod[key] = index_cod[key] - 38

    return index_cod


def Coder(index_key, index_cod, count, sum):
    """Функция реализована для упращения работы.
   
    Может виступать как для шифровки так и для дешифровки.

    """
  
    for x in index_key:
        index_cod = Rotor_in(index_key, index_cod)
        index_cod = Sum_chek(index_cod)

    index_cod = Rotor_norm(index_cod, sum)

    for x in index_key:
        index_cod = Rotor_out(index_key, index_cod, count)
        index_cod = Sum_chek(index_cod)
   
    return index_cod


def Unindex(index_cod, list_cod, rotor_dict):
    """Ищет по индексу буквы в словаре и перености их в лист."""

    list_cod = [
        value 
        for el in index_cod
        for key, value in rotor_dict.items()
        if el == key
    ]

    return list_cod


rotor_dict = {
   0:'0',6:'F',12:'L',18:'S',24:'Y',30:'4',36:'_',
   1:'A',7:'G',13:'M',19:'T',25:'Z',31:'5',37:'.',
   2:'B',8:'H',14:'O',20:'U',26:'N',32:'6',38:',',
   3:'C',9:'Q',15:'P',21:'V',27:'1',33:'7',
   4:'D',10:'J',16:'I',22:'W',28:'2',34:'8',
   5:'E',11:'K',17:'R',23:'X',29:'3',35:'9'
    }
# Инициализация словаря для индексации.  
  
string_cod = input("Введите кодируемое слово: ").upper()
string_key = input("Введите слово шифровки: ").upper()
# Ввод кодируемого слова и его ключа.

space = string_cod.split()
string_cod = '_'.join(space)
space = string_key.split()
string_key = '_'.join(space)
# Замена пробелов для возможности их кодировки. 

count = len (string_key)

list_key = list(string_key)
list_cod = list(string_cod)
# Разделение строки посимвольно для дальнешей индексации.

index_cod = []
index_key = []

index_cod = Index(index_cod, list_cod, rotor_dict)
index_key = Index(index_key, list_key, rotor_dict)
# Инициализация поиска индесов.

sum = sum(index_key)
# Сумма ключа нужна для фиксированого ротора.

index_cod = Coder(index_key, index_cod, count,sum)
list_cod = Unindex(index_cod, list_cod, rotor_dict)
string_cod = "".join(list_cod)
print("Результат шифроки: ", string_cod)
# Блок кода отвечает за пoлный процесс шифровки кодруемого слова. 

index_cod = Coder(index_key, index_cod, count,sum)
list_cod = Unindex(index_cod, list_cod, rotor_dict)
string_cod = "".join(list_cod)
print("Результат дешифровки: ", string_cod)
# Аналогичный блок когда, но отвечающий за дешифровку.

