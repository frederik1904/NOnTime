from abc import ABCMeta

import RPi.GPIO as GPIO
import time

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
    # GPIO to LCD mapping
    LCD_RS = 7 # Pi pin 26
    LCD_E = 8 # Pi pin 24
    LCD_D4 = 25 # Pi pin 22
    LCD_D5 = 24 # Pi pin 18
    LCD_D6 = 23 # Pi pin 16
    LCD_D7 = 18 # Pi pin 12

    # Device constants
    LCD_CHR = True # Character mode
    LCD_CMD = False # Command mode
    LCD_CHARS = 16 # Characters per line (16 max)
    LCD_LINE_1 = 0x80 # LCD memory location for 1st line
    LCD_LINE_2 = 0xC0 # LCD memory location 2nd line

    # Initialize display
    lcd_init()

    @classmethod
    def show_msg(cls, msg):
        cls.lcd.clear()
        lcd_text(msg,LCD_LINE_
