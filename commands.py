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
    print(commands)
    client.sendcommand(device["id"],commands)

def on(name):
    command(name,"switch_led",True)
    
def off(name):
    command(name,"switch_led",False)

def color(bulb, colour):
    on(bulb)
    command(bulb,"work_mode","colour")
    command(bulb,"colour_data_v2",colour)
    
def mode(bulb,mode):
    if mode == "off":
        off(bulb)
    elif mode == "initial":
        off(bulb)
        on(bulb)
    else:
        on(bulb)
        commands.command(bulb,"work_mode",mode)

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

setup()
