#!/usr/bin/env python3

from itertools import combinations
from random import shuffle
from functools import partial
from pathlib import Path
from transliterate import translit
from yaml import safe_load as upload_students

sep = '=' * 30 + '\n'
translit = partial(translit, language_code='uk', reversed=True)


def parse_students(filename):
    '''

    A function that loads the group and student names from the yaml file into the dictionary.

    Args:
        filename(str): name of the file from which the data is taken

    Returns:
        dict: group and name dictionary

    '''

    with open(filename) as student_list:
        dct = upload_students(student_list)
        dct = {
            translit(group): [(translit(name).replace(' ', '_'), name)
                               for name in names]
               for group, names in dct.items()
              }

        return dct


def read_questions(directory):
    '''

    a function that reads questions from a file, sorts them, and writes them into a dictionary.

    Args:
        directory(path): directory where the questions are located

    Returns:
        dict: questions dictionary

    '''

    pth = Path(directory)
    questions = {}
    for filename in sorted(list(pth.glob('*.*'))):
        with open(filename) as qst:
            qst = filename.read().strip().split('\n#')
            qst[1:] = ['#' + q for q in qst[1:]]
            dct[file.name] = qst

    return questions


def generate_questions(students, questions):
    '''

    a function that generates questions for each individual student.

    Args:
        students(dict): group and name dictionary
        questions(dict): questions dictionary

    Returns:
        dict: dictionary of students and questions

    '''

    files = {
        f'{group}_{tr}.rst': f'{sep}{orig}\n{sep}\n'
        for group, lst in students.items()
        for tr, orig in lst
    }

    for category_name, category in questions.items():
        print(f'{category_name:<40}', end='\t')
        personal = list(combinations(category, 2))
        print(f'{len(personal)} combinations')
        assert len(personal) >= len(files), 'Error message'
        shuffle(personal)

        for filename, value in files.items():
            value += '\n' + '\n'.join(personal.pop(0)) + '\n'

    return files


def write_files(outdir, files):
    '''

    A function that creates an .rst file for each student and writes the generated questions into it.

    Args:
        outdir(str): new directory for questions
        files(dict): names and questions in dictionary

    Returns:
        None: None

    '''

    odir = Path(outdir)
    odir.mkdir(exist_ok=True)
    for filename, content in files.items():
        f = odir.joinpath(filename)
        with open(f, 'x') as files:
            files.write(content)


if __name__ == '__main__':
    from sys import argv

    if len(argv) != 4:
        print(f'Usage\n{argv[0]} student_list questions_dir out_dir')
    else:
        student_list, questions_dir, out_dir = argv[1:]
        students = parse_students(student_list)
        questions = read_questions(questions_dir)
        cont = generate_questions(students, questions)
        write_files(out_dir, cont)
