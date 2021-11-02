# grab
This is a script that scrapes the longitude and latitude on food.grab.com

### Prerequisites
- Chrome Browser and Chrome Driver
- VPN and the Browser extension for the VPN should be installed in your Chrome browser. 
- Beautiful Soup.

### Notes
- Avoid making too many requests. There is a limit and a blocker for webscraping implemented by grab.com that's why you need to increase the timeout.
- Vpn location can be any country in Asia. 
- Selenium is highly unstable, so at times you might get some errors. Do not fret :) just restart the script. 
- Running the driver as Headless strangely doesn't work properly because of the proxy problem and since i am using a vpn extension you need to use actual proxy addresses to get it working. So the GUI has to pop up. 👀
