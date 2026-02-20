from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.thesun.co.uk/sport/football/"
path = "/Users/coderafnan2824/Downloads/chromeDriver/chromedriver"

service = Service(path)

driver = webdriver.Chrome(service=service)

print("Driver started successfully!")

driver.quit()