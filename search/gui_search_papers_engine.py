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




path_to_save = '/Users/rodrigodutra/Desktop/python-script/search/history_strings_papers.txt'

#create gui elements
window = Tk()
window.resizable(False, False)
window.title("Search Engine v1.0")
window.geometry('810x415')
lbl_String = Label(window, text="String",font='Helvetica 14 bold')

#String Label
lbl_String.grid(column=0, row=0)
txt_String = Entry(window,width=80)

txt_String.grid(column=1, row=0)
txt_String.place(x=60,y=10,height=40)


lbl_String.place(x=10,y=20)

#Checkbox
chk_state_dblp = BooleanVar()
chk_state_dblp.set(True) #set check state

chk_state_pubmed = BooleanVar()
chk_state_pubmed.set(True) #set check state

chk_state_scopus = BooleanVar()
chk_state_scopus.set(True) #set check state

chk_state_scholar = BooleanVar()
chk_state_scholar.set(True) #set check state

chk = Checkbutton(window, text='DBLP', var=chk_state_dblp)
chk.place(x=30,y=65)
chk = Checkbutton(window, text='PUBMED', var=chk_state_pubmed)
chk.place(x=100,y=65)
chk = Checkbutton(window, text='SCOPUS', var=chk_state_scopus)
chk.place(x=190,y=65)
chk = Checkbutton(window, text='SCHOLAR', var=chk_state_scholar)
chk.place(x=290,y=65)

text = Text(window, height=20, width=110)
text.place(x=10,y=110)
scroll = Scrollbar(window, command=text.yview)
scroll.pack(side=RIGHT)
text.configure(yscrollcommand=scroll.set)


#clear screen log
def show_log():
    text.delete("1.0","end")
    arquivo = open(path_to_save,'r')
    text.insert(INSERT, arquivo.read())  
    

#return google link for search
def google_results(keyword):
    query = keyword
    google_url = "https://www.google.com/search?q=" + query
    return google_url


#open webpage link
def open_link(link): 
    webbrowser.open(link)

#convert the list of engines in string
def convert_list_to_string(engines):
    engines_string = ""
    for engine in engines:
        engines_string = engines_string + ','+ engine
    
    return engines_string


def save_changes():
    arquivo = open(path_to_save,'w')
    arquivo.write(text.get("1.0",END))
    
    text.delete("1.0","end")
    arquivo = open(path_to_save,'r')
    text.insert(INSERT, arquivo.read())  

#if drive upload button
def save_and_drive_upload():
    
    save_changes()
    
    gauth = GoogleAuth()           
    drive = GoogleDrive(gauth)   
    upload_file_list = [path_to_save]
    for upload_file in upload_file_list:
    	gfile = drive.CreateFile({'parents': [{'id': '1Kqbg1KNfA8s3UxHIoqZ2uH8tQP_aVd3z'}]})
    	# Read file and set it as the content of this instance.
    	gfile.SetContentFile(upload_file)
    	gfile.Upload() # Upload the file.
        
        
    alert_msg("Success Uploaded")
    


#if google button
def google_clicked():
    
    if(txt_String.get() == ''):
        tkinter.messagebox.showinfo(title=None, message="String is empty")
    
    else:
        
        link = google_results(str(txt_String.get()))
        open_link(link)
        
        date_ = datetime.datetime.now()

        arquivo = open(path_to_save,'a')
        arquivo.write(str(txt_String.get()) + "," + "GOOGLE" + ',' + str(date_) + "\n")
        arquivo.close()
        
        
        show_log()
        
      
def alert_msg(msg):
    tkinter.messagebox.showinfo(title=None, message=msg)
           
      
        
#if engine button
def engine_clicked():
    
    if(txt_String.get() == ''):
        alert_msg("String is empty")
    
    else:
        engines_names = []
        if(chk_state_dblp.get()):
            engines_names.append("DBLP")
            webbrowser.open("https://dblp.org/search?q=" + str(txt_String.get()))
        if(chk_state_pubmed.get()):
            engines_names.append("PUBMED")
            webbrowser.open("https://pubmed.ncbi.nlm.nih.gov/?term=" + str(txt_String.get()))
        if(chk_state_scopus.get()):
            engines_names.append("SCOPUS")
            #webbrowser.open("https://www.scopus.com/results/results.uri?src=s&sot=b&sdt=b&origin=searchbasic&rr=&sl=40&s=TITLE-ABS-KEY("+str(txt_String.get())+")&searchterm1=blockchain%20and%20healthcare&searchTerms=&connectors=&field1=TITLE_ABS_KEY&fields=")
            webbrowser.open("https://www.scopus.com/results/results.uri?src=s&sot=b&sdt=b&origin=searchbasic&rr=&sl=15&s=ALL("+str(txt_String.get())+")&searchterm1="+str(txt_String.get())+"&searchTerms=&connectors=&field1=ALL&fields=")
        if(chk_state_scholar.get()):
            engines_names.append("SCHOLAR")
            webbrowser.open("https://scholar.google.com/scholar?hl=pt-BR&as_sdt=0%2C5&q="+str(txt_String.get())+"&btnG=")    
    
        date_ = datetime.datetime.now()

        arquivo = open(path_to_save,'a')
        arquivo.write(str(txt_String.get()) + " " + convert_list_to_string(engines_names) + ',' + str(date_) + "\n")
        arquivo.close()
        
        
        show_log()
        
        
        

myFont = font.Font(size=15)

#btn elements
btn_engine = Button(window,text="Engine", command=engine_clicked)
btn_engine.config( height = 2, width = 9 )
btn_engine.place(x=400,y=56)
btn_engine.config(fg='black')
btn_engine['font'] = myFont

btn_google = Button(window, text="Google", command=google_clicked)
btn_google.config( height = 2, width = 9 )
btn_google.place(x=530,y=56)
btn_google.config(fg='blue')
btn_google['font'] = myFont


btn_drive = Button(window, text="Up. To Drive", command=save_and_drive_upload)
btn_drive.config( height = 2, width = 9 )
btn_drive.place(x=660,y=56)
btn_drive.config(fg='black')
btn_drive['font'] = myFont

btn_drive = Button(window, text="Save Changes", command=save_changes)
btn_drive.config( height = 1, width = 9 )
btn_drive.place(x=660,y=380)
btn_drive.config(fg='Black')
btn_drive['font'] = myFont




show_log()


window.mainloop()