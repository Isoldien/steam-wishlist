import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_WEB_API") # get key from system env, dependant on OS 
steam = Steam(KEY)

# search for a user 
def userSearch() :
    global name, search
    name = input('What is your Steam Username?' + '\n')
    search = steam.users.search_user(name)
    return name, search