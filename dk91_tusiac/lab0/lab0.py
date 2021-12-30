
 #Список студентів та їх бали 

 
student = {'Женя': 15,
           'Вітя': 45,
           'Міша': 23
           }


        #Знаходить бал студента за його ім'ям
def find(name):  
    print(student[name],'- балів зі 100')


        #Встановлює новий бал студенту
def set(name, count):  
    count = int(count)
    print(student[name], '=>', count)
    student[name] = count


        #Додає певну кількість балів до рейтингу
def add(name, count):  
    count = int(count)
    print(student[name], '+', count,'=', student[name]+count)
    student[name] += count

