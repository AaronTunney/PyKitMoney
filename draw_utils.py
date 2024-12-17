""" Provides fonts and geometry utilities """

import os
from PIL import ImageFont

picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')

def font_with_size(size: int):
    """ Returns the default font with the desired size """
    return ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), size)

def largest_font_for(text, font, max_width: float, max_height: float):
    """ Finds the largest font size for a piece of text within a rectangle. """
    font_size = max_height

    biggest_size = None
    while biggest_size is None:
        font = font_with_size(int(font_size))
        (width, height) = size_of_text(text, font)
        if width < max_width and height < max_height:
            biggest_size = font_size
        font_size -= 1

    return font_with_size(int(biggest_size))

def size_of_text(text, font):
    """ Returns the size of text for a given font. """
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text).getbbox()[2]
    text_height = font.getmask(text).getbbox()[3] + descent

    return (round(text_width), round(text_height))

def origin_to_center_text(text, font, width: float, height: float):
    """ 
    Returns the coordinates to center text within a rect.
    Only works for single line text.
    """
    (text_width, text_height) = size_of_text(text, font)

    return (round((width - text_width) / 2), round((height - text_height) / 2))

def longest_text(texts, font):
    """ Returns the longest text out of a list. """

    widths = [size_of_text(text, font)[0] for text in texts]
    longest_index = widths.index(max(widths))
    return texts[longest_index]