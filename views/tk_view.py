import tkinter

class tk_view:
    def __init__(self):
        #------------------Seting-the-main-screen-------------------------------
        self.app = tkinter.Tk(screenName="main")
        self.app.geometry("300x200")
        self.app.title("Hymn")
        self.app.iconbitmap("icons/icon.ico")
        #-----------------------------------------------------------------------

