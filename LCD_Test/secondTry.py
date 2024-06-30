import machine
from machine import Pin
import utime

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
def startEndSignal():
    LED.value(0)
    utime.sleep_ms(100)
    LED.value(1)
    utime.sleep_ms(100)
    LED.value(0)
    utime.sleep_ms(100)

def send2LCD(BinNum):
    DB0.value((BinNum & 0b0000000001) >> 0)
    DB1.value((BinNum & 0b0000000010) >> 1)
    DB2.value((BinNum & 0b0000000100) >> 2)
    DB3.value((BinNum & 0b0000001000) >> 3)
    DB4.value((BinNum & 0b0000010000) >> 4)
    DB5.value((BinNum & 0b0000100000) >> 5)
    DB6.value((BinNum & 0b0001000000) >> 6)
    DB7.value((BinNum & 0b0010000000) >> 7)
    RW.value((BinNum & 0b0100000000) >> 8)
    RS.value((BinNum & 0b1000000000) >> 9)
    LED.value((BinNum & 0b1000000000) >> 9)
    print((BinNum & 0b1000000000) >> 9)
def setupLCD():
    RS.value(0)
    print("Setting up LCD")
    utime.sleep_ms(500)
    send2LCD(0b0000111111)
    send2LCD(0b0010111010) # 2 line mode
    send2LCD(0b0001000000) # Set DDRAM address to 0
    RS.value(1)


startEndSignal()
E.value(1)
CS1.value(1)
CS2.value(0)
setupLCD()
inputString = "Hello World!"
print(0b1000000000 | 0b01010101)
for x in inputString:
        send2LCD(0b1000000000 | ord(x))
        print(0b1000000000 | ord(x))
        utime.sleep_ms(500)
startEndSignal()