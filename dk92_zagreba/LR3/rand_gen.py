#!/usr/bin/env python3
import itertools
import random
from pathlib import Path
from transliterate import translit
from yaml import safe_load

QUESTIONS_SET_SEPARATOR = "=" * 30 + "\n"
# Made to global variables for declaration only once, not many


def translate_on_english(value):
    return translit(value, language_code="uk", reversed=True)


# partial replacement is more readable, does the same


def parse_students(filename):
    with open(filename) as file:
        student_names_by_group: dict = safe_load(file)
        return {
            translate_on_english(group_of_name): [
                (translate_on_english(student_name).replace(" ", "_"), student_name)
                for student_name in student_names
            ]
            for group_of_name, student_names in student_names_by_group.items()
        }


# rewritten for a better understanding of what is written


def read_questions(questions_dir):
    questions_dir_path = Path(questions_dir)
    questions_by_filename = {}
    for file in questions_dir_path.glob("*.*"):
        with open(file) as f:
            questions = f.read().split("\n")
            questions_by_filename[file.name] = questions

    return questions_by_filename


# removed # and added again (doesn't make sense)


def generate_questions_sets(students, questions, numeach=2):
    files = {
        f"{group_of_name}_{translate_name}.rst": f"{QUESTIONS_SET_SEPARATOR}{origin_name}\n{QUESTIONS_SET_SEPARATOR}\n"
        for group_of_name, student_names in students.items()
        for translate_name, origin_name in student_names
    }
    # More optimized file creation
    for category_name, category in questions.items():
        print(f"{category_name:<40}", end="\t")
        personal = list(itertools.combinations(category, numeach))
        print(f"{len(personal)} combinations")
        assert (
            len(personal) >= len(files),
            "Please add more categories and questions to prevent questions set redunate!",
            # error message, to better understand what is wrong
        )
        random.shuffle(personal)
        for filename in files:
            files[filename] += "\n" + "\n\n".join(personal.pop(0)) + "\n"

    return files


def write_questions_sets(outdir, question_sets):
    odir = Path(outdir)
    odir.mkdir(exist_ok=True)
    for filename, contents in question_sets.items():
        file = odir.joinpath(filename)
        with open(file, "x") as f:
            f.write(contents)


# only changed names in the name of readability

if __name__ == "__main__":
    from sys import argv

    if len(argv) != 4:
        print(f"Usage\n{argv[0]} student_list questions_dir out_dir")
        exit(-1)
    student_list, questions_dir, out_dir = argv[1:]
    student = parse_students("student_list.yaml")
    q = read_questions("questions_dir")
    cont = generate_questions_sets(student, q, numeach=2)
    write_questions_sets(out_dir, cont)
