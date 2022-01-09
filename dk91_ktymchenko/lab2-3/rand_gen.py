#!/usr/bin/env python3

import itertools
import random
from functools import partial
from pathlib import Path
from transliterate import translit
from yaml import safe_load

SEP = "=" * 30 + "\n"
LANG = "uk"

def translate(value):
    return translit(value, language_code=LANG, reversed=True)

def chunker(seq, size):
    return (seq[pos : pos + size] for pos in range(0, len(seq), size))


def parse_students(filename, lang=LANG):
    with open(filename) as file:
        stud_name_dict = safe_load(file)
        stud_name_dict = {
            translit(key): [(translit(value).replace(" ", "_"), value) for value in values]
            for key, values in stud_name_dict.items()
        }
        return stud_name_dict


def read_questions(directory):
    path = Path(directory)
    questions_dict = {}
    for file in sorted(list(path.glob("*.*"))):
        with open(file) as input_file:
            questions = input_file.read().strip().split("\n#")
            questions[1:] = ["#" + question for question in questions[1:]]
            questions_dict[file.name] = questions

    return questions_dict


def generate_questions(students, questions, *, num_each=2):
    files = dict()
    for group, lst in students.items():
        for trnslt, origin in lst:
            files[f"{group}_{trnslt}.rst"] = f"{SEP}{origin}\n{SEP}\n"

    for category_name, category in questions.items():
        print(f"{category_name:<40}", end="\t")
        personal = list(itertools.combinations(category, num_each))
        print(f"{len(personal)} combinations")
        assert len(personal) >= len(files)
        random.shuffle(personal)
        for file in files:
            files[file] += "\n" + "\n".join(personal.pop(0)) + "\n"

    return files


def write_files(output_dir, files):
    out_dir = Path(output_dir)
    out_dir.mkdir(exist_ok=True)
    for filename, contents in files.items():
        file = out_dir.joinpath(filename)
        with open(file, "x") as out:
            out.write(contents)


if __name__ == "__main__":
    from sys import argv

    if len(argv) != 4:
        print(f"Usage\n{argv[0]} student_list questions_dir out_dir")
        exit(-1)
    student_list, questions_dir, out_dir = argv[1:]
    students_dict = parse_students(student_list)
    questions_dict = read_questions(questions_dir)
    cont = generate_questions(students_dict, questions_dict, num_each=2)
    write_files(out_dir, cont)
