import cherrypy, hashlib, json, secrets, time
import commands, presets, tags

def getFile(filename,mode="r"):
  f = open(filename,mode)
  contents = f.read()
  f.close()
  return contents
  
nonces = {"jdk":"4955763f001968f2a18abb13d47e89ea"}
passwords = json.loads(getFile("password.json"))
config = json.loads(getFile("config.json"))
tokens = {}

class Root(object):
    @cherrypy.expose
    def home(self):
        return getFile('static/site.html')
        
    @cherrypy.expose
    def execute(self,tags,preset,token):
        [getattr(presets,preset)(tag) for tag in json.loads(tags)]
        
    @cherrypy.expose
    def getTags(self,root="Public"):
        return json.dumps(sorted(tags.getChildren(root)))
    
    @cherrypy.expose
    def on(self):
        commands.on("Parlor NE")

    @cherrypy.expose
    def off(self):
        commands.off("Parlor NE")
        
    @cherrypy.expose
    def nonce(self, username):
        nonce = secrets.token_hex(16)
        nonces[username] = nonce
        return nonce
    
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.accept(media="application/json")
    def token(self):
        data = cherrypy.request.json
        username = data["username"]
        authcode = data["authcode"]
        hashFunc = hashlib.sha256()
        byteStr = passwords[username]+nonces[username]
        hashFunc.update(byteStr.encode('utf-8'))
        expected = hashFunc.hexdigest()
        print(byteStr)
        print(expected)
        print(authcode)
        if authcode == expected:
            token = secrets.token_hex(16)
            tokens[username] = token
            return token        

if __name__ == '__main__':
   cherrypy.tools.json_in
   cherrypy.quickstart(Root(), '/', 'site.conf')