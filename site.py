import cherrypy, json, time
import commands

class Root(object):
    @cherrypy.expose
    def index(self):
        return "Hello"
    @cherrypy.expose
    def on(self):
        commands.on("Parlor NE")

    @cherrypy.expose
    def off(self):
        commands.off("Parlor NE")

if __name__ == '__main__':
   cherrypy.quickstart(Root(), '/', 'site.conf')
