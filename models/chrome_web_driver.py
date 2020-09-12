from selenium.webdriver import Chrome
from selenium.webdriver.chrome import Options

class chr_driver:
    def __init__(self,headless=False):
        self.driver = Chrome()
        self.opts= Options()
        self.opts.headless= headless
    
    def get_driver(self):
        return self.driver
    
    def close(self):
        self.get_driver().close()
