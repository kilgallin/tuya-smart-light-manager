import cherrypy, json, time
import commands, presets

def getFile(filename,mode="r"):
  f = open(filename,mode)
  contents = f.read()
  f.close()
  return contents

class Root(object):
    @cherrypy.expose
    def home(self):
        return getFile('static/site.html')
        
    @cherrypy.expose
    def execute(self,tags,preset):
        getattr(presets,preset)(tags)
    
    @cherrypy.expose
    def on(self):
        commands.on("Parlor NE")

    @cherrypy.expose
    def off(self):
        commands.off("Parlor NE")

if __name__ == '__main__':
   cherrypy.quickstart(Root(), '/', 'site.conf')
