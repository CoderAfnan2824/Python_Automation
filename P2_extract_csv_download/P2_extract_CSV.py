'''
Docstring for P2_extract_CSV
'''

import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


from io import StringIO

url = "https://www.football-data.co.uk/englandm.php"

headers = {
    "User-Agentt": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

#Parse html data into tree structure
soup = BeautifulSoup(response.text, 'html.parser')

#1. Obtain links of all csv files
csv_links = []

for links in soup.find_all("a", href = True):
    if links['href'].endswith('.csv'):
        full_url = urljoin(url, links["href"])
        csv_links.append(full_url) 

'''
It prints all csv links

for i in csv_links:
    print(i)
'''
#2. Download from all 10 first links
for links in csv_links[:10]:
    file_year = links.split('/')[-2]
    file_name = links.split('/')[-1]
    
    file_response = requests.get(links)
    with open((file_year+file_name), "wb") as f:
        f.write(file_response.content)
        print(f"Downloaded {file_name}")

'''
#Second case: Direct read csv from website link
csv_data = pd.read_csv("https://www.football-data.co.uk/mmz4281/2526/E0.csv")

#Rename columns
csv_data.rename(columns={"AvgCAHH":"Home goals", "AvgCAHA":"Away goals"}, inplace=True)
print(csv_data)
'''