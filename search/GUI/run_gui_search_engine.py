#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: rodrigodutra
"""
import requests,sys,webbrowser
#import pandas as pd
#import numpy as np
import urllib
from tkinter.filedialog import askopenfilename, asksaveasfilename

import tkinter as tk
#from fake_useragent import UserAgent
import requests
import re
from urllib.request import Request, urlopen
#from bs4 import BeautifulSoup
import datetime
from tkinter import *
from tkinter import scrolledtext  
import tkinter.messagebox
import tkinter.font as font
import time
#from pydrive.auth import GoogleAuth
#from pydrive.drive import GoogleDrive

import os

#change this
path_gui_directory = "./"




#create gui elements
window = Tk()
window.resizable(True, True)
window.title("Search Engine v1.0")
window.geometry('960x600')
lbl_String = Label(window, text="String",font='Consolas 10 bold')
lbl_String.grid(column=0, row=0)
lbl_String.place(x=10,y=20)

txt_String = Entry(window,width=80,font='Consolas 14')
txt_String.grid(column=1, row=0)
txt_String.place(x=60,y=10,height=40)








#Checkbox
chk_state_dblp = BooleanVar()
chk_state_dblp.set(False) #set check state

chk_state_pubmed = BooleanVar()
chk_state_pubmed.set(False) #set check state

chk_state_scopus = BooleanVar()
chk_state_scopus.set(False) #set check state

chk_state_scholar = BooleanVar()
chk_state_scholar.set(False) #set check state


chk_state_zlibgen = BooleanVar()
chk_state_zlibgen.set(False) #set check state


chk = Checkbutton(window, text='DBLP', var=chk_state_dblp)
chk.place(x=30,y=75)
chk = Checkbutton(window, text='PUBMED', var=chk_state_pubmed)
chk.place(x=100,y=75)
chk = Checkbutton(window, text='SCOPUS', var=chk_state_scopus)
chk.place(x=190,y=75)
chk = Checkbutton(window, text='SCHOLAR', var=chk_state_scholar)
chk.place(x=280,y=75)
chk = Checkbutton(window, text='ZLIBGEN', var=chk_state_zlibgen)
chk.place(x=380,y=75)




def track_change_to_text_to_dark(event):
    txt_edit.tag_add("here","1.0","end")
    txt_edit.tag_config("here", background="black", foreground="white",selectbackground="blue",selectforeground="yellow")

def track_change_to_text_to_light(event):
    txt_edit.tag_add("here","1.0","end")
    txt_edit.tag_config("here", background="white", foreground="black",selectbackground="cyan",selectforeground="yellow")

def track_change_to_text_to_blue(event):
    txt_edit.tag_add("here","1.0","end")
    txt_edit.tag_config("here", background="blue", foreground="white",selectbackground="black",selectforeground="yellow")





txt_edit=scrolledtext.ScrolledText(window,width=103, height=20, wrap=tk.WORD,font='Consolas 12')  
txt_edit.bind('<F1>', track_change_to_text_to_dark)
txt_edit.bind('<F2>', track_change_to_text_to_light)
txt_edit.bind('<F3>', track_change_to_text_to_blue)


txt_edit.place(x=10,y=135)





display_text = tk.StringVar()
lbl_String_Saving = Label(window,textvariable=display_text, text="...",font='Helvetica 14')
lbl_String_Saving.place(x=820,y=560)


display_text_file_size = tk.StringVar()
lbl_String_file_size = Label(window,textvariable=display_text_file_size, text="...",font='Helvetica 14')
lbl_String_file_size.place(x=18,y=105)


#autosaving

path_to_save_default = f"{path_gui_directory}/temp.txt"

global path_file_save_this
path_file_save_this = path_to_save_default


def clear_file(name):
    file_to_remove_path = f"{path_gui_directory}/{name}.txt"
    arquivo = open(file_to_remove_path,'w')
    arquivo.write("")
    arquivo.close()






def get_file_size(path):
    try:
        return os.path.getsize(path) 
    except:
        alert_msg("Fail to read file")


#clear screen log
def show_log():
    txt_edit.delete("1.0","end")
    arquivo = open(path_file_save_this,'r')
    txt_edit.insert(INSERT, arquivo.read())  


def open_temp_file():
    txt_edit.delete("1.0","end")
    arquivo = open("temp.txt",'r')
    txt_edit.insert(INSERT, arquivo.read())  
    

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


#save text (for auto saving)
def save_changes():

    try:
        with open(path_file_save_this, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
            
            return True
            
        
    except Exception as e:
        alert_msg(e)


    
    

"""
#if drive upload button
def drive_upload():
    
    path_to_save = open_file()
    
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
"""

def get_date_and_hour():
    date_ = datetime.datetime.now()
    hour_ = f"{date_.hour}:{date_.minute}:{date_.second}"
    date_ = str(date_.strftime("%d/%m/%Y"))

    return date_,hour_


#if google button
def google_clicked():
    
    if(txt_String.get() == ''):
        tkinter.messagebox.showinfo(title=None, message="String is empty")
    
    else:
        
        link = google_results(str(txt_String.get()))
        open_link(link)
        
        
        date_,hour_ = get_date_and_hour()


        print(path_file_save_this)
        arquivo = open(path_file_save_this,'a')
        arquivo.write(str(txt_String.get()) + " , " + "GOOGLE" + ', ' + date_ + ", "+ hour_ +'\n')
        arquivo.close()
            
        show_log()
        
#if engine button
def engine_clicked():
    
    if(txt_String.get() == ''):
        alert_msg("String is empty")
    
    else:
        engines_names = []
        if(chk_state_dblp.get()):
            engines_names.append(" DBLP")
            webbrowser.open("https://dblp.org/search?q=" + str(txt_String.get()))
        if(chk_state_pubmed.get()):
            engines_names.append(" PUBMED")
            webbrowser.open("https://pubmed.ncbi.nlm.nih.gov/?term=" + str(txt_String.get()))
        if(chk_state_scopus.get()):
            engines_names.append(" SCOPUS")
            #webbrowser.open("https://www.scopus.com/results/results.uri?src=s&sot=b&sdt=b&origin=searchbasic&rr=&sl=40&s=TITLE-ABS-KEY("+str(txt_String.get())+")&searchterm1=blockchain%20and%20healthcare&searchTerms=&connectors=&field1=TITLE_ABS_KEY&fields=")
            #webbrowser.open("https://www.scopus.com/results/results.uri?src=s&sot=b&sdt=b&origin=searchbasic&rr=&sl=15&s=TITLE-ABS-KEY("+str(txt_String.get())+")&searchterm1="+str(txt_String.get())+"&searchTerms=&connectors=&field1=ALL&fields=")
            webbrowser.open("https://www.scopus.com/results/results.uri?sid=7a0754416e07eadad037a624472287b7&src=s&sot=b&sdt=b&origin=searchbasic&rr=&sl=25&s=TITLE-ABS-KEY("+str(txt_String.get())+")&searchterm1="+str(txt_String.get())+"&searchTerms=&connectors=&field1=TITLE_ABS_KEY&fields=")      
        if(chk_state_scholar.get()):
            engines_names.append(" SCHOLAR")
            webbrowser.open("https://scholar.google.com/scholar?hl=pt-BR&as_sdt=0%2C5&q="+str(txt_String.get())+"&btnG=") 
        if(chk_state_zlibgen.get()):
            engines_names.append(" ZLIBGEN")
            webbrowser.open("https://br1lib.org/s/"+str(txt_String.get()))   
    
        date_,hour_ = get_date_and_hour()

        arquivo = open(path_file_save_this,'a')
        arquivo.write(str(txt_String.get()) + " " + convert_list_to_string(engines_names) + ', ' + date_ + ", "+ hour_ +'\n')
        arquivo.close()
        
        
        show_log()
                
        
        
      
def alert_msg(msg):
    tkinter.messagebox.showinfo(title="Alert", message=msg)
           
   
    
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    #for save this feature
    global path_file_save_this 
    path_file_save_this = filepath


    

    if not filepath:
        return 

    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor Engine - {filepath}")
    
    
    return True


def try_open_file():
    if(open_file()):
        pass 
    else:
        pass
        #global path_file_save_this
        #path_file_save_this = path_to_save_default
        #alert_msg("Fail to open. Opening default file ... ")
       # open_temp_file()
        



def try_save_file():
    if(save_file()):
        alert_msg("Success !")
    else:
        global path_file_save_this
        path_file_save_this = path_to_save_default


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    
    #for save this feature, store path of file
    global path_file_save_this 
    path_file_save_this = filepath
    
    
    if not filepath:
        return False


    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor Engine - {filepath}")
    
    return True
    
    
    
def new_file():
    txt_edit.delete("1.0","end") 
    if(save_file()):
        alert_msg("Success !")
    else:
      pass
        

    
            
   
count_char =0
old_count_char =0

def autosave():
    #print(path_file_save_this)
    display_text.set(" ")
    global count_char
    global old_count_char
    
   
    count_char = sum(len(x) for x in txt_edit.get(1.0, tk.END).split())
    #count_char  = len(txt_edit.get(1.0, tk.END))
    
    
    if(count_char != old_count_char):
        save_changes()
        display_text.set("Saving")
        #print("saved")
        old_count_char = count_char
    

    #file_size_updated = f"{get_file_size(path_file_save_this)} bytes | {count_char} chars"
    #display_text_file_size.set(file_size_updated)    
        
    time_in_s = 5
    time_to_auto_save_in_ms = time_in_s * 1000
    
    window.after(time_to_auto_save_in_ms, autosave) # time in milliseconds   
    
      



myFont = font.Font(size=8)

#btn elements

align_engine_google_drive_btn = 65
btn_engine = Button(window,text="Engine", command=engine_clicked)
btn_engine.config( height = 2, width = 12 )
btn_engine.place(x=490,y=align_engine_google_drive_btn)
btn_engine.config(fg='black')
btn_engine['font'] = myFont

btn_google = Button(window, text="Google", command=google_clicked)
btn_google.config( height = 2, width = 12 )
btn_google.place(x=590,y=align_engine_google_drive_btn)
btn_google.config(fg='blue')
btn_google['font'] = myFont


"""
btn_drive = Button(window, text="Up. To Drive", command=drive_upload)
btn_drive.config( height = 2, width = 9 )
btn_drive.place(x=690,y=align_engine_google_drive_btn)
btn_drive.config(fg='black')
btn_drive['font'] = myFont
"""


#btn_save = Button(window, text="Save Changes", command=save_changes)
#btn_save.config( height = 1, width = 9 )
#btn_save.place(x=660,y=380)
#btn_save.config(fg='Black')
#btn_save['font'] = myFont



new_save_open_btn_y= 530

btn_new = Button(window, text="New", command=new_file)
btn_new.config( height = 2, width = 12, padx= 20)
btn_new.place(x=15,y=new_save_open_btn_y)
btn_new.config(fg='Black')
btn_new['font'] = myFont

btn_open = Button(window, text="Open", command=try_open_file)
btn_open.config( height = 2, width = 12,padx=20 )
btn_open.place(x=150,y=new_save_open_btn_y)
btn_open.config(fg='Black')
btn_open['font'] = myFont

btn_save_as = Button(window, text="Save as...", command=try_save_file)
btn_save_as.config( height = 2, width = 12,padx=20 )
btn_save_as.place(x=290,y=new_save_open_btn_y)
btn_save_as.config(fg='Black')
btn_save_as['font'] = myFont



#show_log()
#clear_file("blank_file")
open_temp_file()

autosave() 
window.mainloop()