""" Raspbery Pi drawing. """

import logging
from PIL import Image, ImageDraw
import PIL
import utils
import draw_utils

if utils.is_raspberry_pi():
    import epaper

def draw_to_epaper_display(name, balance, transactions, next_transfer):
    """ Draws the data to the 250x122 e-paper display."""
 
    try:
        logging.info('Initialising e-Paper display')

        epd = epaper.epaper('epd2in13_V3').EPD()
        epd.init()

        epd.Clear(0xFF)

        # EPD assumes vertical layout, we use horizontal
        screen_width = epd.height
        screen_height = epd.width

        logging.info('Creating image')

        image = Image.new('1', (screen_width, screen_height), 255) # 255: clear the frame 
        
        logging.info('Drawing image')

        draw = ImageDraw.Draw(image)

        margin = 4

        # Draw title

        title = name
        title_font = draw_utils.font_with_size(36)
        title_height = 36
        title_width = screen_width / 2.0
        title_font = draw_utils.largest_font_for(title, title_font, title_width - (2 * margin), title_height - (2 * margin))
        (title_x, title_y) = draw_utils.origin_to_center_text(title, title_font, title_width, title_height)
        draw.text((title_x, title_y), title, font = title_font, fill = 0)

        # Draw horizontal line
        draw.line((0, title_height, screen_width, title_height))
        
        # Draw balance
        balance_y_origin = title_height + 1
        balance_height = screen_height - balance_y_origin
        balance_width = screen_width / 2
        balance_font = draw_utils.font_with_size(32)
        balance_font = draw_utils.largest_font_for(balance, balance_font, balance_width - (2 * margin), balance_height - (2 * margin))
        (balance_x, balance_y) = draw_utils.origin_to_center_text(balance, balance_font, balance_width, balance_height)
        draw.text((balance_x, balance_y_origin + balance_y - margin), balance, font = balance_font, fill = 0)
        
        # Draw vertical line
        draw.line((balance_width, 0, balance_width, screen_height))

        # Draw next
        next_title = next_transfer
        next_font = draw_utils.font_with_size(22)
        next_x_origin = title_width + 1
        next_width = screen_width - next_x_origin
        next_font = draw_utils.largest_font_for(next_title, next_font, next_width - (2 * margin), title_height - (2 * margin))
        (next_x, next_y) = draw_utils.origin_to_center_text(next_title, next_font, next_width, title_height)
        draw.text((next_x_origin + next_x, next_y - margin), next_title, font = next_font, fill = 0)

        # Draw transactions
        if len(transactions) > 0:
            transactions_font = draw_utils.font_with_size(15)
            transactions_origin_x = balance_width + 1 + margin
            transactions_origin_y = title_height + 1 + margin
            transactions_width = screen_width - transactions_origin_x
            transactions_height = screen_height - transactions_origin_y

            longest_text = draw_utils.longest_text(transactions, transactions_font)
            (transaction_x, transaction_y) = draw_utils.origin_to_center_text(longest_text, transactions_font, transactions_width, transactions_height)
            transaction_height = 20

            starting_x = transaction_x + transactions_origin_x
            starting_y = transaction_y + transactions_origin_y - transaction_height - margin

            for index, transaction in enumerate(transactions):
                y_position = starting_y + (transaction_height * index)
                draw.text((starting_x, y_position), transaction, font = transactions_font, fill = 0)

        logging.info('Display image')

        final_image = image.rotate(180, PIL.Image.NEAREST, expand = 0)

        epd.display(epd.getbuffer(final_image))

        logging.info('Sleeping')

        epd.sleep()
    except IOError as e:
        logging.error(e)

    except KeyboardInterrupt:
        epd2in13_V3.epdconfig.module_exit()
        exit()
