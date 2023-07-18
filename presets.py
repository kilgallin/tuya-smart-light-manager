import commands
import tags

import json

def green(tag):
    [commands.color(name,json.dumps({"h":128,"s":1000,"v":1000})) for name in tags.getBulbs(tag)]
    
def white(tag):
    [commands.mode(name,"white") for name in tags.getBulbs(tag)]

def pink(tag):
    [commands.color(name,json.dumps({"h":342,"s":1000,"v":1000})) for name in tags.getBulbs(tag)]
    
def party(tag):
    [commands.mode(name,"scene") for name in tags.getBulbs(tag)]

def timer(name, duration, colour = [.0,0,1000], alarmcolour=[0,1000,1000]):
    commands.on(name)
    commands.command(name,"work_mode", "colour")
    commands.command(name,"colour_data_v2", f'{{"h":{colour[0]},"s":{colour[1]},"v":{colour[2]}}}')
    time.sleep(duration)
    commands.command(name,"colour_data_v2", f'{{"h":{alarmcolour[0]},"s":{alarmcolour[1]},"v":{alarmcolour[2]}}}')