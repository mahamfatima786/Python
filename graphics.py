# PythonMarg - NEON GLOW VORTEX WALLPAPER
from turtle import *
from colorsys import hsv_to_rgb
setup(1000, 1000)
bgcolor("#F2E1E1")
tracer(400000)
hideturtle()
h = 0.3

def glow_circle(radius, extent, base_color):
    for size, alpha in [(8, 0.65), (6, 0.35), (3, 0.9)]:
        pensize(size)
        color(tuple(c * alpha for c in base_color))
        circle(radius, extent)
    pensize(1.5)
    color(base_color)
    circle(radius, extent)

for i in range(910):
    h += 0.002
    base_color = hsv_to_rgb(h % 1.0, 1, 1)
    goto(0, 0)
    glow_circle(190 - i/4, 90, base_color)
    glow_circle(40, 70, base_color)
    glow_circle(6 + i/6, 360, base_color)
    glow_circle(200 - i/3, -90, base_color)
    left(10.6)

update()
done()