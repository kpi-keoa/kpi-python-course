import lab2

def _func():
    second_human = lab2.Psychiatrist('Vasiliy', 'Lomachenko', '03.09.1991', 20000, 5)
    print(second_human)
    print(repr(second_human))
    print(len(second_human))
    print(second_human.work_as_doctor())
    print(second_human.works_as_psh())
    second_human.add_salary(1500)
    print(second_human.current_salary())

_func()
