import commands
import json

def green(name):
    commands.color(name,json.dumps({"h":128,"s":1000,"v":1000}))
    
def white(name):
    commands.mode(name,"white")

def timer(name, duration, colour = [.0,0,1000], alarmcolour=[0,1000,1000]):
    on(name)
    command(name,"work_mode", "colour")
    command(name,"colour_data_v2", f'{{"h":{colour[0]},"s":{colour[1]},"v":{colour[2]}}}')
    time.sleep(duration)
    command(name,"colour_data_v2", f'{{"h":{alarmcolour[0]},"s":{alarmcolour[1]},"v":{alarmcolour[2]}}}')