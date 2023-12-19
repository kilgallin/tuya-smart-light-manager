import cherrypy, json, time
import commands, presets, tags

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
        [getattr(presets,preset)(tag) for tag in json.loads(tags)]
        
    @cherrypy.expose
    def getTags(self,root="Living Space"):
        return json.dumps(sorted(tags.getChildren(root)))
    
    @cherrypy.expose
    def on(self):
        commands.on("Parlor NE")

    @cherrypy.expose
    def off(self):
        commands.off("Parlor NE")

if __name__ == '__main__':
   cherrypy.quickstart(Root(), '/', 'site.conf')
