from selenium import webdriver #import webdriver from selenium (tool/ web framework for automating web browsers)
from selenium.webdriver.chrome.service import Service

#download chrome webdriver = https://sites.google.com/chromium.org/driver/
class info():
    def __init__(self):
        chromedriver_path = 'C:/Users/HP/.wdm/drivers/chromedriver-win64/chromedriver.exe'
        # Create a Service obj, initiate the driver to control chrome
        self.service = Service(executable_path=chromedriver_path)
        # Initiate the Chrome driver using the service obj
        self.driver = webdriver.Chrome(service=self.service)
    
#task performing main function, query is what you want to search
    def get_info(self, query):
        self.query = query
        self.driver.get("https://google.com") #self.driver initiates the chromedriver, .get method takes the url for a search
        self.driver.implicitly_wait(10) #wait for up to 10 seconds for elements to load

#class instance
assist = info()
assist.get_info('hello')