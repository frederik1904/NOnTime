from abc import ABCMeta

import adafruit_character_lcd.character_lcd as characterlcd
import board
import digitalio


class DisplayInterface:
    """ A Strategy class for returning a reply to the user """
    __metaclass__ = ABCMeta

    @classmethod
    def show_msg(cls, msg):
        """ A method to show a message to the user through some I/O device """
        raise NotImplementedError


class ConsoleDisplay(DisplayInterface):
    @classmethod
    def show_msg(cls, msg):
        """ Prints the msg string to the user """
        print(msg)


class LCDDisplay(DisplayInterface):
    lcd_rs = digitalio.DigitalInOut(board.D26)
    lcd_en = digitalio.DigitalInOut(board.D19)
    lcd_d7 = digitalio.DigitalInOut(board.D27)
    lcd_d6 = digitalio.DigitalInOut(board.D22)
    lcd_d5 = digitalio.DigitalInOut(board.D24)
    lcd_d4 = digitalio.DigitalInOut(board.D25)

    lcd_columns = 16
    lcd_rows = 2

    lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)
    lcd.cursor = False

    @classmethod
    def show_msg(cls, msg):
        """ Clears the LCD screen and writes the msg string to it """
        if not isinstance(msg, str):
            raise Exception(f"show_msg needs a string but got {type(msg)}")

        cls.lcd.clear()
        cls.lcd.message = msg

#
# class MyClient(object):
#     def __init__(self, server):
#         if not isinstance(server, DisplayInterface):
#             raise Exception("Bad interface")
#
#         if not DisplayInterface.version() == "1.0":
#             raise Exception("Bad version")
#
#         self.__server = server
#
#     def client_show(cls):
#         cls.__server.show()
#
#
# x = MyClient(MyServer())
#
# x.client_show()
