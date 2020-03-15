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

        # NOTEBOOK
        self.notebook = Notebook(self)

        # FRAME - tabStart
        tabStart = tk.Frame(self.notebook)

        # BUTTON - btnSelectSource
        self.btnSelectSource = tk.Button(tabStart, text='Select Source', command=self.clicked_btnSelectSource)
        self.btnSelectSource.pack(side=tk.BOTTOM, fill=tk.X)

        # BUTTON - btnContinue
        self.btnContinue = tk.Button(tabStart, text='Continue', command=self.clicked_btnContinue)
        self.btnContinue.configure(state = 'disabled')
        # self.btnContinue.pack(side=tk.RIGHT, fill=tk.X)
        # self.btnContinue.pack(side=tk.RIGHT, fill=tk.NONE, expand=0)

        # STRINGVAR - varUserFile
        self.varUserFile = tk.StringVar(tabStart)
        self.varUserFile.set('Click the "Select Source" button below.')

        # LABEL - lblUserFilePath
        self.lblUserFilePath = tk.Label(tabStart, textvar=self.varUserFile, bg='lightgrey', fg='black')
        self.lblUserFilePath.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # ADD FRAMES to NOTEBOOK
        self.notebook.add(tabStart, text='Start Page')

        # PACK NOTEBOOK
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
    def clicked_btnSelectSource(self):
        # print('clicked_btnSelectSource')

        # Ask for delimited file.
        fileName =  filedialog.askopenfilename(initialdir = './',title = "Select a delimited file",filetypes = (('text files','*.txt *.csv'),('all files','*.*')))

        # Check that a file has been selected.
        
        # Update the StringVariable to update the label to be the path of the file.
        self.varUserFile.set(str(fileName))

        # Enable the Continue Button
        self.btnContinue.configure(state = 'active')
        self.btnContinue.pack(side=tk.RIGHT, fill=tk.X)
        self.notebook.pack(fill=tk.BOTH, expand=1)


    def clicked_btnContinue(self):
        pass
        print('clicked_btnContinue ran.')
        

    def copy_to_clipboard(self, text=None):
        print('copy_to_clipboard ran')
        # if not text:
        #     text = self.italian_translation.get()

        # self.clipboard_clear()
        # self.clipboard_append(text)
        # msg.showinfo('Copied Successfully', 'Text copied to clipboard')


if __name__ == '__main__':
    delimitedPy = DelimitedPy()
    delimitedPy.mainloop()