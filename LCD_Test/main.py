import machine
from machine import Pin
import utime
def pulseE():
    E.value(1)
    utime.sleep_us(40)
    E.value(0)
    utime.sleep_us(40)

def send2LCD(BinNum):
    DB0.value((BinNum & 0b00000001) >> 0)
    DB1.value((BinNum & 0b00000010) >> 1)
    DB2.value((BinNum & 0b00000100) >> 2)
    DB3.value((BinNum & 0b00001000) >> 3)
    DB4.value((BinNum & 0b00010000) >> 4)
    DB5.value((BinNum & 0b00100000) >> 5)
    DB6.value((BinNum & 0b01000000) >> 6)
    DB7.value((BinNum & 0b10000000) >> 7)
    pulseE()
def setupLCD():
    RS.value(0)
    send2LCD(0b0000111111)
    send2LCD(0b0010111010) # 2 line mode
    send2LCD(0b0001000000) # Set DDRAM address to 0
    RS.value(1)



CS1 = Pin(0, Pin.OUT)
CS2 = Pin(1, Pin.OUT)
RST = Pin(21, Pin.OUT)
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
LED.value(1)
setupLCD()
inputString = "Hello World!"
print(0b1000000000 | 0b01010101)
for x in inputString:
        send2LCD(0b1000000000 | ord(x))
        print(0b1000000000 | ord(x))
        utime.sleep_ms(500)
LED.value(0)