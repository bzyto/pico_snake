# pico_snake
This is my public repository containing the code for snake running on Raspberry Pi Pico H. 
Components required to build a working version:
- Raspberry Pi Pico, or any microcontroller working with MicroPython,
- 8x8 LED matrix,
- Joystick,
- 7 segment display (not essential),
- button (needed for resetting).

How to connect components to Pico

| Pico | LED Matrix |
|------|---------|
|Pin 2 | CLK |
|Pin 3| CS|
|Pin 4| DIN|
|VBUS | VCC|
|GND | GND|

|Pico | Joystick|
|-----|------|
|Pin 26| VR_y|
|Pin 27| VR_x|
| VBUS | VCC|
|GND | GND|

These cannot be changed, as there are only 3 Pico pins that take analog input.

|Pico | 7 segment display|
|-----|-----------------|
|Pin 16| DIO|
|Pin 17| CLK|
| VBUS | VCC|
|GND | GND|

|Pico | Button|
|-----|------|
|Pin 14| Button|

You could also connect the button to RUN (Pin 30).

To run the code simply save main.py and functions.py on your Pico (probably using ThonnyIDE). Be aware that Pico only handles a certain voltage and you cannot, for example, connect 9V battery to the microcontroller.

I am looking to optimize the joystick input and a clean way to restart the game. If you have any ideas let me know. There are also some issues with selfeat function. You can set your own render time, I found 0.2 seconds is good enough for a decent gameplay. 

