import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_WEB_API") # get key from system env, dependant on OS 
steam = Steam(KEY)

global name

def userSearch() :
    name = input('What is your steam name?' + '\n')
    result = steam.users.search_user(name)
    print(result)