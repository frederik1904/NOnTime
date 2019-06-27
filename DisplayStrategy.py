from abc import ABCMeta

import adafruit_character_lcd.character_lcd as characterlcd
import board
import digitalio


class DisplayInterface:
    ___metaclass___ = ABCMeta

    @classmethod
    def version(cls):
        return "1.0"

    @classmethod
    def show_msg(cls, msg):
        raise NotImplementedError


class ConsoleDisplay(DisplayInterface):
    @classmethod
    def show_msg(cls, msg):
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
