#
import os
import time
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import webbrowser
import shutil
from datetime import datetime
from threading import Timer

#
import project_gui
import main


#
def center_window(self, w, h):  # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


#
def folderCheck(self):
    count = None
    path_A = self.folderPath_A.get()
    path_B = self.folderPath_B.get()
    # check if folders are populated
    if path_A != '' and path_B != '':
        self.lbl_info.config(
            text='Next Check: {}'.format(self.nextTime.time()))
        # Get files from folder A
        filesInDir = os.listdir(path_A)
        count = 0
        for file in filesInDir:
            count += 1
            # move the file
            shutil.move(
                '{}/{}'.format(path_A, file), path_B)

        self.lbl_display.config(text='Files moved: {}'.format(count))
    else:
        self.lbl_display.config(text='Folder A or B have not been selected')


#
def openFolder_A(self):
    path = filedialog.askdirectory()
    self.folderPath_A.set(value=path)
    if path != '':
        # get drive
        driveLetter = os.path.splitdrive(path)[0]
        # grab the last folder in the path
        folder = os.path.basename(path)
        self.lbl_fp_A.config(text='{}\\..\\{}'.format(driveLetter, folder))
        print(path)
    else:
        self.lbl_fp_A.config(text='!!Please Select a folder!!')


#
def openFolder_B(self):
    path = filedialog.askdirectory()
    self.folderPath_B.set(value=path)
    if path != '':
        # get drive
        driveLetter = os.path.splitdrive(path)[0]
        # grab the last folder in the path
        folder = os.path.basename(path)
        # update label
        self.lbl_fp_B.config(text='{}\\..\\{}'.format(driveLetter, folder))
        print(path)
    else:
        # if nothing was selectde let the user know
        self.lbl_fp_B.config(text='!!Please Select a folder!!')


#
def cancel(self):
    self.master.destroy()


# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if self.messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)


#
def openFile(fileName=''):
    data = ''
    if fileName != '':
        with open(fileName, 'r') as f:
            data = f.read()
            f.close()
    return data


if __name__ == "__main__":
    pass
