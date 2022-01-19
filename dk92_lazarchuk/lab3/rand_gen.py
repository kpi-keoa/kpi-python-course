#!/usr/bin/env python3

import itertools
import random
from functools import partial
from pathlib import Path
from transliterate import translit
from yaml import safe_load


LANG='uk'


def parse_students(filename, lang=LANG):
    '''
    Read yaml file with students names
        inputs:
            filename - path to yaml file
        return:
            dict example [[group_name1, [student1,...., studentn]],....,[group_namen, [student1,...., studentn]]]
    '''
    translit = partial(translit, language_code=lang, reversed=True)
    with open(filename) as f:
        dct = safe_load(f)
        dct = {translit(key): [(translit(v).replace(' ', '_'), v)
                               for v in values]
               for key, values in dct.items()}
        return dct


def read_questions(directory):
    '''
    Read in directory all questions files
        inputs:
            directory - path to questions files
        return:
            dict example [[filename, [quest1,...., questn]],....,[filename, [quest1,...., questn]]]
    '''
    pth = Path(directory)
    dct = {}
    for file in sorted(list(pth.glob('*.*'))):
        with open(file) as f:
            qst = f.read().strip().split('\n#')
            qst[1:] = ['#' + q for q in qst[1:]]
            dct[file.name] = qst

    return dct


def generate_questions(students, questions, *, numeach=2):
    '''
    Generate dict 
        inputs:
            students - dict example [[group_name1, [student1,...., studentn]],....,[group_namen, [student1,...., studentn]]]
            questions - dict example [[filename, [quest1,...., questn]],....,[filename, [quest1,...., questn]]]
            numeach -- int parameter to set number of questions
        return:
            dict example [[filename, content_to_write],....,[filename, content_to_write]]
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
    Write in outdir files
        inputs:
            outdir - path to out dictorie
            files - dict example [[filename, content_to_write],....,[filename, content_to_write]]
        return: none
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
    st = parse_students(student_list)
    q = read_questions(questions_dir)
    cont = generate_questions(st, q, numeach=2)
    write_files(out_dir, cont)
