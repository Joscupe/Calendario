from machine import Pin
import utime

# Pin Definitions
CS1 = Pin(0, Pin.OUT)
CS2 = Pin(1, Pin.OUT)
RST = Pin(16, Pin.OUT)
E = Pin(7, Pin.OUT)
RW = Pin(6, Pin.OUT)
RS = Pin(5, Pin.OUT)
DB0 = Pin(8, Pin.OUT)
DB1 = Pin(9, Pin.OUT)
DB2 = Pin(10, Pin.OUT)
DB3 = Pin(11, Pin.OUT)
DB4 = Pin(12, Pin.OUT)
DB5 = Pin(13, Pin.OUT)
DB6 = Pin(14, Pin.OUT)
DB7 = Pin(15, Pin.OUT)
LED = Pin(25, Pin.OUT)

charH = [0x7F, 0x08, 0x08, 0x08, 0x7F, 0x00]
print(charH[2])
charE = [0x7F, 0x49, 0x49, 0x49, 0x41, 0x00]
charL = [0x7F, 0x40, 0x40, 0x40, 0x40, 0x00]
charO = [0x3E, 0x41, 0x41, 0x41, 0x3E, 0x00]
charW = [0x7F, 0x08, 0x14, 0x22, 0x41, 0x00]
charR = [0x7F, 0x09, 0x09, 0x09, 0x76, 0x00]
charD = [0x7F, 0x41, 0x41, 0x41, 0x3E, 0x00]
pause = 100  # ms


def glcd_select_page0():
    CS1.value(1)
    CS2.value(0)


def glcd_select_page1():
    CS1.value(0)
    CS2.value(1)


def databus_write(data):
    DB0.value((data & 0b00000001) >> 0)
    DB1.value((data & 0b00000010) >> 1)
    DB2.value((data & 0b00000100) >> 2)
    DB3.value((data & 0b00001000) >> 3)
    DB4.value((data & 0b00010000) >> 4)
    DB5.value((data & 0b00100000) >> 5)
    DB6.value((data & 0b01000000) >> 6)
    DB7.value((data & 0b10000000) >> 7)


def pulse_e():
    E.value(1)
    print("Pulse E")
    utime.sleep_ms(pause)  # might adapt this time
    E.value(0)
    utime.sleep_ms(pause)
    print("Pulse E finsihed")


def glcd_cmd_write(cmd):
    databus_write(cmd)
    RS.value(0)
    RW.value(0)
    pulse_e()


def glcd_data_write(data):
    databus_write(data)
    RS.value(1)
    RW.value(0)
    pulse_e()


def glcd_display_char(char):
    for i in range(6):
        glcd_data_write(char[i])

def glcd_init():
    CS1.value(1)
    CS2.value(1)
    RST.value(1)
    utime.sleep_ms(200)
    glcd_cmd_write(0b00111110)  # display off
    glcd_cmd_write(0b10000000)  # set y address to 0
    glcd_cmd_write(0b10111000)  # set x address to page 0
    glcd_cmd_write(0b11000000)  # set display start line to 0
    glcd_cmd_write(0b00111111)  # display on


# main
LED.value(1)
glcd_init()
# display hello on Page0
glcd_select_page0()
glcd_display_char(charH)
glcd_display_char(charE)
glcd_display_char(charL)
glcd_display_char(charL)
glcd_display_char(charO)
''''
# display world on Page1
glcd_select_page1()
glcd_cmd_write(0b10111111)  # set x address to page 7
glcd_display_char(charW)
glcd_display_char(charO)
glcd_display_char(charR)
glcd_display_char(charL)
glcd_display_char(charD)
utime.sleep_ms(pause)
'''
LED.value(0)
