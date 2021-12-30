#!/usr/bin/env python3

import itertools
import random
from functools import partial
from pathlib import Path
from transliterate import translit
from yaml import safe_load

LANG = 'uk'

translit = partial(translit, language_code=LANG, reversed=True)


def chunker(seq, size):
    """Single docstring PEP257"""
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def parse_students(filename, lang=LANG):
    with open(filename) as f:
        my_dict = safe_load(f)
        my_dict = {translit(key): [(translit(v).replace(' ', '_'), v)
                               for v in values]
               for key, values in my_dict.items()}
        return my_dict


def read_questions(directory):
    """
    Multi-line doc PEP 257
    """
    pth = Path(directory)
    my_dict = {}
    for file in sorted(list(pth.glob('*.*'))):
        with open(file) as f:
            question = f.read().strip().split('\n#')
            question[1:] = ['#' + q for q in question[1:]]
            my_dict[file.name] = question

    return my_dict


def generate_questions(students, questions, *, numeach=2):
    sep = '=' * 30 + '\n'
    files = dict()
    for group, lst in students.items():
        for tr, orig in lst:
            files[f'{group}_{tr}.rst'] = f'{sep}{orig}\n{sep}\n'

    for catname, category in questions.items():
        print(f'{catname:<40}', end='\t')
        # copy = list(category)
        # sel = choices(copy, k=numeach * len(files))
        # personal = ['\n'.join(q) + '\n' for q in chunker(sel, numeach)]
        personal = list(itertools.combinations(category, numeach))
        print(f'{len(personal)} combinations')
        assert len(personal) >= len(files)
        random.shuffle(personal)
        for f in files:
            files[f] += '\n' + '\n'.join(personal.pop(0)) + '\n'

    return files


def write_files(outdir, files):
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
        exit(1)
    student_list, questions_dir, out_dir = argv[1:]
    st = parse_students(student_list)
    q = read_questions(questions_dir)
    cont = generate_questions(st, q, numeach=2)
    write_files(out_dir, cont)
