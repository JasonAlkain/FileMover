
from tkinter import *
import tkinter as tk

import main
import project_func


def load_gui(self):
    #################################
    # Label Setup
    #################################
    # Folder path A Label
    # initial text setup
    path = 'None' if self.folderPath_A.get() == '' else self.folderPath_A.get()
    self.lbl_fp_A = Label(self.master, text=path)
    self.lbl_fp_A["font"] = ('Arial', 16)
    self.lbl_fp_A["fg"] = 'whitesmoke'
    self.lbl_fp_A["bg"] = '#505050'
    self.lbl_fp_A["height"] = 1
    self.lbl_fp_A["width"] = 27
    # Folder path A Label
    # initial text setup
    path = 'None' if self.folderPath_B.get() == '' else self.folderPath_B.get()
    self.lbl_fp_B = Label(self.master, text=path)
    self.lbl_fp_B["font"] = ('Arial', 16)
    self.lbl_fp_B["fg"] = 'whitesmoke'
    self.lbl_fp_B["bg"] = '#505050'
    self.lbl_fp_B["height"] = 1
    self.lbl_fp_B["width"] = 27
    # Info Label
    self.lbl_info = Label(
        self.master, text='Next Check:')
    self.lbl_info["font"] = ('Arial', 16)
    self.lbl_info["fg"] = 'whitesmoke'
    self.lbl_info["bg"] = '#303030'
    # Notification
    self.lbl_display = Label(self.master, text='Notification Area')
    self.lbl_display["font"] = ('Arial', 12)
    self.lbl_display["bg"] = '#666'
    self.lbl_display["fg"] = 'whitesmoke'
    self.lbl_display["height"] = 4
    self.lbl_display["width"] = 50
    #################################
    # Button Setup
    #################################
    # folder A select Button Setup
    self.btn_folderA_select = Button(self.master)
    self.btn_folderA_select["text"] = 'Select Folder A'
    self.btn_folderA_select["width"] = 14
    self.btn_folderA_select["height"] = 2
    self.btn_folderA_select["command"] = lambda: project_func.openFolder_A(
        self)
    self.btn_folderA_select["bg"] = '#65FF80'
    # folder B select Button Setup
    self.btn_folderB_select = Button(self.master)
    self.btn_folderB_select["text"] = 'Select Folder B'
    self.btn_folderB_select["width"] = 14
    self.btn_folderB_select["height"] = 2
    self.btn_folderB_select["command"] = lambda: project_func.openFolder_B(
        self)
    self.btn_folderB_select["bg"] = '#65FF80'
    # Start Button Setup
    self.btn_start = Button(self.master)
    self.btn_start["text"] = 'Start Check'
    self.btn_start["width"] = 12
    self.btn_start["height"] = 2
    self.btn_start["bg"] = '#050F10'
    # This does not work...
    #self.btn_start["command"] = lambda: self.startCheck()
    # Submit Button Setup
    self.btn_submit = Button(self.master)
    self.btn_submit["text"] = 'Manual Check'
    self.btn_submit["width"] = 12
    self.btn_submit["height"] = 2
    self.btn_submit["command"] = lambda: project_func.folderCheck(self)
    self.btn_submit["bg"] = '#6580FF'
    # Close Button Setup
    self.btn_close = Button(self.master)
    self.btn_close["text"] = 'Close'
    self.btn_close["width"] = 10
    self.btn_close["height"] = 2
    self.btn_close["command"] = lambda: project_func.ask_quit(self)
    self.btn_close["bg"] = '#FF8090'

    #################################
    # label placement
    #################################
    self.lbl_fp_A.grid(row=1, column=0, columnspan=4,
                       padx=(145, 0), pady=(10, 0), sticky=W)
    self.lbl_fp_B.grid(row=2, column=0, columnspan=4,
                       padx=(145, 0), pady=(10, 0), sticky=W)
    # top info bar
    self.lbl_info.grid(row=0, column=0, columnspan=4, sticky=N+W,
                       padx=(20, 20), pady=(20, 0))
    # Notification
    self.lbl_display.grid(row=4, column=0, rowspan=3, columnspan=4,
                          padx=(20, 20), pady=(20, 20))
    #################################
    # Button placement
    #################################
    self.btn_folderA_select.grid(
        row=1, column=0, columnspan=1, padx=(20, 0), pady=(10, 0), sticky=N+W)
    self.btn_folderB_select.grid(
        row=2, column=0, columnspan=1, padx=(20, 0), pady=(10, 0), sticky=N+W)
    # buttom buttons
    self.btn_submit.grid(
        row=7, column=0, padx=(20, 0), pady=(20, 0), sticky=N+W)
    self.btn_start.grid(
        row=7, column=1, padx=(20, 0), pady=(20, 0), sticky=N+W)
    self.btn_close.grid(
        row=7, column=2, padx=(20, 0), pady=(20, 0), sticky=N+E)


if __name__ == "__main__":
    pass
