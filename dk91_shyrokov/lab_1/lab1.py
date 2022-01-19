from random import shuffle

"""This module demonstrate editing text file"""

spec_char = {
    ',', '.', '?',
    '[', ']', '(',
    ')', ';', ':',
    '-', '{', '}'
}

def cut_string(file):
    """Create file with text's words.
       In directory with executable file.
    
    Args:
        file: the file name.
    """

    txt_file = open(file, 'r')
    text_content = txt_file.read()

    for ch in spec_char:
        text_content = text_content.replace(ch, '')

    txt_file.close()

    rez_name = file[:-4] + '_rezult_cut.txt' 
    txt_file = open(rez_name, 'w')

    for i in text_content.split():
        txt_file.write(i + '\n')
    txt_file.close()


def cut_part_string(file, *, start, end):
    """Create file with text's words in range.
       In directory with executable file.
    
    Args:
        file: the file name.
        start: start word.
        end: end word.
    """
    txt_file = open(file, 'r')
    text_content = txt_file.read()

    for ch in spec_char:
        text_content = text_content.replace(ch, '')

    txt_file.close()

    rez_name = file[:-4] + '_rezult_part_cut.txt' 
    txt_file = open(rez_name, 'w')

    for i in text_content.split()[start:end]:
        txt_file.write(i + '\n')
    txt_file.close()


def shuffle_text(file):
    """Shuffle text words and generate new
       random text.
    
    Args:
        file: the file name.
    """	
    txt_file = open(file, 'r')
    text_content = txt_file.read()

    text_words = text_content.split()

    shuffle(text_words)

    txt_file.close()

    rez_name = file[:-4] + '_rezult_shuffle.txt' 
    txt_file = open(rez_name, 'w')

    for i in text_words:
        txt_file.write(i + ' ')

    txt_file.write('.')
    txt_file.close()

if __name__ == '__main__':
    import argparse

    aparse = argparse.ArgumentParser()
    aparse.add_argument('file', type=str, help='file adress')

    aparse.add_argument('--num1', type=int, help='num for start cut')
    aparse.add_argument('--num2', type=int, help='num for end cut')

    group = aparse.add_mutually_exclusive_group()
    group.add_argument('--cut', help='cutting text by word', action='store_true')
    group.add_argument('--pcut', help='cutting text by word partly', action='store_true')
    group.add_argument('--shuffle', help='shuffle text', action='store_true')

    arg = aparse.parse_args()

    if arg.shuffle:
        shuffle_text(arg.file)
    elif arg.cut:
        cut_string(arg.file)
    elif arg.pcut:
        cut_part_string(arg.file, start=arg.num1, end=arg.num2)