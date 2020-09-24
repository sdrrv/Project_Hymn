from models.chrome_web_driver import chr_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from models.musics import musics_model


class controller:
    def __init__(self):
        self.webdriver = chr_driver(True)
        self.musics = musics_model()

    def get_musics_model(self):
        return self.musics
    
    def get_musics_list(self):
        return [music for music in self.musics.get_musics()]

    def open(self,to_open):
        self.webdriver.get_driver().get(to_open)

    def shearch_youtube(self,to_shearch):
        self.open("https://www.youtube.com/results?search_query="+to_shearch)
        wait = WebDriverWait(self.webdriver.get_driver(), 3)
        presence = EC.presence_of_element_located
        visible = EC.visibility_of_element_located
        return self.webdriver.get_driver().find_element_by_id("video-title").get_attribute("href")
