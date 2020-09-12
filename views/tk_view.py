import tkinter

class tk_view:
    def __init__(self):
        #------------------Creating-the-main-screen-----------------------------
        self.app = tkinter.Tk(screenName="main") #Making the main root
        self.app.geometry("300x200") # Setting the size of the main window
        self.app.title("Hymn") 
        self.app.iconbitmap("icons/icon.ico") #Setting the main left top icon
        #-----------------Populating-the-main-screen----------------------------
        #.........-Grid..................................
        self.music_grid= tkinter.Listbox(master=self.app)
        self.music_grid.grid(row=0,column=0)
        #..........Buttons...............................
        #..........Entry.................................
