from selenium.webdriver import Chrome
from selenium.webdriver.chrome import Options

class chr_driver:
    def __init__(self,headless=False):
        self.driver = Chrome()
        self.opts= Options()
        self.opts.headless= headless
