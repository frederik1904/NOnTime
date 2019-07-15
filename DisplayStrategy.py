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

    def ___init___(self):
        # Initialize display
        self.lcd_init()

    @classmethod
    def show_msg(cls, msg):
        cls.lcd.clear()
        cls.lcd_text(msg, cls.LCD_LINE_1)

    # Initialize and clear display
    def lcd_init(cls):
        cls.lcd_write(0x33, cls.LCD_CMD) # Initialize
        cls.lcd_write(0x32, cls.LCD_CMD) # Set to 4-bit mode
        cls.lcd_write(0x06, cls.LCD_CMD) # Cursor move direction
        cls.lcd_write(0x0C, cls.LCD_CMD) # Turn cursor off
        cls.lcd_write(0x28, cls.LCD_CMD) # 2 line display
        cls.lcd_write(0x01, cls.LCD_CMD) # Clear display
        time.sleep(0.0005) # Delay to allow commands to process

    def lcd_write(cls, bits, mode):
        # High bits
        GPIO.output(cls.LCD_RS, mode) # RS

        GPIO.output(cls.LCD_D4, False)
        GPIO.output(cls.LCD_D5, False)
        GPIO.output(cls.LCD_D6, False)
        GPIO.output(cls.LCD_D7, False)
        if bits&0x10==0x10:
            GPIO.output(cls.LCD_D4, True)
        if bits&0x20==0x20:
            GPIO.output(cls.LCD_D5, True)
        if bits&0x40==0x40:
            GPIO.output(cls.LCD_D6, True)
        if bits&0x80==0x80:
            GPIO.output(cls.LCD_D7, True)

        # Toggle 'Enable' pin
        cls.lcd_toggle_enable()

        # Low bits
        GPIO.output(cls.LCD_D4, False)
        GPIO.output(cls.LCD_D5, False)
        GPIO.output(cls.LCD_D6, False)
        GPIO.output(cls.LCD_D7, False)
        if bits&0x01==0x01:
            GPIO.output(cls.LCD_D4, True)
        if bits&0x02==0x02:
            GPIO.output(cls.LCD_D5, True)
        if bits&0x04==0x04:
            GPIO.output(cls.LCD_D6, True)
        if bits&0x08==0x08:
            GPIO.output(cls.LCD_D7, True)

        # Toggle 'Enable' pin
        cls.lcd_toggle_enable()

    def lcd_toggle_enable(cls):
        time.sleep(0.0005)
        GPIO.output(cls.LCD_E, True)
        time.sleep(0.0005)
        GPIO.output(cls.LCD_E, False)
        time.sleep(0.0005)

    def lcd_text(cls, message,line):
        # Send text to display
        message = message.ljust(cls.LCD_CHARS," ")

        cls.lcd_write(line, cls.LCD_CMD)

        for i in range(cls.LCD_CHARS):
            cls.lcd_write(ord(message[i]), cls.LCD_CHR)
