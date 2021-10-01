# List of students and their scores
students = {"Zhenya": 15, "Vitya": 45, "Misha": 23}

# Map names to Ukrainian
LOCAL_NAMES = {"Zhenya": "Женя", "Vitya": "Вітя", "Misha": "Міша"}


def local_name(name):
    return LOCAL_NAMES.get(name, name)


def retreive(name):
    """Finds student's score by the name."""
    print(f"{local_name(name)}: {students[name]}/100")


def assign(name, count):
    """Sets a new student's score."""
    count = int(count)
    students[name] = count
    retreive(name)


def add(name, count):
    """Adds a certain number of points to the rating."""
    count = int(count)
    students[name] += count
    retreive(name)
