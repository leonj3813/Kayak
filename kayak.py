from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import helper
import time
import os

next_urls = helper.return_URLs()

for url in next_urls:
    # use phantomjs headless browser to fetch webpage
    driver = webdriver.PhantomJS("phantomjs")
    driver.get(url)
   #driver.delete_all_cookies()

    soup = BeautifulSoup(driver.page_source)
    print url
    results = helper.filter_results(soup)

    for item in results:
        Departure1 = item[1]
        latest_departure1 = time.strptime("13:30", "%H:%M")
        Departure2 = item[2]
        latest_departure2 = time.strptime("15:00", "%H:%M")  

        #if (Departure1 > latest_departure1) and (Departure2 > latest_departure2):
        print url
        print item[0] + ", " + time.strftime("%H:%M", Departure1) + ", " + time.strftime("%H:%M", Departure2)

    driver.close()


   