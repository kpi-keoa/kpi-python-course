#!/usr/bin/env python3

import itertools
import random
from functools import partial
from math import ceil
from pathlib import Path
from transliterate import translit
from yaml import safe_load


LANG='uk'

def translator(value):
    '''Translates the group name and student names into English.'''

    return translit(value, language_code=LANG, reversed=True)


def parse_students(filename, lang=LANG):
    '''
    Opens a yaml file, and writes the group and student names translated
    into English as a dictionary.
    '''
    with open(filename) as f:
        dictionary = safe_load(f)
        dictionary = {translator(key): [(translator(v).replace(' ', '_'), v)
                               for v in values]
               for key, values in dictionary.items()}
        return dictionary


def read_questions(directory):
    '''
    The function reads the questions from the given file, sorts them
    and writes them to a variable of dictionary type.
    '''
    pth = Path(directory)
    dictionary = {}
    for file in sorted(list(pth.glob('*.*'))):
        with open(file) as f:
            qst = f.read().strip().split('\n#')
            qst[1:] = ['#' + q for q in qst[1:]]
            dictionary[file.name] = qst

    return dictionary


def generate_questions(students, questions, *, numeach=2):
    '''
    The function is designed to generate an individual task for each student.
    '''
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
    '''
    The function creates a file separately for each student,
    and this file records previously generated individual questions.
    '''
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
    students = parse_students(student_list)
    qst = read_questions(questions_dir)
    cont = generate_questions(students, qst, numeach=2)
    write_files(out_dir, cont)
