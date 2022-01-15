#!/usr/bin/env python3

import itertools
import random

from pathlib import Path
from yaml import safe_load
from functools import partial
from transliterate import translit

LANG = 'uk'

def translt(text, lang=LANG):
    '''Transliterate word into latin alphabet.
    
    Args:
        text (str): transliterated text  
    
    Return:
        result translit func
    '''

    return translit(text, language_code='uk', reversed=True)


def parse_students(filename):
    """Read yaml file with students names
       and creating dict with students fullnames

    Args:
        filename (str): path to yaml file
        lang (str):  Defaults to LANG.

    Returns:
        dct (dict): student's dict
    """
    with open(filename) as f:
        dct = safe_load(f)
        dct = {translt(key): [(translt(v).replace(' ', '_'), v)
                           for v in values]
               for key, values in dct.items()}
        return dct


def read_questions(directory):
    """Read in directory all questions files

    Args:
        directory (str): path to questions files

    Returns:
        dct (dict): dict of questions
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
    """Generate dict

    Args:
        students (dict): students dict
        questions (dict): qustions dict
        numeach (int): int parameter to set number of questions
                       for each student

    Returns:
        files (dict): dict with questions
    """
    sep = '=' * 30 + '\n'
    files = {}
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
    """Write in outdir files

    Args:
        outdir (str): path to out dictorie
        files (dict): dict of questions for 
                      each student

    Return:
        void
    """
    odir = Path(outdir)
    odir.mkdir(exist_ok=True)
    for filename, contents in files.items():
        file = odir.joinpath(filename)
        with open(file, 'x') as f:
            f.write(contents)
        

if __name__ == '__main__':
    import argparse as arg

    aparse = arg.ArgumentParser(description='Question generator')

    aparse.add_argument('student_list', type=str, 
                    help='Student list in yaml format')
    aparse.add_argument('questions_dir', type=str,
                    help='Question list')
    aparse.add_argument('out_dir', type=str,
                    help='Output directory for generated list')

    args = aparse.parse_args()

    student_list = args.student_list
    questions_dir = args.questions_dir
    out_dir = args.out_dir

    st = parse_students(student_list)
    q = read_questions(questions_dir)
    cont = generate_questions(st, q, numeach=2)

    write_files(out_dir, cont)
