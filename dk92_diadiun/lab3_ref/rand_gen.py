#!/usr/bin/env python3

import itertools
import random
from functools import partial
from math import ceil
from pathlib import Path
from transliterate import translit
from yaml import safe_load


LANG = 'uk'

translit = partial(translit, language_code=LANG, reversed=True)


def parse_students(filename, lang=LANG):
    """

    The function opens the file and reads the names into the dictionary. 

    Function arguments:
    - file path to read

    Returns
    - dictionary with students' names

    """
    with open(filename) as f:
        dct = safe_load(f)
        dct = {translit(key): [(translit(v).replace(' ', '_'), v)
                               for v in values]
               for key, values in dct.items()}
        return dct


def read_questions(directory):
    """

    Function that reads questions from a file, sorts them, and writes them into a dictionary.

    Args:
        - Directory where the questions are located

    Returns:
        - Questions dictionary

    """
    pth = Path(directory)
    dct = {}
    for file in sorted(list(pth.glob('*.*'))):
        with open(file) as f:
            qst = f.read().strip().split('\n#')
            qst[1:] = ['#' + q for q in qst[1:]]
            dct[file.name] = qst

    return dct


def generate_questions(students, questions, *, numeach=2):
    """

     Function that generates questions for each individual student.

    Function arguments:
        Group and name dictionary
        Questions dictionary

    Returns:
        Dictionary of students and questions

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

    Function writes data to a file.

    Function arguments:
    - Path to the file for recording
    - Input data

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
    st = parse_students(student_list)
    q = read_questions(questions_dir)
    cont = generate_questions(st, q, numeach=2)
    write_files(out_dir, cont)
