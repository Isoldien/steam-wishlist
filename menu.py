#pymenu
from pymenu import Menu
import steam_id

def start():
    steam_wishlist = r"""
     _                                     _     _     _ _     _   
 ___| |_ ___  __ _ _ __ ___      __      _(_)___| |__ | (_)___| |_ 
/ __| __/ _ \/ _` | '_ ` _ \ ____\ \ /\ / / / __| '_ \| | / __| __|
\__ \ ||  __/ (_| | | | | | |_____\ V  V /| \__ \ | | | | \__ \ |_ 
|___/\__\___|\__,_|_| |_| |_|      \_/\_/ |_|___/_| |_|_|_|___/\__|
"""

    menu = Menu(steam_wishlist)
    menu.add_option("Steam ID", lambda: steam_id.userSearch())
    menu.show()

