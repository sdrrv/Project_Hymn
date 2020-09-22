from models.chrome_web_driver import chr_driver

class controller:
    def __init__(self):
        self.webdriver = chr_driver(True)
    def open(self,to_open):
        self.webdriver.get_driver().get(to_open)
    def shearch_youtube(self,to_shearch):
        pass