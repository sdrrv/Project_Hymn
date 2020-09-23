import tkinter
from controllers.controller import controller
class tk_view:
    def __init__(self):
        #?-----------------------Data-Structors----------------------------------
        self.musics={}
        self.controller = controller()
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
        #..........Labels................................
        #?--------------------new_window--------------------------------------------
        self.new_window_music_input = None
        self.new_window_artist_input = None
        self.new_app = None
#!----------------------------------------------------------------------------------------------------------
    def update_grid(self):
        self.music_grid.delete(0,"end")
        tmp= [key for key in self.musics]
        for i in range(len(tmp)):
            self.music_grid.insert(i,tmp[i])

    def add_music(self,music,url):
        tmp= [key for key in self.musics]
        if not music in tmp:
            self.musics[music] = url
            self.update_grid()
        
    def submit_button_action(self):
        pass

    def add_music_button_action(self):
        self.create_choice_window()
    
    def delete_button_action(self):
        tmp= [key for key in self.musics]
        to_del= [tmp[i] for i in self.music_grid.curselection()]
        for i in to_del:
            self.musics.pop(i,None)
        self.update_grid()
    
    def create_choice_window(self):
        #?---------------------------------------------------------------------
        self.new_app = tkinter.Toplevel(self.app)
        self.new_app.geometry("300x100") # Setting the size of the main window
        self.new_app.title("Select") 
        self.new_app.iconbitmap("icons/icon.ico") #Setting the main left top icon
        #?---------------------------------------------------------------------
        self.new_window_music_input = tkinter.Entry(master=self.new_app)
        self.new_window_artist_input = tkinter.Entry(master=self.new_app)
        new_window_music_label = tkinter.Label(master= self.new_app, text="Music Name:")
        new_window_artist_label = tkinter.Label(master= self.new_app, text="Artist Name:")
        new_window_submit_button = tkinter.Button(master = self.new_app, text= "Submit", command =self.new_window_submit)
        new_window_music_label.grid(row=0,column=0)
        self.new_window_music_input.grid(row=1,column=0)

        new_window_artist_label.grid(row=0,column=2)
        self.new_window_artist_input.grid(row=1,column=2)

        new_window_submit_button.grid(row=4,column=1)

    def new_window_submit(self):
        music = self.new_window_music_input.get()
        artist = self.new_window_artist_input.get()
        self.add_music(music+" - "+artist,self.controller.shearch_youtube(music+" - "+artist) )
        self.new_app.destroy()
        self.new_app.update()
