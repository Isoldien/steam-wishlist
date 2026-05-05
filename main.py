import os #to be used for env, dependant on operating system
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")
steam = Steam(KEY)

def start():
    steam_wishlist = r"""
 _                                     _     _     _ _     _   
 ___| |_ ___  __ _ _ __ ___      __      _(_)___| |__ | (_)___| |_ 
/ __| __/ _ \/ _` | '_ ` _ \ ____\ \ /\ / / / __| '_ \| | / __| __|
\__ \ ||  __/ (_| | | | | | |_____\ V  V /| \__ \ | | | | \__ \ |_ 
|___/\__\___|\__,_|_| |_| |_|      \_/\_/ |_|___/_| |_|_|_|___/\__|
"""
    print(steam_wishlist)

start()