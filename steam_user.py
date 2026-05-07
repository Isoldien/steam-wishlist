import os
from steam_web_api import Steam
import csv
import pandas as pd

KEY = os.environ.get("STEAM_WEB_API") # get key from system env, dependant on OS 
steam = Steam(KEY)

# search for a user 
def userSearch() :
    global name, search
    name = str(input('What is your Steam Username?' + '\n'))
    search = steam.users.search_user(name)
    return name, search

# convert dictioniary to CSV
def dictToCSV() :
    # @TODO add exception if directory exists 
    # @TODO add exception if file already exists

    # create directory and filename
    os.mkdir("csv")
    csv_filename = "csv/search_results"

    # convert dict to csv
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(search.keys())
        writer.writerow(search.values())
    


