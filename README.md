# grab
This is a script that scrapes the longitude and latitude on food.grab.com

### Prerequisites
- Python
- Selenium
- Chrome Browser and Chrome Driver
- VPN and the Browser extension for the VPN should be installed in your Chrome browser. 
- Beautiful Soup.

### Notes
- Avoid making too many requests. There is a limit and a blocker for webscraping implemented by grab.com that's why you need to increase the timeout.
- Vpn location can be any country in Asia. 
- Selenium is highly unstable, so at times you might get some errors. Do not fret :) just restart the script. 
- Running the driver as Headless strangely doesn't work properly because of the proxy problem and since i am using a vpn extension you need to use actual proxy addresses to get it working. So the GUI has to pop up. 👀
- You can adjust the ```sliced_links``` depending on how many restaurants longitude and latitude you want to scrape.

### Output
```
Number of pages loaded is  1
Number of pages loaded is  2
Number of pages loaded is  3
['https://food.grab.com/ph/en/restaurant/mcdonald-s-sta-cruz-church-delivery/AWiD5JwQfYWaYaQC4nY4', 'https://food.grab.com/ph/en/restaurant/greenwich-morayta-delivery/2-CYKTRUDUNNVAFE', 'https://food.grab.com/ph/en/restaurant/mang-inasal-morayta-delivery/2-CZDEV76BTREHKE', 'https://food.grab.com/ph/en/restaurant/wendy-s-dapitan-available-for-long-distance-delivery-delivery/PHGFSTI0000017w', 'https://food.grab.com/ph/en/restaurant/angel-s-pizza-legarda-available-for-long-distance-delivery-delivery/PHGFSTI000000zw', 'https://food.grab.com/ph/en/restaurant/jollibee-raon-delivery/2-CZC1EZEYACBTCX', 'https://food.grab.com/ph/en/restaurant/kfc-sta-cruz-delivery/2-CYUZC8BTGJ51GJ', 'https://food.grab.com/ph/en/restaurant/chowking-sta-cruz-manila-delivery/2-CYMHN7DWAGL2WE', 'https://food.grab.com/ph/en/restaurant/coco-fresh-tea-juice-grabkitchen-sampaloc-delivery/2-C2DDLZNZVTV2TA', 'https://food.grab.com/ph/en/restaurant/subway-medical-center-manila-available-for-long-distance-delivery-delivery/PHGFSTI000003e8', 'https://food.grab.com/ph/en/restaurant/yellow-cab-pizza-espana-available-for-long-distance-delivery-delivery/2-CYKCVZNZJTDFLE', 'https://food.grab.com/ph/en/restaurant/three-j-lugawan-earnshaw-street-available-for-long-distance-delivery-delivery/2-C2JTJFEKWCKZLE', 'https://food.grab.com/ph/en/restaurant/army-navy-burger-burrito-ust-dapitan-available-for-long-distance-delivery-delivery/PHGFSTI000000ym', 'https://food.grab.com/ph/en/restaurant/kenny-rogers-roasters-manila-delco-available-for-long-distance-delivery-delivery/2-CYMFVAK2CU5KN6', 'https://food.grab.com/ph/en/restaurant/zark-s-burgers-ust-available-for-long-distance-delivery-delivery/2-C2VZMEUEPGADDA', 'https://food.grab.com/ph/en/restaurant/happilee-korean-kitchen-grabkitchen-sampaloc-available-for-long-distance-delivery-delivery/2-C2JECYXXKF2ATA', 'https://food.grab.com/ph/en/restaurant/boodle-inasal-x-happy-thirstday-sampaloc-available-for-long-distance-delivery-delivery/2-C2J3BF3DSA2YRX', 'https://food.grab.com/ph/en/restaurant/pares-kimchi-intramuros-available-for-long-distance-delivery-delivery/2-CZNKLEUUMBTHCA', 'https://food.grab.com/ph/en/restaurant/something-healthy-ust-available-for-long-distance-delivery-delivery/2-CYVGEUCHNF3ZJN', 'https://food.grab.com/ph/en/restaurant/shakey-s-pizza-espana-delivery/2-CYK2GKKXEKTULJ', 'https://food.grab.com/ph/en/restaurant/papa-john-s-pizza-tri-loyola-building-available-for-long-distance-delivery-delivery/2-CYTZE7BTVVEVDA', 'https://food.grab.com/ph/en/restaurant/pizza-hut-cm-recto-available-for-long-distance-delivery-delivery/2-CYLCMEJHCNTCGJ', 'https://food.grab.com/ph/en/restaurant/macao-imperial-tea-pacific-suites-delivery/PHGFSTI000003fv', 'https://food.grab.com/ph/en/restaurant/turks-recto-delivery/2-CYUJJNU2N6KFTA', 'https://food.grab.com/ph/en/restaurant/serenitea-ust-lacson-available-for-long-distance-delivery-delivery/2-CZJTAAXDGEJABA', 'https://food.grab.com/ph/en/restaurant/food-house-by-madla-ust-delivery/2-CZKJC241LXA1TN', 'https://food.grab.com/ph/en/restaurant/mister-kabab-grabkitchen-sampaloc-available-for-long-distance-delivery-delivery/2-C2JEE7UARFJYEN', 'https://food.grab.com/ph/en/restaurant/grabkitchen-mix-and-match-sampaloc-available-for-long-distance-delivery-delivery/2-C2JTEVCUFFAYA6', 'https://food.grab.com/ph/en/restaurant/dosirakuya-korean-street-food-tondo-available-for-long-distance-delivery-delivery/2-C2MEPBJBLYU2DA', 'https://food.grab.com/ph/en/restaurant/tutong-s-laksa-sampaloc-available-for-long-distance-delivery-delivery/2-C23URRLCNJUTVT', 'https://food.grab.com/ph/en/restaurant/i-love-milktea-tayuman-delivery/2-C2TKT3DVJYUELX', 'https://food.grab.com/ph/en/restaurant/erlinda-s-foodhouse-loyola-street-delivery/2-C2WCFGMANYXTAA', 'https://food.grab.com/ph/en/restaurant/big-scoop-p-guevarra-st-delivery/2-C2UWRYJBTX4JSE', 'https://food.grab.com/ph/en/restaurant/mipanda-milk-tea-hub-lacson-available-for-long-distance-delivery-delivery/2-C2MUNFEKGYAHET', 'https://food.grab.com/ph/en/restaurant/caution-bistro-manila-available-for-long-distance-delivery-delivery/2-C2WFT2UYEUBDCX', 'https://food.grab.com/ph/en/restaurant/24-7-wings-ust-available-for-long-distance-delivery-delivery/2-CYUYBF42AU5ELJ', 'https://food.grab.com/ph/en/restaurant/baliwag-lechon-manok-laong-laan-manila-available-for-long-distance-delivery-delivery/2-C2CGNKTYGA4ZL6', 'https://food.grab.com/ph/en/restaurant/hong-kong-noodles-dimsum-house-quiapo-available-for-long-distance-delivery-delivery/PHGFSTI000001d8', 'https://food.grab.com/ph/en/restaurant/selecta-ice-cream-shop-sta-cruz-delivery/2-CYWFLCNBKFCZJJ', 'https://food.grab.com/ph/en/restaurant/starbucks-puerta-de-isabel-ii-delivery/2-CY42TKKBTKM3LE']
You have scraped 40 links
{'latitude': 14.599870428571428, 'longitude': 120.9797005}
{'latitude': 14.605052185873603, 'longitude': 120.98803399294457}
{'latitude': 14.605344959550562, 'longitude': 120.9881068}
{'latitude': 14.611880266666667, 'longitude': 120.9884545}
{'latitude': 14.599262918622557, 'longitude': 120.9900343411054}
{'latitude': 14.6007231, 'longitude': 120.98439648}
{'latitude': 14.599968222336393, 'longitude': 120.98002192}
{'latitude': 14.599834675, 'longitude': 120.980555425}
```
