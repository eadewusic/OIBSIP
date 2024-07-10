from selenium import webdriver #import webdriver from selenium (tool/ web framework for automating web browsers)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #to search google search field
from selenium.webdriver.common.keys import Keys #to send specific key that can't be typed like the arrow keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        self.driver.implicitly_wait(15)  # Increased wait time

        try:
        # Wait for the search box to appear
            search = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
            )
        
        # Clear the search box and enter the query
            search.clear()
            search.send_keys(query + Keys.ENTER)

        except Exception as e:
            print(f"An error occurred: {e}")  # Print the error message for debugging


#class instance
assist = info()
assist.get_info('neutron')