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
    '''Translates the name of the group and the names of the students into English.'''
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def parse_students(filename, lang=LANG):
    '''Opens the yaml file and writes down the translated group and student names in English as a dictionary.'''
    with open(filename) as f:
        wordbook = safe_load(f)
        wordbook = {translit(key): [(translit(v).replace(' ', '_'), v)
                               for v in values]
               for key, values in wordbook.items()}
        return wordbook


def read_questions(directory):
    '''The function reads questions from the specified file, sorts them and writes them to a dictionary type variable.
    '''
    trail = Path(directory)
    wordbook = {}
    for file in sorted(list(trail.glob('*.*'))):
        with open(file) as f:
            quiz = f.read().strip().split('\n#')
            quiz[1:] = ['#' + q for q in quiz[1:]]
            wordbook[file.name] = quiz

    return wordbook


def generate_questions(students, questions, *, numeach=2):
    '''The function is intended for the formation of an individual task for each student.'''
    sep = '=' * 30 + '\n'
    files = dict()
    for group, lst in students.items():
        for tr, orig in lst:
            files[f'{group}_{tr}.rst'] = f'{sep}{orig}\n{sep}\n'

    for student, category in questions.items():
        print(f'{student:<40}', end='\t')
        personal = list(itertools.combinations(category, numeach))
        print(f'{len(personal)} combinations')
        assert len(personal) >= len(files)
        random.shuffle(personal)
        for f in files:
            files[f] += '\n' + '\n'.join(personal.pop(0)) + '\n'

    return files


def write_files(outdir, files):
    '''This feature creates a file separately for each student,
      and this file records previously generated individual questions.'''
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
