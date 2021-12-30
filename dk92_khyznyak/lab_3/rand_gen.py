#!/usr/bin/env python3

import itertools
import random
from functools import partial
from math import ceil
from pathlib import Path
from transliterate import translit
from yaml import safe_load


LANG='uk'

translit = partial(translit, language_code=LANG, reversed=True)


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def parse_students(filename, lang=LANG):
    """
    This function enters the names of students and groups in a file.
    Arguments:
    filename
    """
    with open(filename) as file:
        dictionary = safe_load(file)
        return {
            translit(group): [(translit(name).replace(' ', '_'), name)
                for name in names]
                    for group, names in dictionary.items()}


def read_questions(directory):
    """
    This feature enters questions in the dictionary and sorts them.
    Arguments:
    directory
    """
    path = Path(directory)
    dictionary = {}
    for file in sorted(list(path.glob('*.*'))):
        with open(file) as f:

            question = f.read().strip().split('\n#')
            question[1:] = ['#' + q for q in question[1:]]
            dictionary[file.name] = question

    return dictionary


def generate_questions(students, questions, *, numeach=2):
    """
    This feature generates questions for each student.
    Arguments:
    students
    questions
    """
    sep = '=' * 30 + '\n'
    files = dict()
    for group, lst in students.items():
        for tr, orig in lst:
            files[f'{group}_{tr}.rst'] = f'{sep}{orig}\n{sep}\n'

    for catname, category in questions.items():
        print(f'{catname:<40}', end='\t')
        personal = list(itertools.combinations(category, numeach))
        print(f'{len(personal)} combinations')
        assert len(personal) >= len(files)
        random.shuffle(personal)
        for f in files:
            files[f] += '\n' + '\n'.join(personal.pop(0)) + '\n'

    return files


def write_files(outdir, files):
    """
    This feature creates a question file for each student.
    Arguments:
    outdir
    files
    """
    odir = Path(outdir)
    odir.mkdir(exist_ok=True)
    for filename, contents in files.items():
        file = odir.joinpath(filename)
        with open(file, 'x') as f:
            f.write(contents)


if __name__ == '__main__':
    from sys import argv
    if len(argv) != 4:
        print(f'Usage\n{argv[0]} student_list questions_dir out_dir')
        exit(-1)
    student_list, questions_dir, out_dir = argv[1:]
    student = parse_students(student_list)
    questions = read_questions(questions_dir)
    cont = generate_questions(student, questions, numeach=2)
    write_files(out_dir, cont)
