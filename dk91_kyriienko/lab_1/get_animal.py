#!/usr/bin/env python3

import os
import argparse

import requests as req
from PIL import Image, ImageDraw, ImageFont

"""Get animal's picture.

This module demonstrates using "Some Random Api" for geting pictures with
animals and facts about its.

Example:
    $ python get_animal.py <arg1> <arg2>
    $ python get_animal.py dog --fact

Program will be print fact about dog. 

Attributes:
	api_url<str>: contains url-link for GET-request.    
"""

api_url = 'https://some-random-api.ml'

aparse = argparse.ArgumentParser()
aparse.add_argument('animal', type=str, help='Animal type')

group = aparse.add_mutually_exclusive_group()
group.add_argument('--fact', help='Fact about animal', action='store_true')
group.add_argument('--img', help='Animal image and saving in progam dir',
                   action='store_true')
group.add_argument('--all', help='Fact and print it at image, and saving it',
                   action='store_true')

args = aparse.parse_args()


def set_font(img_w, len_text, /):
    """Use to count font size due to image size.

    Args:
          img_w: image's width
          len_text: length of text

    Returns:
          Font size.
    """
    font_size = 1
    font_s = font_size * len_text

    text_img_w = img_w - 100
    # print('{} {} | {} {}'.format(text_img_w, len_text, font_s, font_size))

    while font_s <= text_img_w*2:
        font_size += 1
        font_s = font_size * len_text

    return font_size


def apiget():
    """Main function to use Some Random API"""
    if args.fact:
        """Returns fact about animal."""
        print(req.get(
            '{}/{}/{}'.format(api_url, 'facts', args.animal)
            ).json().get('fact'))

    elif args.img:
        """Returns animal's image."""
        img_link = req.get(
            '{}/{}/{}'.format(api_url, 'img', args.animal)
            ).json().get('link')
        img_bin = req.get(img_link)

        file = open(img_link[-11:], "wb")
        file.write(img_bin.content)
        file.close()

        os.system(img_link[-11:])

    elif args.all:
        """Returns image which contain fact about animal."""
        get_req = req.get(
            '{}/{}/{}'.format(api_url, 'animal', args.animal)
            ).json()

        fact = get_req.get('fact')
        img_link = get_req.get('image')

        img_bin = req.get(img_link)

        file = open(img_link[-11:], "wb")
        file.write(img_bin.content)
        file.close()

        animal_img = Image.open(img_link[-11:])

        img_width, img_height = animal_img.size

        font = ImageFont.truetype("arial.ttf", set_font(img_width, len(fact)))
        draw = ImageDraw.Draw(animal_img)
        draw.text((50, 50), fact, font=font, fill='black')

        animal_img.save(img_link[-11:])
        os.system(img_link[-11:])


if __name__ == '__main__':
    apiget()
