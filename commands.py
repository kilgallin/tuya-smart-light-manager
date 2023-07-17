import json
import time
import tinytuya

client = {}
devices = []
deviceMap = {}
def setup():
    global client, devices, deviceMap
    client = tinytuya.Cloud()
    devices = client.getdevices()
    deviceMap = {x["name"] : x for x in devices}

def command(name,code,value):
    device = next(d for d in devices if d["name"] == name)
    commands = {
        "commands": [
            {"code": code, "value": value}
        ]
    }
    client.sendcommand(device["id"],commands)

def on(name):
    command(name,"switch_led",True)
    
def off(name):
    command(name,"switch_led",False)

def flash(name,duration=1,post_duration=1):
    on(name)
    time.sleep(duration)
    off(name)
    time.sleep(post_duration)

def dash(name):
    print("dash")
    flash(name,1,0)
    
def dot(name):
    print("dot")
    flash(name,0,0)
    
morse_code = {"0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..",".":".-.-.-",",":"--..--","?":"..--..","!":"-.-.--","-":"-....-","/":"-..-.","@":".--.-.","(":"-.--.",")":"-.--.-"}
morse_code_renderer = {".":dot,"-":dash}
def morseCodeChar(bulb, char):
    print(morse_code[char])
    [morse_code_renderer[x](bulb) for x in morse_code[char]]
    time.sleep(1)
    
def morseCode(bulb, message):
    off(bulb)
    off(bulb)
    time.sleep(2)
    [morseCodeChar(bulb, x) for x in message]


def timer(name, duration, colour = [0,0,1000], alarmcolour=[0,1000,1000], rgb=False):
    '''if(rgb):
        colour = rgb_to_hsv(colour)
        alarmcolour = rgb_to_hsv(alarmcolour)'''
    on(name)
    command(name,"work_mode", "colour")
    command(name,"colour_data_v2", f'{{"h":{colour[0]},"s":{colour[1]},"v":{colour[2]}}}')
    time.sleep(duration)
    command(name,"colour_data_v2", f'{{"h":{alarmcolour[0]},"s":{alarmcolour[1]},"v":{alarmcolour[2]}}}')
def scene(name, scene_num=1, unit_change_mode="jump", bright=500, temperature=500, h=0, s=1000, v=0):
    unit_switch_duration = random.randint(15, 100)
    unit_gradient_duration = random.randint(15, 100)

    json_string = '{"scene_num":%d,"scene_units":{"unit_change_mode":"%s","unit_switch_duration":%d,"unit_gradient_duration":%d,"bright":%d,"temperature":%d,"h":%d,"s":%d,"v":%d}}' % (scene_num, unit_change_mode, unit_switch_duration, unit_gradient_duration, bright, temperature, h, s, v)

    print(json_string)
    command(name,"scene_data_v2", json_string)
    command(name,"work_mode", "scene")
    '''
    commands.scene("Parlor NE", scene_num=8, h=0, s=1000)
    {"scene_num":8,"scene_units":{"unit_change_mode":"jump","unit_switch_duration":24,"unit_gradient_duration":84,"bright":500,"temperature":500,"h":0,"s":1000,"v":0}}
    {'code': 1104, 'msg': 'type is incorrect', 'success': False, 't': 1689560576070, 'tid': 'd7126c66244811ee8c70fe98ebe72f12'}
    '''

setup()


