#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: rodrigodutra
"""
import requests,sys,webbrowser
#import pandas as pd
#import numpy as np
import urllib
#from fake_useragent import UserAgent
import requests
import re
from urllib.request import Request, urlopen
#from bs4 import BeautifulSoup
import datetime
from tkinter import *

import tkinter.messagebox
import tkinter.font as font

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive




path_to_save = '/Users/rodrigodutra/Desktop/python-script/search/my_notes.txt'

#create gui elements
window = Tk()
window.resizable(False, False)
window.title("Notes Engine v1.0")
window.geometry('810x500')

lbl_String = Label(window, text="My Notes",font='Helvetica 14')
lbl_String.grid(column=0, row=0)
lbl_String.place(x=10,y=10)



text = Text(window, height=21, width=85,font='Helvetica 16')
text.place(x=10,y=34)
scroll = Scrollbar(window, command=text.yview)
scroll.pack(side=RIGHT)
text.configure(yscrollcommand=scroll.set)


#clear screen log
def show_log():
    text.delete("1.0","end")
    arquivo = open(path_to_save,'r')
    text.insert(INSERT, arquivo.read())  
    

      
def alert_msg(msg):
    tkinter.messagebox.showinfo(title=None, message=msg)



def save_changes(show_Msg=True):
    try:
        arquivo = open(path_to_save,'w')
        arquivo.write(text.get("1.0",END))

        text.delete("1.0","end")
        arquivo = open(path_to_save,'r')
        text.insert(INSERT, arquivo.read())  
        if(show_Msg):
            alert_msg("Success !")
    except:
        alert_msg("Fail !")
    
    
    

#if drive upload button
def save_and_drive_upload():
    
    save_changes(False)
    
    try:
        gauth = GoogleAuth()           
        drive = GoogleDrive(gauth)   
        upload_file_list = [path_to_save]
        
        for upload_file in upload_file_list:
            
        	gfile = drive.CreateFile({'parents': [{'id': '1XoutccDFglVRay4Nfvc-qDjBHDm3VIHi'}]})
        	# Read file and set it as the content of this instance.
        	gfile.SetContentFile(upload_file)
        	gfile.Upload() # Upload the file.
            
        alert_msg("Success !")    
        
        
    except:
        
        alert_msg("Fail !")



myFont = font.Font(size=15)

btn_drive = Button(window, text="Up. To Drive", command=save_and_drive_upload)
btn_drive.config( height = 2, width = 9 )
btn_drive.place(x=648,y=445)
btn_drive.config(fg='black')
btn_drive['font'] = myFont

btn_save = Button(window, text="Save", command=save_changes)
btn_save.config( height = 2, width = 9 )
btn_save.place(x=510,y=445)
btn_save.config(fg='Black')
btn_save['font'] = myFont




show_log()


window.mainloop()