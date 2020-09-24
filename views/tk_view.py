import tkinter
from controllers.controller import controller
class tk_view:
    def __init__(self):
        #?-----------------------Controller----------------------------------
        self.controller = controller()
        #?------------------Creating-the-main-screen-----------------------------
        self.app = tkinter.Tk() #Making the main root
        self.app.geometry("200x200") # Setting the size of the main window
        self.app.title("Hymn") 
        self.app.iconbitmap("icons/icon.ico") #Setting the main left top icon
        #?-----------------Populating-the-main-screen----------------------------
        #.........Grid..................................
        self.music_grid= tkinter.Listbox(master=self.app,selectmode="extended")
        self.music_grid.grid(row=0,column=0)
        #..........Buttons...............................
        self.submit_button = tkinter.Button(master=self.app,command=self.submit_button_action,text= "Submit")
        self.submit_button.grid(row=1,column=3)

        self.delete_button = tkinter.Button(master=self.app,text="Delete Music",command=self.delete_button_action)
        self.delete_button.grid(row=1,column=0)

        self.add_music_button = tkinter.Button(master=self.app,text="Add Music",command=self.add_music_button_action)
        self.add_music_button.grid(row=0,column=3)
        #..........Labels................................
        #?--------------------new_window--------------------------------------------
        self.new_window_music_input = None
        self.new_window_artist_input = None
        self.new_app = None
        self.new_window_submit_button = None
#!----------------------------------------------------------------------------------------------------------
    def update_grid(self):
        self.music_grid.delete(0,"end")
        tmp= self.controller.get_musics_model().get_musics_list()
        for i in range(len(tmp)):
            self.music_grid.insert(i,tmp[i])

    def add_music(self,music,url):
        tmp= self.controller.get_musics_list()
        if not music in tmp:
            self.controller.get_musics_model().add_music(music,url)
            self.update_grid()
        
    def submit_button_action(self):
        pass

    def add_music_button_action(self):
        self.create_choice_window()
    
    def delete_button_action(self):
        tmp= self.controller.get_musics_model().get_musics_list()
        to_del= [tmp[i] for i in self.music_grid.curselection()]
        for i in to_del:
            self.controller.get_musics_model().delete_music(i)
        self.update_grid()
    
    def create_choice_window(self):
        #?---------------------------------------------------------------------
        self.new_app = tkinter.Toplevel(self.app)
        self.new_app.bind("<Return>",self.new_window_submit) #Submit with the enter
        self.new_app.geometry("300x100") # Setting the size of the main window
        self.new_app.title("Select") 
        self.new_app.iconbitmap("icons/icon.ico") #Setting the main left top icon
        #?---------------------------------------------------------------------
        self.new_window_music_input = tkinter.Entry(master=self.new_app)
        self.new_window_artist_input = tkinter.Entry(master=self.new_app)
        new_window_music_label = tkinter.Label(master= self.new_app, text="Music Name:")
        new_window_artist_label = tkinter.Label(master= self.new_app, text="Artist Name:")
        self.new_window_submit_button = tkinter.Button(master = self.new_app, text= "Submit", command =self.new_window_submit)
        new_window_music_label.grid(row=0,column=0)
        self.new_window_music_input.grid(row=1,column=0)

        new_window_artist_label.grid(row=0,column=2)
        self.new_window_artist_input.grid(row=1,column=2)

        self.new_window_submit_button.grid(row=4,column=1)

    def new_window_submit(self,event=None):
        self.new_window_submit_button["state"]="disabled"
        music = self.new_window_music_input.get()
        artist = self.new_window_artist_input.get()
        self.add_music(music+" - "+artist,self.controller.shearch_youtube(music+" - "+artist) )
        self.new_app.destroy()
        self.new_app.update()
