import json

def getJson(filename):
  f = open(filename,"r")
  contents = f.read()
  f.close()
  return json.loads(contents)