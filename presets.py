import commands
import tags

import json
import time

hues = {"red":0, "orange":16, "yellow":40, "lime":80, "green":120, "aqua":136, "cyan":150, "blue":240, "indigo":256, "violet":290, "pink":342}

def hue(tag, color):
    [commands.color(name,json.dumps({"h":hues[color],"s":1000,"v":1000})) for name in tags.getBulbs(tag)]

def red(tag):
    hue(tag,"red")

def orange(tag):
    hue(tag,"orange")
    
def yellow(tag):
    hue(tag,"yellow")

def lime(tag):
    hue(tag,"lime")
    
def green(tag):
    hue(tag,"green")

def aqua(tag):
    hue(tag,"aqua")
    
def cyan(tag):
    hue(tag,"cyan")
    
def blue(tag):
    hue(tag,"blue")
    
def indigo(tag):
    hue(tag,"indigo")

def violet(tag):
    hue(tag,"violet")

def pink(tag):
    hue(tag,"pink") 

def white(tag):
    [commands.mode(name,"white") for name in tags.getBulbs(tag)]
    
def dimmest(tag):
    [commands.brightness(name,10) for name in tags.getBulbs(tag)]
    
def dim(tag):
    [commands.brightness(name,32) for name in tags.getBulbs(tag)]
    
def dimmish(tag):
    [commands.brightness(name,100) for name in tags.getBulbs(tag)]

def brightish(tag):
    [commands.brightness(name,320) for name in tags.getBulbs(tag)]

def bright(tag):
    [commands.brightness(name,750) for name in tags.getBulbs(tag)]
    
def brightest(tag):
    [commands.brightness(name,1000) for name in tags.getBulbs(tag)]
    
def party(tag):
    [commands.mode(name,"scene") for name in tags.getBulbs(tag)]

def timer(name, duration, colour = [.0,0,1000], alarmcolour=[0,1000,1000]):
    commands.on(name)
    commands.command(name,"work_mode", "colour")
    commands.command(name,"colour_data_v2", f'{{"h":{colour[0]},"s":{colour[1]},"v":{colour[2]}}}')
    time.sleep(duration)
    commands.command(name,"colour_data_v2", f'{{"h":{alarmcolour[0]},"s":{alarmcolour[1]},"v":{alarmcolour[2]}}}')
    
def fiveCycle(tag,first,second,third,fourth,fifth,delay=0):
    bulbs = sorted(tags.getBulbs(tag))
    first(bulbs[0])
    second(bulbs[1])
    third(bulbs[2])
    fourth(bulbs[3])
    fifth(bulbs[4])
    time.sleep(delay)
    fiveCycle(tag,fifth,first,second,third,fourth)
    
def oneGreenCycle(tag):
    fiveCycle(tag,green,white,white,white,white)