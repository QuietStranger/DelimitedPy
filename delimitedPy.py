import tkinter as tk
from tkinter import messagebox as msg
from tkinter.ttk import Notebook
from tkinter import filedialog

import requests

appVersion = '0.1'

class DelimitedPy(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('DelimitedPy v{appVersion}'.format(appVersion=appVersion))
        self.geometry('500x500')

        self.notebook = Notebook(self)

        selectSourceTab = tk.Frame(self.notebook)
        italian_tab = tk.Frame(self.notebook)

        self.selectSourceButton = tk.Button(selectSourceTab, text='Select Source', command=self.select_source_command)
        self.selectSourceButton.pack(side=tk.BOTTOM, fill=tk.X)

        self.english_entry = tk.Text(selectSourceTab, bg='white', fg='black')
        self.english_entry.pack(side=tk.TOP, expand=1)

        self.italian_copy_button = tk.Button(italian_tab, text='Copy to Clipboard', command=self.copy_to_clipboard)
        self.italian_copy_button.pack(side=tk.BOTTOM, fill=tk.X)

        # self.italian_translation = tk.StringVar(italian_tab)
        # self.italian_translation.set('')
        self.userInputFile = tk.StringVar(selectSourceTab)
        self.userInputFile.set('')

        # self.italian_label = tk.Label(italian_tab, textvar=self.italian_translation, bg='lightgrey', fg='black')
        # self.italian_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.userInputFileLabel = tk.Label(selectSourceTab, textvar=self.userInputFile, bg='lightgrey', fg='black')
        self.userInputFileLabel.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


        self.notebook.add(selectSourceTab, text='Select Source')
        self.notebook.add(italian_tab, text='Italian')

        self.notebook.pack(fill=tk.BOTH, expand=1)

    # def translate(self, target_language='it', text=None):
        # if not text:
        #     text = self.english_entry.get(1.0, tk.END)

        # url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}'.format('en', target_language, text)

        # try:
        #     r = requests.get(url)
        #     r.raise_for_status()
        #     translation = r.json()[0][0][0]
        #     self.italian_translation.set(translation)
        #     msg.showinfo('Translation Successful', 'Text successfully translated')
        # except Exception as e:
        #     msg.showerror('Translation Failed', str(e))
    def select_source_command(self):
        # print('test')

        # @INPUT
        # Dialog to ask the user for a file
        fileName =  filedialog.askopenfilename(initialdir = './',title = "Select file",filetypes = (('text files','*.txt *.csv'),('all files','*.*')))

        # Updates label with path of selected file.
        # self.update_lbl_csv_path(new_label_text=root.filename)
        self.userInputFile.set(fileName)

        # filenameEdits = str(root.filename)
        # Custom_Methods.duplicate_csv_file(source_csv = root.filename)

    def copy_to_clipboard(self, text=None):
        if not text:
            text = self.italian_translation.get()

        self.clipboard_clear()
        self.clipboard_append(text)
        msg.showinfo('Copied Successfully', 'Text copied to clipboard')


if __name__ == '__main__':
    delimitedPy = DelimitedPy()
    delimitedPy.mainloop()






############### OLD CODE BELOW #####################################

# # Simple enough, just import everything from tkinter.
# from tkinter import filedialog
# from tkinter import *

# # Custom set of methods used for creating, this is mainly to control what is going on behind the scenes
# import Custom_Methods



# # Here, we are creating our class, Window, and inheriting from the Frame
# # class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
# class Window(Frame):

#     # Define settings upon initialization. Here you can specify
#     def __init__(self, master=None):
        
#         # parameters that you want to send through the Frame class. 
#         Frame.__init__(self, master)   

#         #reference to the master widget, which is the tk window                 
#         self.master = master

#         #with that, we want to then run init_window, which doesn't yet exist
#         self.init_window()


        

#     #Creation of init_window
#     def init_window(self):

#         # changing the title of our master widget      
#         self.master.title("GUI")

#         self.lbl_csv_path = Label(self, text='Please choose an action.')
#         self.lbl_csv_path.place(x=0,y=0)

#         # allowing the widget to take the full space of the root window
#         self.pack(fill=BOTH, expand=1)


#         # creating a menu instance
#         menu = Menu(self.master)
#         self.master.config(menu=menu)

#         # create the file object)
#         file = Menu(menu)

#         # adds a command to the menu option, calling it exit, and the
        

#         file.add_command(label='Open CSV', command=self.get_csv)
#         # command it runs on event is client_exit
#         file.add_command(label="Exit", command=self.client_exit)

        

#         #added "file" to our menu
#         menu.add_cascade(label="File", menu=file)

#         # create the file object)
#         edit = Menu(menu)

#         # adds a command to the menu option, calling it exit, and the
#         # command it runs on event is client_exit
#         edit.add_command(label="Undo")

#         #added "file" to our menu
#         menu.add_cascade(label="Edit", menu=edit)

    
#     def client_exit(self):
#         exit()


#     def update_lbl_csv_path(self, new_label_text):
#         # @ToDo - Error Checking:
#         # Make sure text is able to be displayed.
#         # If text is the same, do not update.

#         # @Options - Add:
#         # .after to update self after period of time
#         #   self.after(1000, self.update_lbl_csv_path)

#         new_text = new_label_text
#         self.lbl_csv_path.configure(text = new_text)

#     # self made.
#     def get_csv(self):
#         # @ToDo - Error Checking:
#         # Handle user not selecting a file.
#         # Handle if the file is currently open by something else.

#         # @INPUT
#         # Dialog to ask the user for a file
#         root.filename =  filedialog.askopenfilename(initialdir = './',title = "Select file",filetypes = (('text files','*.txt *.csv'),('all files','*.*')))
        
#         # Updates label with path of selected file.
#         self.update_lbl_csv_path(new_label_text=root.filename)

#         # @VALIDATION
#         # @ToDo - Handle user not selecting a file.
        
#         # Create new input box to allow for user to input output file name


#         # @ToDo - Create a button to click after passing validation, to then change below to become a button to copy.
#         # Method to create duplicate as a test

#         # filenameEdits = str(root.filename)
#         Custom_Methods.duplicate_csv_file(source_csv = root.filename)


          

        
# # root window created. Here, that would be the only window, but
# # you can later have windows within windows.
# root = Tk()

# # Initial size of the Tkinter application window dimentions.
# root.geometry("400x300")


# # Creation of an instance
# app = Window(root)

# # Update the label a period of time
# # root.after(1000, app.update_lbl_csv_path)



# # Last line to add last minute things to run before the Tkinter application starts up.
# # print('A test message perhaps? This will be run right before the Tkinter application launches.')

# # Custom_Methods.duplicate_csv_file()





# #mainloop
# # Everthing that happens before this look will be contained within the Tkinter application.
# # Everything after this will run once the Tkinter application is closed by close() or user clicks to close the window.
# root.mainloop()

# # Application is only Tkinter UI based and so probably not going to have code after this line unless expanded uppon later.