import tkinter

class tk_view:
    def __init__(self):
        #------------------Seting-the-main-screen-------------------------------
        self.app = tkinter.Tk(screenName="main") #Making the main root
        self.app.geometry("300x200") # Setting the size of the main window
        self.app.title("Hymn") 
        self.app.iconbitmap("icons/icon.ico") #Setting the main left top icon
        #-----------------------------------------------------------------------

