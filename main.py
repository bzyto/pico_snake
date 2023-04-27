from machine import Pin, SPI, ADC, reset
import max7219
import tm1637
from time import sleep
from random import randint
from functions import *
spi = SPI(0,sck=Pin(2),mosi=Pin(3))
cs = Pin(5, Pin.OUT)
xpin=ADC(Pin(26))
ypin=ADC(Pin(27))
display = max7219.Matrix8x8(spi, cs, 1)
button = Pin(12, Pin.IN, Pin.PULL_DOWN)
display.brightness(10)
score_display = tm1637.TM1637(clk=Pin(16), dio=Pin(17))
def gameover():
    display.fill(0)
    display.show()
class Player:
    def __init__(self, position):
        self.position=position
        self.score=0
        self.head=position[0]
    def eat(self, apple):
            pass
    def score(self):
        self.playerscore+=1
    def p_move(self, direction):
        newposition=[]
        oldhead=self.head[:]
        for i in self.position[1:-1]:
            newposition.append(i)
        newhead=move(self.head, direction)
        self.position=[oldhead]+newposition
        self.position=[newhead]+self.position
        return self.position
    def render(self):
        for cords in self.position:
            display.pixel(cords[0], cords[1], 1)
    def check_selfeat(self):
        if self.head in self.position[2:] and len(self.position)!=3:
            gameover()
    def check_walls(self):
        for i in self.head:
            if i==0 or i==7:
                gameover()

snake=Player([[2,3]])
class Apple:
    def generate_new(self):
        self.position=[randint(0,7), randint(0, 7)]
        if self.position in snake.position:
            self.generate_new()
        display.pixel(self.position[0], self.position[1],1)
    def maintain(self):
        display.pixel(self.position[0], self.position[1],1)
apple=Apple()
apple.generate_new()
prevdir=-2
while True:
    display.fill(0)
    if button.value():
        display.fill(1)
        display.show()
        sleep(2)
        reset()
    xread=xpin.read_u16()
    yread=ypin.read_u16()
    dir=convert_to_direction(xread, yread)
    if dir==-prevdir:
        dir==3
    if dir==3:
        dir=prevdir
    if check_eat(apple.position, snake.head):
        apple.generate_new()
        tail=snake.position[-2]
        snake.p_move(dir)
        snake.score+=1
        snake.position.insert(-1,tail)
    else:
        snake.check_selfeat()
        #snake.check_walls()
        snake.p_move(dir)
    score_display.number(snake.score)
    snake.render()
    apple.maintain()
    display.show()
    prevdir=dir
    sleep(0.2)