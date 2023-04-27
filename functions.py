from machine import Pin, SPI, ADC, reset
import max7219
from time import sleep
from random import randint
def convert_to_direction(xValue, yValue):
    if xValue <= 1000:
            xStatus = 1
            return xStatus
    elif xValue >= 60000:
            xStatus = -1
            return xStatus
    if yValue <= 1000:
            yStatus = 2
            return yStatus
    elif yValue >= 60000:
            yStatus = -2
            return yStatus
    return 3

def mymap(num):
  return (-1 + (float(num) / float(65535 - 800) * 2))
def move(position, direction):
    if direction==1:
        position[0]+=-1
    if direction==-1:
        position[0]+=1
    if direction==2:
        position[1]+=1
    if direction==-2:
        position[1]+=-1
    for i in 0,1:
        if position[i]==-1:
            position[i]=7
        if position[i]==8:
            position[i]=0
    return position
def check_eat(apple, position):
    if apple==position:
        return True
    return False