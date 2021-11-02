# -*- coding: utf-8 -*-
"""


@author: Maro
"""

import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\\Users\\USER\\Downloads\\chromed\\chromedriver')
driver.get('https://food.grab.com/ph/')


#Look for the class
search_box = driver.find_element_by_class_name("ant-input")

#Write what needs to be searched#
search_box.send_keys('manila')

#Submit the text
search_box.send_keys(Keys.ENTER)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div/button').click()


changed_url='https://food.grab.com/ph/en/restaurants'

submit = driver.page_source
time.sleep(10)
p=driver.find_element_by_class_name('ant-btn.ant-btn-block').click()

clicks = 0
#
#while clicks < 3:
#    try:
#        time.sleep(12)
#        p=driver.find_element_by_class_name('ant-btn.ant-btn-block')
#        p.click()
#        clicks = clicks + 1
#    
#    except:
#        print("Number of pages scraped: ",count)
#        
#
url_elements = driver.find_elements_by_xpath("//a[contains(@href, '/ph/en/restaurant')]")

time.sleep(10)
submitt = driver.page_source

soup = BeautifulSoup(submitt, "html.parser")
s=soup.select("div.ant-row-flex.RestaurantListRow___1SbZY")
s = soup.find('div', attrs={'class':'ant-layout'})
l=[]
for data in s:
    yourl=data.findAll('a')
    for u in yourl:
        a=l.append(u.get("href"))
print("https://food.grab.com"+l)


#test

for urls in l:
    driver.get(urls)
    a=driver.page_source
    #print(a)
    soup = BeautifulSoup(a, "html.parser")
    s = soup.find('script', type='application/json')
    a=json.loads(s.text)
    lis=[]
    filename='wa.json'
    f = open(filename,'w')
    f.write(json.dumps(a))
    f.close()
    values=a["props"]["initialReduxState"]["pageRestaurantDetail"]["entities"]
    for key,value in values.items():
        print(key)
    print(key)
    print(values[key]['latlng'])
