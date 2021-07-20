from threading import Timer
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime

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
        self.master.geometry('{}x{}'.format(490, 380))
        self.master.config(bg='#303030')
        self.messagebox = messagebox
        self.master.protocol("WM_DELETE_WINDOW",
                             lambda: project_func.ask_quit(self))

        #################################
        # String Variable Setup
        #################################
        self.folderPath_A = StringVar()
        self.folderPath_B = StringVar()
        self.nextCheck = ''

        self.folderPath_A.set(value='')
        self.folderPath_B.set(value='')
        #################################
        # Function Starts
        #################################
        project_gui.load_gui(self)

    #This doesn't work for some reason...
    def startCheck(self):
        # get curent time
        self.curTime = datetime.today()
        # set next time
        self.nextTime = self.curTime.replace(second=self.curTime.second+5)
        # Get delta time
        delta_t = self.nextTime-self.curTime
        # prep interval
        secs = delta_t.seconds+1
        #
        self.ti = Timer(secs, project_func.folderCheck(self))
        # start the timer
        self.ti.start()


if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    app.mainloop()
