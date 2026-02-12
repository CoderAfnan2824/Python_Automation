'''
Project 1: This will extract tables from websites using Pandas Library
'''



import requests
import pandas as pd

#To convert string data as a file
from io import StringIO


url = "https://en.wikipedia.org/wiki/List_of_Stranger_Things_episodes"

#needed to pretend as a USER
headers = {
    "User-Agent": "Mozilla/5.0"
}

#header tell that you are logging into URL as a user, not as a bot
response = requests.get(url,headers=headers)

#stringIO treats your html string data as a filee
html_data = StringIO(response.text)

stranger_things = pd.read_html(html_data)

#number of tables
df = stranger_things[2]
print(df.to_string)