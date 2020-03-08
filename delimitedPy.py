# Simple enough, just import everything from tkinter.
from tkinter import filedialog
from tkinter import *



# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()


        

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        self.lbl_csv_path = Label(self, text='Please choose an action.')
        self.lbl_csv_path.place(x=0,y=0)

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)


        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        

        file.add_command(label='Open CSV', command=self.get_csv)
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)

    
    def client_exit(self):
        exit()


    def update_lbl_csv_path(self, new_label_text):
        # @ToDo - Error Checking:
        # Make sure text is able to be displayed.
        # If text is the same, do not update.

        # @Options - Add:
        # .after to update self after period of time
        #   self.after(1000, self.update_lbl_csv_path)

        new_text = new_label_text
        self.lbl_csv_path.configure(text = new_text)

    # self made.
    def get_csv(self):
        # @ToDo - Error Checking:
        # Handle user not selecting a file.
        # Handle if the file is currently open by something else.

        # @INPUT
        # Dialog to ask the user for a file
        root.filename =  filedialog.askopenfilename(initialdir = './',title = "Select file",filetypes = (('text files','*.txt *.csv'),('all files','*.*')))
        
        # Updates label with path of selected file.
        self.update_lbl_csv_path(new_label_text=root.filename)


          

        
# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")




#creation of an instance
app = Window(root)



# Update the label a period of time
# root.after(1000, app.update_lbl_csv_path)




#mainloop 
root.mainloop()