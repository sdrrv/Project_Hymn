from selenium.webdriver import Chrome
from selenium.webdriver.chrome import Options

class chr_driver:
    def __init__(self,headless=False): # not setting headless to True will put it to default, witch is False.
        self.driver = Chrome() #Setting the main driver
        self.opts= Options()
        self.opts.headless= headless # setting the headless mode to the value inputed above
    
    def get_driver(self): #get the main driver
        return self.driver
    
    def close(self): #close the driver
        self.get_driver().close()
