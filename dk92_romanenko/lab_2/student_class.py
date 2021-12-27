class Human():
	def __init__(self, name, surname, age):
		self.name = name
		self.surname = surname
		self.age = age

	def how_old(self):
		print(f"{self.name} is {self.age} years old!")

class Student(Human):
        def __init__(self, name, surname,
                     age, group, deg):
                Human.__init__(self, name, surname, age)
                self.group = group
                self.deg = deg

        def full(self):
                print(f"{self.surname} {self.name}|{self.age}|{self.group}")
                
        def how_old(self):
	        print(f"{self.surname} is {self.age} years old!")



class Faculty(Student):
        def __init__(self, name, surname,
                     age, group, deg, status="В строю"):
                Student.__init__(self, name, surname, age,
                                 group, deg)
                self.status = status

        def change_status(self, status):
                self.status = status

        def print_status(self):
                print(f"{self.surname} {self.status}")

if __name__ == '__main__':
        #Human class demonstration
        y = Human("Anton", "Romanenko", 20)
        y.how_old()

        #Student class demonstration
        st = Student("Anton", "Romanenko", 20, "DK-92", "Bacelor")
        st.full()

        #Faculty class demonstration
        fac = Faculty("Anton", "Romanenko", 20, "DK-92", "Bacelor")
        fac.print_status()
        fac.change_status("Happy!")
        fac.print_status()

        
        
