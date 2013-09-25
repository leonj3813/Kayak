from bs4 import BeautifulSoup
import helper
import time
from selenium import webdriver

# use phantomjs headless browser to fetch webpage

driver = webdriver.PhantomJS('phantomjs.exe')
driver.get('http://www.kayak.com/flights/SCE-ATL/2013-10-04/2013-10-06')

soup = BeautifulSoup(driver.page_source)

results = helper.filter_results(soup)

for item in results:
    Departure1 = item[1]
    latest_departure1 = time.strptime("13:30", "%H:%M")
    Departure2 = item[2]
    latest_departure2 = time.strptime("15:00", "%H:%M")
    
    if Departure1 > latest_departure1 and Departure2 > latest_departure2:
        print item[0] + ", " + time.strftime("%H:%M", Departure1) + ", " + time.strftime("%H:%M", Departure2)


driver.close()


   