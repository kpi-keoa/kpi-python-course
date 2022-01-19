#!/usr/bin/env python3

"""This module displays all file names and sizes at the given path."""

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("dir_path", type=str, help='Paste the link to the directory.')
parser.add_argument("-a", "--action", help='Select an action.', default="up", choices=['up', 'down'])
args = parser.parse_args()


def find_files(dir_path: str):
    """Create dictionary with file name and size.
    Args:
        dir_path : The path to the folder.
    Returns:
        dict: Returns a dictionary with folder files and their sizes.
    """
    f_dict = {}
    files = os.listdir(dir_path)
    for fi in files:
        f_path = os.path.join(dir_path, fi)
        if os.path.isfile(f_path):
            onlyfiles = fi
            f_size = round(os.path.getsize(f_path)/1024, 2)
            f_dict[f_size] = onlyfiles
    if ~any(f_dict):
        print("No files found in the specified path") 
    return f_dict


def up():
    """Display a dictionary in ascending order of its key values."""
    up_dict = dict(sorted(find_files(args.dir_path).items()))
    for key in up_dict:
        print(up_dict[key], '->', key, 'Kb')


def down():
    """Display a dictionary by decaying the values of its keys."""
    down_dict = dict(sorted(find_files(args.dir_path).items(), reverse=True))
    for key in down_dict:
        print(down_dict[key], '->', key, 'Kb')


if args.action == 'up':
    up()
elif args.action == 'down':
    down()
else:
    print('OOOPS')
