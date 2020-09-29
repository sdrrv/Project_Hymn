
class musics_model:
    def __init__(self):
        self.musics={}
    
    def get_musics(self):
        return self.musics
    
    def add_music(self,music,url):
        self.musics[music] = url

    def delete_music(self,key):
        self.musics.pop(key,None)
    
    def get_url(self,music):
        return self.musics[music]
