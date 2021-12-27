class Human():
	def __init__(self, name, surname, age):
		self.name = name
		self.surname = surname
		self.age = age
    
    def wiyn(self):
        print(f"{self.name} {self.surname}")


	def how_old(self):
	    print(f"{self.age} years old!")

class Student(Human):
    def __init__(self, name, surname, age, group, deg):
        Human.__init__(self, name, surname, age)
        self.group = group
        self.deg = deg

    def info(self):
        print(f"{self.surname} {self.name} {self.age} {self.group}")
                

class Teacher(Human):
    def: __init__(self, name, surname, age, academic_title):
        Human.__init__(self, name, surname, age)
        self.academic_title = academic_title
    def info(self):
        print(f"{self.surname} {self.name} {self.age} {self.academic_title}")   




if __name__ == '__main__':
    h = Human("Makhno", "Viktor", 19)
    h.wiyn()
    h.how_old()

    st = Student("Makhno", "Victor", 19, "DK-91", "Bacelor")
    st.info()

    teach = Teacher("John", "Doe", 35, "Professor")
    teach.info()


