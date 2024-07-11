from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class poem():
    def __init__(self):
        chromedriver_path = 'C:/Users/HP/.wdm/drivers/chromedriver-win64/chromedriver.exe'
        self.service = Service(executable_path=chromedriver_path)
        self.driver = webdriver.Chrome(service=self.service)

#main working function of our YouTube automation script
    def play(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com/results?search_query=" + query)

        try:
        # Search for the element and interact with it
            video = self.driver.find_element(By.ID, "video-title")
            video.click() #click on video link to play the video

            time.sleep(124.8)  # Keep the browser open till the poem ends
            self.driver.quit()  # Close the browser after waiting

        except Exception as e:
            print(f"An error occurred: {e}")  # Print the error message for debugging

# assist = poem()
# assist.play('Dear Young Woman')