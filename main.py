import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from threading import Timer

import project_gui
import project_func


class Application(Frame):
    def __init__(self, master=None):
        #################################
        # Super init()
        #################################
        super().__init__(master)
        #################################
        # Master setup
        #################################
        self.master = master
        self.master.title('File Mover!')

        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(490, 280))
        self.master.config(bg='#303030')
        self.messagebox = messagebox
        self.master.protocol("WM_DELETE_WINDOW",
                             lambda: project_func.ask_quit(self))

        #################################
        # String Variable Setup
        #################################
        self.folderPath_A = 'E:\\Schools\\The Tech Academy\\the-tech-academy-repos\\FileMover\\Folder_A'
        self.folderPath_B = 'E:\\Schools\\The Tech Academy\\the-tech-academy-repos\\FileMover\\Folder_B'
        self.nextCheck = ''
        #################################
        # Function Starts
        #################################
        project_gui.load_gui(self)
        self.startCheck()

    def startCheck(self):
        project_func.submit(self)
        today = datetime.today()
        tomorow = today.replace(day=today.day+1)
        delta_t = tomorow-today
        secs = delta_t.seconds+1

        t = Timer(secs, project_func.submit(self))
        t.start()


if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    app.mainloop()
