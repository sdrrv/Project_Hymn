import tkinter

class tk_view:
    def __init__(self):
        #-----------------------Data-Structors----------------------------------
        self.musics=[]
        #------------------Creating-the-main-screen-----------------------------
        self.app = tkinter.Tk() #Making the main root
        self.app.geometry("500x500") # Setting the size of the main window
        self.app.title("Hymn") 
        self.app.iconbitmap("icons/icon.ico") #Setting the main left top icon
        #-----------------Populating-the-main-screen----------------------------
        #.........-Grid..................................
        self.music_grid= tkinter.Listbox(master=self.app)
        self.music_grid.grid(row=0,column=0)
        #..........Buttons...............................
        self.submit_button = tkinter.Button(master=self.app,command=self.submit_button_action)

        self.delete_button = tkinter.Button(master=self.app)

        self.add_music_button = tkinter.Button(master=self.app)

        #..........Entry.................................
        self.music_input= tkinter.Entry(master= self.app)
        
        #..........Labels................................

    def add_music(self,music):
        pass
    
    def submit_button_action(self):
        pass