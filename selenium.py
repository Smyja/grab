# -*- coding: utf-8 -*-
"""


@author: Maro
"""
import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome('C:\\Users\\USER\\Downloads\\chromed\\chromedriver')
driver.get('https://food.grab.com/ph/')

#to get the entire page
#print(driver.find_element_by_xpath('//*').get_attribute("innerHTML"))

#Look for the class
search_box = driver.find_element_by_class_name("ant-input")

#Write what we be searched#
search_box.send_keys('manila')

#Submit the text
search_box.send_keys(Keys.ENTER)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div/button').click()

#update the url, since it changes
changed_url='https://food.grab.com/ph/en/restaurants'

driver.get(changed_url)
submit = driver.page_source
time.sleep(10)
p=driver.find_element_by_class_name('ant-btn.ant-btn-block').click()

clicks = 0

"""
The code block below handles the clicking of the Load more button, 
if this is to be used the sleep time would need to be increased because it takes a while for the items to be loaded. 
Uncomment this block if you want to load everything, grab.com heavily restricts bots so you might have to run this several times.

"""
#while True:
#    try:
#        time.sleep(12)
#        p=driver.find_element_by_class_name('ant-btn.ant-btn-block')
#        p.click()
#        clicks = clicks + 1
#    
#    except:
#        break
#    print("Number of pages loaded is ",clicks)

"""
This only clicks the button 3 times
"""        
while clicks<3:
    try:
        time.sleep(12)
        p=driver.find_element_by_class_name('ant-btn.ant-btn-block')
        p.click()
        clicks = clicks + 1
    
    except:
        break
    print("Number of pages loaded is ",clicks)

time.sleep(15)
#get the source code of the page
submitt = driver.page_source

#Use beautiful soup to scrape the source code
soup = BeautifulSoup(submitt, "html.parser")
s=soup.select("div.ant-row-flex.RestaurantListRow___1SbZY")

l=[]

for data in s:
    yourl=data.findAll('a')
    #Loop through the urls to get the longitude and latitude
    for u in yourl:
        baseurl="https://food.grab.com"
        links=u.get("href")
        a=l.append(baseurl + links)
print(l)
print("You have scraped",len(l),"links")
#Links scraped is 8, because of the time it will take. changing ```l[:8]``` to ```len(l)``` is all you need if you want to scrape everything
sliced_list=l[:8] 


for urls in sliced_list:
    driver.get(urls)
    a=driver.page_source
    #print(a)
    soup = BeautifulSoup(a, "html.parser")
    s = soup.find('script', type='application/json')
    a=json.loads(s.text)
    values=a["props"]["initialReduxState"]["pageRestaurantDetail"]["entities"]
    for key,value in values.items():
        pass
    
    print(values[key]['latlng'])

