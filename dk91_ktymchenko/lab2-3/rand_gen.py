#!/usr/bin/env python3

import itertools
import random
from functools import partial
from pathlib import Path
from transliterate import translit
from yaml import safe_load

SEP = "=" * 30 + "\n"
LANG = "uk"

translit = partial(translit, language_code=LANG, reversed=True)


def chunker(seq, size):
    return (seq[pos : pos + size] for pos in range(0, len(seq), size))


def parseStudents(filename, lang=LANG):
    with open(filename) as file:
        studNameDict = safeLoad(file)
        studNameDict = {
            translit(key): [(translit(value).replace(" ", "_"), v) for v in values]
            for key, values in studNameDict.items()
        }
        return studNameDict


def readQuestions(directory):
    path = Path(directory)
    questionsDict = {}
    for file in sorted(list(path.glob("*.*"))):
        with open(file) as file:
            questions = file.read().strip().split("\n#")
            questions[1:] = ["#" + question for question in questions[1:]]
            questionsDict[file.name] = questions

    return questionsDict


def generateQuestions(students, questions, *, num_each=2):
    files = dict()
    for group, lst in students.items():
        for transliterate, original in lst:
            files[f"{group}_{transliterate}.rst"] = f"{SEP}{original}\n{SEP}\n"

    for categoryName, category in questions.items():
        print(f"{categoryName:<40}", end="\t")
        personal = list(itertools.combinations(category, numEach))
        print(f"{len(personal)} combinations")
        assert len(personal) >= len(files)
        random.shuffle(personal)
        for f in files:
            files[f] += "\n" + "\n".join(personal.pop(0)) + "\n"

    return files


def write_files(outputDir, files):
    outDir = Path(outputDir)
    outDir.mkdir(existOk=True)
    for filename, contents in files.items():
        file = outDir.joinpath(filename)
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
    write_files(output, cont)
