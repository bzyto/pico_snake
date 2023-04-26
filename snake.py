from machine import Pin, SPI, ADC, reset
import max7219
from time import sleep
from random import randint

spi = SPI(0,sck=Pin(2),mosi=Pin(3))
cs = Pin(5, Pin.OUT)
xpin=ADC(Pin(26))
ypin=ADC(Pin(27))
display = max7219.Matrix8x8(spi, cs, 1)
button = Pin(12, Pin.IN, Pin.PULL_DOWN)
display.brightness(10)
possible_directions={(2, 1), (1, 2), (0, 1), (1, 0)}
position=[4, 4]
display.fill(0)
display.pixel(position[0], position[1], 1)
display.show()
def convert_to_direction(xValue, yValue):
    if xValue <= 1000:
            xStatus = "up"
            return xStatus
    elif xValue >= 60000:
            xStatus = "down"
            return xStatus
    if yValue <= 1000:
            yStatus = "left"
            return yStatus
    elif yValue >= 60000:
            yStatus = "right"
            return yStatus
    return "follow"

def mymap(num):
  return (-1 + (float(num) / float(65535 - 800) * 2))
def move(position, direction):
    if direction=="up":
        position[0]+=-1
    if direction=="down":
        position[0]+=1
    if direction=="left":
        position[1]+=1
    if direction=="right":
        position[1]+=-1
    for i in 0,1:
        if position[i]==-1:
            position[i]=7
        if position[i]==8:
            position[i]=0
    return position
xread_initial=mymap(xpin.read_u16())
yread_initial=mymap(ypin.read_u16())
xmin=xread_initial
while True:
    if button.value():
        reset()
    xread=xpin.read_u16()
    yread=ypin.read_u16()
    dir=convert_to_direction(xread, yread)
    move(position,dir)
    display.fill(0)
    display.pixel(position[0], position[1], 1)
    display.show()
    sleep(0.5)