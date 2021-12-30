class Human():
    """Human class."""

    default_name = 'None'
    default_surname = 'None'
    default_birthday = 'xx.xx.xxxx'
    default_salary = 0
    default_wexp = 0

    def __init__(
        self, name=default_name, surname=default_surname,
        birthday=default_birthday, salary=default_salary, wexp=default_wexp):
        """

        Human class constructor.

        Args:
            name(str): variable refers to human name
            surname(str): variable refers to human surname
            birthday(str): variable refers to human date of birth
            salary(int): variable refers to human salary
            wexp(int): variable refers to human work experience

        """
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.salary = salary
        self.wexp = wexp

    def __str__(self):
        """

        A method of the Human class responsible for the string representation of the object.

        Returns:
            f-string of Human information

        """
        return (f'Name: {self.name}, Surname: {self.surname}, Birthday: {self.birthday},'
                f'Salary: {self.salary}, Work Experience: {self.wexp}'
                )

    def __repr__(self):
        """

        A method of the Human class responsible for the string representation of the object.

        Returns:
            F-string of Human information

        """
        return f'Human{self.name, self.surname, self.birthday, self.salary, self.wexp}'

    def __len__(self):
        """

        A method of the Human class responsible for to find the length of the name.

        Returns:
            Lenght of Human name

        """
        return len(self.name)

    def add_salary(self, amount):
        """

        A method of the Human class responsible for salary increases.

        Args:
            amount(int): amount of money that you increase

        Returns:
            Human salary

        """
        print(f'{self.name} deserve a raise: {amount}$')
        self.salary = self.salary + amount
        return self.salary

    def current_salary(self):
        """

        A method of the Human class responsible for return string with current salary.

        Returns:
            F-string with current salary

        """
        return f'{self.name}, now your current salary is {self.salary}$ a month'


class Doctor(Human):
    """class Doctor."""

    def work_as_doctor(self):
        """

        A method of the Doctor class responsible for return string with information.

        Returns:
            F-string with information about Doctor

        """
        return f'{self.name} is a doctor, he helps people.'


class Surgeon(Doctor):
    """class Surgeon."""

    def __str__(self):
        """

        A method of the Surgeon class responsible for return string with information.

        Returns:
            F-string with information about Surgeon

        """
        return (f'{self.name} has been working as a surgeon for {self.wexp} years,'
                f'now his salary is {self.salary}$ a month')

    def works_as_surgeon(self):
        """

        A method of the Surgeon class responsible for return string with information.

        Returns:
            F-string with information of successful surgery

        """
        return f'{self.name} had a successful surgery.'


class Psychiatrist(Doctor):
    """class Psychiatrist."""

    def __str__(self):
        """

        A method of the Psychiatrist class responsible for return string with information.

        Returns:
            F-string with information about Psychiatrist

        """
        return (f'{self.name} has been working as a psychiatrist for {self.wexp} years,'
                f'now his salary is {self.salary}$ a month')

    def works_as_psh(self):
        """

        A method of the Surgeon class responsible for return string with information.

        Returns:
            F-string with information of great session

        """
        return f'{self.name} had a great session'


def _func():
    first_human = Surgeon('Alexey', 'Panchenko', '11.07.1984', 30000, 12)
    print(first_human)
    print(repr(first_human))
    print(len(first_human))
    print(first_human.work_as_doctor())
    print(first_human.works_as_surgeon())
    first_human.add_salary(3000)
    print(first_human.current_salary())


if __name__ == '__main__':
    _func()
