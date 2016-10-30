from time import sleep
from contextlib import closing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Radio:
    def __init__(self):
        self.url = "https://treesradio.com"
        self.driver = webdriver.Chrome()
    # use firefox to get page with javascript generated content
    
    def getCurrentSong(self):
        self.driver.get(self.url)
        sleep(10) 
        name = self.driver.find_element_by_class_name('current-playing-media').text
        print(name)
        return name
    
    def closeBrowser(self):
        self.driver.close()
        
    #url = "https://treesradio.com"
    #driver = webdriver.Chrome()
    
    # wait for the page to load
    # store it to string variable
    #page_source = browser.page_source
    #page_source = driver.page_source

    #print(page_source)

