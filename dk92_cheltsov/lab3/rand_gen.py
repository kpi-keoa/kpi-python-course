"""Module to generate random questions combinations for students"""

import itertools
import random
from functools import partial
from pathlib import Path
from transliterate import translit
from yaml import safe_load

LANG = "uk"
translit_func = partial(translit, language_code=LANG, reversed=True)


def parse_students(filename: str):
    """Read the file with some students list.

    Students file should be in format yaml
    Example:
        Group_name:
            - Student1 Name
            - Student2 Name
    """
    with open(filename) as input_file:
        students_names_dict = safe_load(input_file)
        students_names_dict = {
            translit_func(key): [
                (translit_func(value).replace(" ", "_"),
                 value) for value in values
            ]
            for key, values in students_names_dict.items()
        }
        return students_names_dict


def read_questions(directory: str, suffix: str = "*") -> dict:
    """Collect all files in input directory.
    Parse collected files to the questions dict object.
    Kwargs:
    suffix -- the extension of files, which you want to parse
    (default * - all files extension)

    WARNING: function can parse all files in the following directory.
    Before usage be sure, that there are no accidental files.
    For parsing -- data in files should be in the following format:
    #Question1
    #Question2
    """
    pth = Path(directory)
    ready_questions_dict = {}
    for file in sorted(list(pth.glob(f"*.{suffix}"))):
        with open(file) as input_file:
            try:
                questions = input_file.read().strip().split("\n#")
                questions[1:] = ["#" + question for question in questions[1:]]
                ready_questions_dict[file.name] = questions
            except UnicodeDecodeError:
                print(f"INFO: Skipping file {file.name} due to error.")
                continue
    return ready_questions_dict


def generate_questions(
        students: dict, questions: dict, num_each: int = 2) -> dict:
    """Randomly generates questions for students

    input:
    students -- dict with students
    questions -- dict with available questions
    num_each -- int parameter to set number of questions,
     that one user gets (default 2)

    """
    sep = "=" * 30 + "\n"
    files = dict()
    for group, lst in students.items():
        for transliteration, original in lst:
            files[f"{group}_{transliteration}.rst"] = f"{sep}{original}\n{sep}\n"

    for filename, category in questions.items():
        print(f"{filename:<40}", end="\t")
        personal = list(itertools.combinations(category, num_each))
        print(f"{len(personal)} combinations")
        assert len(personal) >= len(files)
        random.shuffle(personal)
        for file in files:
            files[file] += "\n" + "\n".join(personal.pop(0)) + "\n"

    return files


def create_files(output_dir: str, files: dict) -> None:
    """Create output directory.
    Write files in .rst extension with questions for students into it.
    (Only if files doesn't exist.)

    input:
     output_dir -- directory, where to create files
     files -- dictionary with info for files. (Questions and students)

    """
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    for filename, contents in files.items():
        file = output_path.joinpath(filename)
        with open(file, "x") as output_file:
            output_file.write(contents)


if __name__ == "__main__":
    from sys import argv

    if len(argv) != 4:
        print(f"Usage\n{argv[0]} student_list questions_dir out_dir")
        exit(-1)
    students_file, questions_dir, output_dir_path = argv[1:]
    students_dict = parse_students(students_file)
    questions_dict = read_questions(questions_dir)
    try:
        cont = generate_questions(students_dict, questions_dict, num_each=2)
        create_files(output_dir_path, cont)
    except AssertionError:
        print("ERROR: Amount of students more that amount of possible combinations!")  # noqa: E501
    except FileExistsError:
        print("ERROR: Files are already created in the output directory")  # noqa: E501
