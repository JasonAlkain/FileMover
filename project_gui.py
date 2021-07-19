
from tkinter import *
import tkinter as tk

import main
import project_func


def load_gui(self):
    #################################
    # Label Setup
    #################################
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
    # Submit Button Setup
    self.btn_submit = Button(self.master)
    self.btn_submit["text"] = 'Manual Check'
    self.btn_submit["width"] = 12
    self.btn_submit["height"] = 2
    self.btn_submit["command"] = lambda: project_func.submit(self)
    self.btn_submit["bg"] = '#65FF80'
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
    self.lbl_info.grid(row=0, column=0, columnspan=3,
                       padx=(20, 0), pady=(20, 0))

    self.lbl_display.grid(row=4, column=0, rowspan=3, columnspan=4,
                          padx=(20, 0), pady=(20, 0))
    #################################
    # Button placement
    #################################
    self.btn_submit.grid(
        row=7, column=0, padx=(20, 0), pady=(20, 0), sticky=NW)
    self.btn_close.grid(
        row=7, column=1, padx=(20, 0), pady=(20, 0), sticky=NW)


if __name__ == "__main__":
    pass
