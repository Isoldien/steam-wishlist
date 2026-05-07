import menu

import steam_user
from steam_user import *

# Load menu
menu.start()

# search user
# put results into csv
steam_user.userSearch()
steam_user.dictToCSV()