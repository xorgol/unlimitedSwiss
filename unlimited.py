import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

print("Import complete")


if(len(sys.argv)>= 2):
    url = sys.argv[1]
else:
    url = "https://www.swisstransfer.com/d/a237d483-2e23-45a8-86e2-cdf01f2e7072"

# initiating the webdriver
op = webdriver.ChromeOptions()
op.add_argument("user-data-dir=selenium") 
driver = webdriver.Chrome(options=op) 

driver.get(url) 

# this is just to ensure that the page is loaded
time.sleep(2) 
print("Slept for 2, now close cookies banner")

time.sleep(10)
print("Did you close the cookie banner?")

html = driver.page_source
# this renders the JS code and stores all
# of the information in static HTML code.


all_links = driver.find_elements(By.CLASS_NAME, "downloadFile")
print(len(all_links))
for i in range(0, len(all_links)):
    driver.get(url)
    time.sleep(2)
    html=driver.page_source
    all_links = driver.find_elements(By.CLASS_NAME, "downloadFile")
    print("i = {}".format(i))
    all_links[i].click()
    time.sleep(10)