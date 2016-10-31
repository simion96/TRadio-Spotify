from time import sleep
from contextlib import closing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

class Radio:
    def __init__(self):
        self.url = "https://treesradio.com"
        
    # use firefox to get page with javascript generated content
    
    def getCurrentSong(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        sleep(10) 
        song = self.driver.find_element_by_class_name('current-playing-media').text
        #song = "Joey Fatts - Choppa [ft. ASAP Rocky & Danny Brown] --- Joey Fatts - Choppa [ft. ASAP Rocky & Danny Brown]"
        
        #remove duplicated name
        if ("---" in song):
            song = song[0:song.index("---")-1]
        
        #disallowed characters
        song2 = re.sub('.', lambda m: {'-':'', ':':'', '\'':''}.get(m.group(), m.group()), song)
        
        print("song before regex " +song)
        #check for brackets and contents inside it
        garbage = re.search(r"(\([A-Za-z0-9_ &^%$£!.;:<>+~#,()]+)\)", song2)
        if (garbage == None):
            garbage = re.search(r"\[([A-Za-z0-9_ &^%$£!.;:<>+~#,()]+)\]", song2)
        
        #if found, remove it
        if (garbage != None):
            if (garbage.group() in song2):
                song2 = song2.replace(garbage.group(), "")
       
        print("song after regex" + song2)
        return song2
    
    def closeBrowser(self):
        self.driver.close()
    
    def checkSongName(self, song):
        song2 = ""
        if ("---" in song):
            song2 = song[0:song.index("---")-1]
        return song2
        
    #url = "https://treesradio.com"
    #driver = webdriver.Chrome()
    
    # wait for the page to load
    # store it to string variable
    #page_source = browser.page_source
    #page_source = driver.page_source

    #print(page_source)

