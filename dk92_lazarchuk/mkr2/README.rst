#. Написать код, реализующий бросок кубика в ООП-стиле.
   
   Создать класс, реализующий игральный кубик.
   
   При создании объекта задается количество граней, а если оно не указано – используется стандартное,
   заданное *на уровне класса* (для данного класса – 6).
   Класс имеет методы:
     - ``roll`` – кидает кубик. При этом задает значение, как выпал кубик. И возвращает это же значение.
       Предусмотреть, что после броска кубик нельзя снова бросить, если при инициализации
       параметр ``is_rerollable`` (по умолчанию False) не задан в True.
     - ``handout`` – ``classmethod``, создающий по M кубиков для N игроков
     - Специальные (dunder-) методы для сравнения двух кубиков. Сравнивать можно только те кубики, которые
       уже были брошены.
     - Специальные (dunder-) методы для красивого вывода выпавшего значения кубика. Предусмотреть,
       что кубик на момент вывода может быть еще не брошен.
   
   Создать ряд стандартных классов для игральных кубиков с 11 и 15 гранями, которые наследуются от
   предыдущего класса.
   
   Отдельно описать логику, где несколько игроков могут играть вместе, бросая кубики.
   
   В блоке ``if __name__ == '__main__':`` коротко продемонстрировать использование.
   
   Все должно задокументировано согласно PEP257.
   Код должен соответствовать стилю PEP8. Wemake-Python-Styleguide, при запуске flake8
   не должен выводить *ни одной* ошибки.