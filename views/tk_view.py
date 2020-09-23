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

        #..........Entry.................................
        self.music_input= tkinter.Entry(master= self.app)
        self.music_input.grid(row=1,column=0)
        #..........Labels................................     
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
        #print(self.create_choice_window(music))
        
    def submit_button_action(self):
        pass

    def add_music_button_action(self):
        self.add_music(self.music_input.get(),"google")
        self.music_input.delete(0,len(self.music_input.get()))
    
    def delete_button_action(self):
        to_del= [self.musics[i] for i in self.music_grid.curselection()]
        for i in to_del:
            self.musics.remove(i)
        self.update_grid()
    
    def create_choice_window(self,inputer):
        #?---------------------------------------------------------------------
        new_app = tkinter.Toplevel(self.app)
        new_app.geometry("300x100") # Setting the size of the main window
        new_app.title("Select") 
        new_app.iconbitmap("icons/icon.ico") #Setting the main left top icon
        #?---------------------------------------------------------------------
        new_window_submit_button = tkinter.Button(master = new_app, text= "Submit", command = self.add_music())
        new_window_music_input = tkinter.Entry(master=new_app)
        new_window_artist_input = tkinter.Entry(master=new_app)
        new_window_music_label = tkinter.Label(master= new_app, text="Music Name:")
        new_window_artist_label = tkinter.Label(master= new_app, text="Artist Name:")

        new_window_music_label.grid(row=0,column=0)
        new_window_music_input.grid(row=1,column=0)

        new_window_artist_label.grid(row=0,column=2)
        new_window_artist_input.grid(row=1,column=2)

        new_window_submit_button.grid(row=4,column=1)

        #return self.controller.shearch_youtube(inputer)
    