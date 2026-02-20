from selenium import webdriver
from selenium.webdriver.edge.service import Service



from selenium import webdriver
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
path = "/Users/coderafnan2824/Downloads/chromeDriver"
driver = webdriver.Edge()
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

df.to_csv('headlines.csv')

driver.quit()