import time
from contextlib import closing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# use firefox to get page with javascript generated content
url = "https://treesradio.com"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(10)
button = driver.find_element_by_class_name('current-playing-media').text
print(button)
driver.close()
 # wait for the page to load
 # store it to string variable
 #page_source = browser.page_source
#page_source = driver.page_source

#print(page_source)

