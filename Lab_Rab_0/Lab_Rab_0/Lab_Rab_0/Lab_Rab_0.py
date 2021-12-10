def Index(Index_cod,List_cod,Rotor_Dict):
    Index_cod = [
        key 
        for el in List_cod 
        for key, value in Rotor_Dict.items()
        if el == value
]
    return Index_cod
def Rotor_norm(Index_cod,sum): 
    result=[sum-x for x in Index_cod]
    return result
def Rotor_in(Index_key,Index_cod):
    result_list = [
        value 
        for _ in range(len(Index_cod)) 
        for value in Index_key
        ]                                                                                                                                            
    result=[
        x-y 
        for x, y in zip(Index_cod, result_list)
        ]

    return result
def Rotor_out(Index_key,Index_cod,count):
    result_list = [
        symbol 
        for _ in range(len(Index_cod)) 
        for symbol in Index_key
        ]   
    result=[x+y for x, y in zip(Index_cod, result_list)]

    return result  
def Sum_chek(Index_cod):
    for key in range(len(Index_cod)):
        if Index_cod[key] < 0:
           Index_cod[key]=Index_cod[key]+38
        elif Index_cod[key]>38:
           Index_cod[key]=Index_cod[key]-38





      
   # (Index_cod[i] < 0  for i in range(len(Index_cod)))
    #(Index_cod[i] > 36 for i in range(len(Index_cod)))
    return Index_cod
def Coder(Index_key,Index_cod,count,sum):
  
  
    for x in Index_key:
        Index_cod = Rotor_in(Index_key,Index_cod)
        Index_cod = Sum_chek(Index_cod)

    Index_cod = Rotor_norm(Index_cod,sum)

    for x in Index_key:
        Index_cod = Rotor_out(Index_key,Index_cod,count)
        Index_cod = Sum_chek(Index_cod)
   
    return Index_cod
def Unindex(Index_cod,List_cod,Rotor_Dict):
    List_cod = [
        value 
        for el in Index_cod
        for key, value in Rotor_Dict.items()
        if el == key
]
    return List_cod


Rotor_Dict = {
   0:'0',6:'F',12:'L',18:'S',24:'Y',30:'4',36:'_',
   1:'A',7:'G',13:'M',19:'T',25:'Z',31:'5',37:'.',
   2:'B',8:'H',14:'O',20:'U',26:'N',32:'6',38:',',
   3:'C',9:'Q',15:'P',21:'V',27:'1',33:'7',
   4:'D',10:'J',16:'I',22:'W',28:'2',34:'8',
   5:'E',11:'K',17:'R',23:'X',29:'3',35:'9'
    }

String_cod = input("Введите кодируемое слово: ").upper()
String_key = input("Введите слово шифровки: ").upper()

l = String_cod.split()
String_cod = '_'.join(l)
l = String_key.split()
String_key = '_'.join(l)

count =len (String_key)

List_key = list(String_key)
List_cod = list(String_cod)

Index_cod = []
Index_key = []

Index_cod = Index(Index_cod,List_cod,Rotor_Dict)
Index_key = Index(Index_key,List_key,Rotor_Dict)

Sum = sum(Index_key)

Index_cod = Coder(Index_key,Index_cod,count,Sum)
List_cod = Unindex(Index_cod,List_cod,Rotor_Dict)
String_cod = "".join(List_cod)
print("Результат шифроки: ",String_cod)

Index_cod = Coder(Index_key,Index_cod,count,Sum)
List_cod =Unindex(Index_cod,List_cod,Rotor_Dict)
String_cod = "".join(List_cod)
print("Результат дешифровки: ",String_cod)

