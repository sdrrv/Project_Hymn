import tkinter

class tk_view:
    def __init__(self):
        #?-----------------------Data-Structors----------------------------------
        self.musics=[]
        #?------------------Creating-the-main-screen-----------------------------
        self.app = tkinter.Tk() #Making the main root
        self.app.geometry("500x500") # Setting the size of the main window
        self.app.title("Hymn") 
        self.app.iconbitmap("icons/icon.ico") #Setting the main left top icon
        #?-----------------Populating-the-main-screen----------------------------
        #.........Grid..................................
        self.music_grid= tkinter.Listbox(master=self.app,selectmode="extended")
        self.music_grid.grid(row=0,column=0)
        #..........Buttons...............................
        self.submit_button = tkinter.Button(master=self.app,command=self.submit_button_action)

        self.delete_button = tkinter.Button(master=self.app,text="Delete",command=self.delete_button_action)
        self.delete_button.grid(row=3,column=0)

        self.add_music_button = tkinter.Button(master=self.app,text="Add",command=self.add_music_button_action)
        self.add_music_button.grid(row=1,column=1)

        #..........Entry.................................
        self.music_input= tkinter.Entry(master= self.app)
        self.music_input.grid(row=1,column=0)
        #..........Labels................................
        
#!----------------------------------------------------------------------------------------------------------
    def update_grid(self):
        self.music_grid.delete(0,"end")
        for i in range(len(self.musics)):
            self.music_grid.insert(i,self.musics[i])

    def add_music(self,music):
        if not music in self.musics:
            self.musics.append(music)
            self.update_grid()
        self.create_choice_window()
        
    def submit_button_action(self):
        pass

    def add_music_button_action(self):
        self.add_music(self.music_input.get())
        self.music_input.delete(0,len(self.music_input.get()))
    
    def delete_button_action(self):
        to_del= [self.musics[i] for i in self.music_grid.curselection()]
        for i in to_del:
            self.musics.remove(i)
        self.update_grid()
    
    def create_choice_window(self):
        #?---------------------------------------------------------------------
        new_app = tkinter.Toplevel(self.app)
        new_app.geometry("300x300") # Setting the size of the main window
        new_app.title("Select") 
        new_app.iconbitmap("icons/icon.ico") #Setting the main left top icon
        #?---------------------------------------------------------------------
        