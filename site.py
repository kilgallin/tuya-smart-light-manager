import base64, cherrypy, hashlib, hmac, json, secrets, time
import commands, presets, tags

def getFile(filename,mode="r"):
  f = open(filename,mode)
  contents = f.read()
  f.close()
  return contents
  
nonces = {}
passwords = json.loads(getFile("password.json"))
config = json.loads(getFile("config.json"))
tokens = {}

def sign_string(key_b64, to_sign):
    key = base64.b64decode(key_b64)
    signed_hmac_sha256 = hmac.HMAC(key, to_sign.encode(), hashlib.sha256)
    digest = signed_hmac_sha256.digest()
    return base64.b64encode(digest).decode()

class Root(object):
    @cherrypy.expose
    def home(self):
        return getFile('static/site.html')
        
    @cherrypy.expose
    def execute(self,tags,preset,username,token):
        if token == tokens[username]:
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
        expected = sign_string(base64.b64encode(passwords[username].encode('utf-8')),nonces[username])
        print(expected)
        print(authcode)
        if authcode == expected:
            token = secrets.token_hex(16)
            tokens[username] = token
            return token

    @cherrypy.expose
    def getRoot(self, username):
        return config[username]["root"]

if __name__ == '__main__':
   cherrypy.tools.json_in
   cherrypy.quickstart(Root(), '/', 'site.conf')