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


def turnOnLCD():
    RS.value(0)
    RW.value(0)
    DB7.value(0)
    DB6.value(0)
    DB5.value(1)
    DB4.value(1)
    DB3.value(1)
    DB2.value(1)
    DB1.value(1)
    DB0.value(1)

def turnOffLCD():
    RS.value(0)
    RW.value(0)
    DB7.value(0)
    DB6.value(0)
    DB5.value(1)
    DB4.value(1)
    DB3.value(1)
    DB2.value(1)
    DB1.value(1)
    DB0.value(0)


def setcmd(cmd):
    RS.value(int(cmd[0]))
    RW.value(int(cmd[1]))
    DB7.value(int(cmd[2]))
    DB6.value(int(cmd[3]))
    DB5.value(int(cmd[4]))
    DB4.value(int(cmd[5]))
    DB3.value(int(cmd[6]))
    DB2.value(int(cmd[7]))
    DB1.value(int(cmd[8]))
    DB0.value(int(cmd[9]))

print("Hello World!")
LED.value(1)
utime.sleep(0.5)
for i in range(5):
    LED.value(0)
    utime.sleep(0.1)
    LED.value(1)
    utime.sleep(0.1)

E.value(1)
CS1.value(0)
CS2.value(0)
RST.value(0)
turnOnLCD()
print("LCD ON")
utime.sleep(2)

setcmd("0010111000")
print("X Position 0")
utime.sleep(0.5)

setcmd("0001000000")
print("Y Position 0")
utime.sleep(0.5)

setcmd("1001000001")
print("A Position 0")
utime.sleep(0.5)
for i in range(30):
    setcmd("1010111000")
    print("B Position 0")
    utime.sleep(0.5)

utime.sleep(5)
turnOffLCD()
print("LCD OFF")
LED.value(0)
