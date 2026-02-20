from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd

from datetime import datetime
import os, sys



def logic():

    app_path = os.path.dirname(sys.executable)
    print(app_path)

    datetime = datetime.now()

    ddmmYY = datetime.strftime("%m%d%Y")

    website = "https://www.thesun.co.uk/sport/football/"
    path = "/Users/coderafnan2824/Downloads/chromeDriver/chromedriver"

    service = Service(executable_path=path)

    #Headless-mode
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=service, options=options)


    driver.get(website)

    containers = driver.find_elements(by="xpath", value='//div[@class="story__copy-container"]')

    titles = []
    subtitles = []
    links = []

    for container in containers[:4]:
        title = container.find_element(by="xpath", value='./a/p').text
        sub_title = container.find_element(by="xpath", value='./a/h3').text
        link = container.find_element(by="xpath", value="./a").get_attribute("href")

        titles.append(title)
        subtitles.append(sub_title)
        links.append(link)


    my_dict = {'title': titles,
            'subtitle':subtitles,
            'link':links}

    df = pd.DataFrame(my_dict)
    file_name = f'headlines-{ddmmYY}.csv'
    final_path = os.path.join(app_path, file_name) 
    df.to_csv()

    driver.quit()

if __name__ == "__main__":
    logic()
