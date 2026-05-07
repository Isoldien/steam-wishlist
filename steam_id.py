import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_WEB_API") # get key from system env, dependant on OS 
steam = Steam(KEY)

def userSearch() :
    global name
    name = input('What is your Steam Username?' + '\n')
    search = steam.users.search_user(name)
    return search, name