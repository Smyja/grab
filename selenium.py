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

#Set the path for the web driver  
driver = webdriver.Chrome('C:\\Users\\USER\\Downloads\\chromed\\chromedriver')

driver.get('https://food.grab.com/ph/')

#Look for the class
search_box = driver.find_element_by_class_name("ant-input")

#Write what needs to be searched#
search_box.send_keys('manila')

#Submit the text
search_box.send_keys(Keys.ENTER)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div/button').click()

#update the url, since it changes
changed_url='https://food.grab.com/ph/en/restaurants'


submit = driver.page_source
time.sleep(10)
p=driver.find_element_by_class_name('ant-btn.ant-btn-block').click()

clicks = 0
"""
The code block below handles the clicking of the Load more button, if this is to be used the sleep time would need to be increased because it takes a while for the items to be loaded. 

"""
#
#while clicks < 3:
#    try:
#        time.sleep(12)
#        p=driver.find_element_by_class_name('ant-btn.ant-btn-block')
#        p.click()
#        clicks = clicks + 1
#    
#    except:
#        print("button has been clicked",count,"times")
#        
#


time.sleep(10)
#get the source code of the page
submitt = driver.page_source

#Use beautiful soup to scrape the source code
soup = BeautifulSoup(submitt, "html.parser")
s=soup.select("div.ant-row-flex.RestaurantListRow___1SbZY")
s = soup.find('div', attrs={'class':'ant-layout'})
l=[]
for data in s:
    yourl=data.findAll('a')
    for u in yourl:
        a=l.append(u.get("href"))
print("https://food.grab.com"+l)


#Loop through the urls to get the longitude and latitude

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
    #Longitude and latitude are in a dictionary
    print(values[key]['latlng'])
