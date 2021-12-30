#!/usr/bin/env python3

import itertools
import random
from functools import partial
from pathlib import Path

from transliterate import translit
from yaml import safe_load

SEP = "=" * 30 + "\n"
LANG="uk"

def translate(value):
    return translit(value, language_code=LANG, reversed=True)


def chunker(seq, size):
    return (seq[pos : pos + size] for pos in range(0, len(seq), size))


def parse_students(filename):
    with open(filename) as infile:
        students_names_dict = safe_load(infile)
        students_names_dict = {
            translate(key): [(translate(value).replace(" ", "_"), value) for value in values]
            for key, values in students_names_dict.items()
        }
        return students_names_dict


def read_questions(directory):
    questions_dir = Path(directory)
    questions_dict = {}
    for file in sorted(list(questions_dir.glob("*.*"))):
        with open(file) as infile:
            questions = infile.read().strip().split("\n#")
            questions[1:] = ["#" + question for question in questions[1:]]
            questions_dict[file.name] = questions

    return questions_dict


def generate_questions(students, questions, *, num_each=2):
    files = dict()
    for group, lst in students.items():
        for transliterate, original in lst:
            files[f"{group}_{transliterate}.rst"] = f"{SEP}{original}\n{SEP}\n"

    for category_name, category in questions.items():
        print(f"{category_name:<40}", end="\t")
        personal = list(itertools.combinations(category, num_each))
        print(f"{len(personal)} combinations")
        assert len(personal) >= len(files)
        random.shuffle(personal)
        for file in files:
            files[file] += "\n" + "\n".join(personal.pop(0)) + "\n"

    return files


def write_files(output_directory, files):
    output = Path(output_directory)
    output.mkdir(exist_ok=True)
    for filename, contents in files.items():
        file = output.joinpath(filename)
        with open(file, "x") as outfile:
            outfile.write(contents)


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
