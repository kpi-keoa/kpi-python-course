==================
 KPI-Python-Course
==================

DK-92 Lab2
---------

*Four classes were created. The main class is Human, the class Doctor which is inherited from him, as well as two classes Surgeon and Psychiatrist which are inherited from Doctor.*

*The Human class has a constructor, as well as dunder/magic methods, such as*

1. __init__ method of Human class, also a constructor. Is called when objects are created.
2. __str__ method for the string output of the object itself
3. __repr__ similar method, differing only in output
4. __len__ method that allows you to find the length of the desired string

*I also created an additional file lab2_oop.py, which is designed to test our class as a module instead of a script.*
*To demonstrate the logic of the classes, a function called _func() was created and called through if __name__ == '__main__'*

*Example*:
Output:
    Alexey has been working as a surgeon for 12 years, now his salary is 30000$ a month
    Representation: Human('Alexey', 'Panchenko', '11.07.1984', 30000, 12)
    Length of Alexey is 6
    Alexey is a doctor, he helps people.
    Alexey had a successful surgery.
    Alexey deserve a raise: 3000$
    Alexey, now your current salary is 33000$ a month
