#
import os
import time
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import webbrowser
import shutil
from datetime import datetime

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
def submit(self):
    today = datetime.today()
    tomorow = today.replace(day=today.day+1)
    self.lbl_info.config(text='Next Check: {}'.format(tomorow))
    count = None
    # Get files from folder A
    filesInDir = os.listdir(self.folderPath_A)
    if filesInDir != '':
        count = 0
        for file in filesInDir:
            count += 1
            if self.manualCheck == True:
                if self.messagebox.askokcancel("Move File", 'Okay to move file "{}"?'.format(file)):
                    # move the file
                    shutil.move(
                        '{}/{}'.format(self.folderPath_A, file), self.folderPath_B)
            else:
                shutil.move('{}/{}'.format(self.folderPath_A, file),
                            self.folderPath_B)
    updateNotify(self, 'Files moved: {}'.format(count))


#
def openFolder_A(self):
    self.folder_A = filedialog.askdirectory()
    print(self.folder_A)
    self.lbl_folder_A.config(text='{}'.format(self.folder_A))

    pass


#
def openFolder_B(self):
    self.folder_B = filedialog.askdirectory()
    print(self.folder_B)
    self.lbl_folder_B.config(text='{}'.format(self.folder_B))
    pass


#
def updateNotify(self, text=''):
    self.lbl_display.config(text='{}'.format(text))
    # self.lbl_display.config(text='')


#
def cancel(self):
    self.master.destroy()


# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if self.messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)


def openFile(fileName=''):
    data = ''
    if fileName != '':
        with open(fileName, 'r') as f:
            data = f.read()
            f.close()
    return data


def body_html(self):
    _h1s = '\n\t\t<h1>{}</h1>'.format(self.header_html.get())
    _ps = '\n\t\t<p>{}</p>'.format(self.paragraph_html.get())
    section = '<div>{}{}\n\t</div>'.format(_h1s, _ps)
    return section


# Returns a template html document with the inner html
def htmlSetup(self):
    docType = '<!DOCTYPE html>'
    metaTags = ['<meta charset="UTF-8">', '<meta http-equiv="X-UA-Compatible" content="IE=edge">',
                '<meta name="viewport" content="width=device-width, initial-scale=1.0">']
    titleTag = '<title>PWPG</title>'
    headTag = '<head>\n\t{}\n\t{}\n\t{}\n\t{}\n</head>'.format(
        metaTags[0], metaTags[1], metaTags[2], titleTag)
    bodyTag = '<body style="text-align: center; padding: 0 20;">\n\t{}\n</body>'.format(
        body_html(self))
    htmlTag = '<html lang="en">\n{}\n{}\n</html>'.format(headTag, bodyTag)
    return '{}\n{}'.format(docType, htmlTag)


if __name__ == "__main__":
    pass
