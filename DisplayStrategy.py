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
    LCD_RS = 7  # Pi pin 26
    LCD_E = 8  # Pi pin 24
    LCD_D4 = 25  # Pi pin 22
    LCD_D5 = 24  # Pi pin 18
    LCD_D6 = 23  # Pi pin 16
    LCD_D7 = 18  # Pi pin 12

    # Device constants
    LCD_CHR = True  # Character mode
    LCD_CMD = False  # Command mode
    LCD_CHARS = 16  # Characters per line (16 max)
    LCD_LINE_1 = 0x80  # LCD memory location for 1st line
    LCD_LINE_2 = 0xC0  # LCD memory location 2nd line

    def t(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbers
        GPIO.setup(self.LCD_E, GPIO.OUT)  # Set GPIO's to output mode
        GPIO.setup(self.LCD_RS, GPIO.OUT)
        GPIO.setup(self.LCD_D4, GPIO.OUT)
        GPIO.setup(self.LCD_D5, GPIO.OUT)
        GPIO.setup(self.LCD_D6, GPIO.OUT)
        GPIO.setup(self.LCD_D7, GPIO.OUT)

        # Initialize display
        self.lcd_init()

    @classmethod
    def show_msg(cls, msg):
        # Loop - send text and sleep 3 seconds between texts
        # Change text to anything you wish, but must be 16 characters or less
        cls.lcd_text(cls, msg, cls.LCD_LINE_1)
        cls.lcd_text(cls, msg, cls.LCD_LINE_2)

    # Initialize and clear display
    def lcd_init(self):
        self.lcd_write(0x33, self.LCD_CMD)  # Initialize
        self.lcd_write(0x32, self.LCD_CMD)  # Set to 4-bit mode
        self.lcd_write(0x06, self.LCD_CMD)  # Cursor move direction
        self.lcd_write(0x0C, self.LCD_CMD)  # Turn cursor off
        self.lcd_write(0x28, self.LCD_CMD)  # 2 line display
        self.lcd_write(0x01, self.LCD_CMD)  # Clear display
        time.sleep(0.0005)  # Delay to allow commands to process

    def lcd_write(self, bits, mode):
        # High bits
        GPIO.output(self.LCD_RS, mode)  # RS

        GPIO.output(self.LCD_D4, False)
        GPIO.output(self.LCD_D5, False)
        GPIO.output(self.LCD_D6, False)
        GPIO.output(self.LCD_D7, False)
        if bits & 0x10 == 0x10:
            GPIO.output(self.LCD_D4, True)
        if bits & 0x20 == 0x20:
            GPIO.output(self.LCD_D5, True)
        if bits & 0x40 == 0x40:
            GPIO.output(self.LCD_D6, True)
        if bits & 0x80 == 0x80:
            GPIO.output(self.LCD_D7, True)

        # Toggle 'Enable' pin
        self.lcd_toggle_enable()

        # Low bits
        GPIO.output(self.LCD_D4, False)
        GPIO.output(self.LCD_D5, False)
        GPIO.output(self.LCD_D6, False)
        GPIO.output(self.LCD_D7, False)
        if bits & 0x01 == 0x01:
            GPIO.output(self.LCD_D4, True)
        if bits & 0x02 == 0x02:
            GPIO.output(self.LCD_D5, True)
        if bits & 0x04 == 0x04:
            GPIO.output(self.LCD_D6, True)
        if bits & 0x08 == 0x08:
            GPIO.output(self.LCD_D7, True)

        # Toggle 'Enable' pin
        self.lcd_toggle_enable()

    def lcd_toggle_enable(self):
        time.sleep(0.0005)
        GPIO.output(self.LCD_E, True)
        time.sleep(0.0005)
        GPIO.output(self.LCD_E, False)
        time.sleep(0.0005)

    def lcd_text(self, message, line):
        # Send text to display
        message = message.ljust(self.LCD_CHARS, " ")

        self.lcd_write(self, line, self.LCD_CMD)

        for i in range(self.LCD_CHARS):
            self.lcd_write(self, ord(message[i]), self.LCD_CHR)
