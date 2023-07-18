import utilities

tags = utilities.getJson("tags.json")

def tag(name, names):
    tag[name] = names
    
def getBulbs(tag, depth=10):
    if depth == 0:
        return []
    if tag not in tags:
        return [tag] # Assumed to be a bulb if it's not a known tag
    return list(set().union(*[getBulbs(subtag,depth-1) for subtag in tags[tag]]))