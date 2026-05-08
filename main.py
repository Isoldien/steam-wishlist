import menu.menu as menu
import logic.steam_logic as steam_logic
from logic.steam_logic import *
# Load menu
menu.start()

steam_logic.userSearch()
steam_logic.getSteamID()
steam_logic.getWishlist()