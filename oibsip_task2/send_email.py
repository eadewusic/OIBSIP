from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class email():
    def __init__(self):
        chromedriver_path = 'C:/Users/HP/.wdm/drivers/chromedriver-win64/chromedriver.exe'
        self.service = Service(executable_path=chromedriver_path)
        self.driver = webdriver.Chrome(service=self.service)

#main working function of our email sending script
    def send_email(self, query):
        self.query = query
        self.driver.get("https://mail.google.com/mail/u/0/?fs=1&tf=cm&source=mailto&to=" + query)

assist = email()
assist.send_email('nexogirlss@gmail.com')