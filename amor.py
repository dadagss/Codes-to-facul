from turtle import *
import keyboard



color ('red')
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()

while True:
    if keyboard.is_pressed('esc'):
        break