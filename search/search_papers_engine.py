#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: rodrigodutra
"""
import requests,sys,webbrowser,bs4
import pandas as pd
import numpy as np
import urllib
from fake_useragent import UserAgent
import requests
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import datetime
from tkinter import *
import tkinter.messagebox

window = Tk()



window.title("Welcome to Search Store Engine")
window.geometry('550x100')
lbl_String = Label(window, text="String")


lbl_String.grid(column=0, row=0)
txt_String = Entry(window,width=50)

txt_String.grid(column=1, row=0)

txt_String.place(x=60,y=10)
lbl_String.place(x=5,y=10)


chk_state_dblp = BooleanVar()
chk_state_dblp.set(True) #set check state

chk_state_pubmed = BooleanVar()
chk_state_pubmed.set(True) #set check state

chk_state_scopus = BooleanVar()
chk_state_scopus.set(True) #set check state


chk_state_scholar = BooleanVar()
chk_state_scholar.set(True) #set check state

chk = Checkbutton(window, text='DBLP', var=chk_state_dblp)
chk.place(x=30,y=50)
chk = Checkbutton(window, text='PUBMED', var=chk_state_pubmed)
chk.place(x=100,y=50)
chk = Checkbutton(window, text='SCOPUS', var=chk_state_scopus)
chk.place(x=190,y=50)
chk = Checkbutton(window, text='SCHOLAR', var=chk_state_scholar)
chk.place(x=290,y=50)



def query_dblp(query):
    query = urllib.parse.quote_plus(query) # Format into URL encoding
    ua = UserAgent()
    dblp_link = "https://dblp.org/search?q=" + query
    response = requests.get(dblp_link, {"User-Agent": ua.random})
    soup = BeautifulSoup(response.text, "html.parser")

    return dblp_link



def open_links(links):
    for link in links:
        webbrowser.open(link)





def convert_list_to_string(engines):
    engines_string = ""
    for engine in engines:
        engines_string = engines_string + ','+ engine
    
    return engines_string

def clicked():
    
    
    if(txt_String.get() == ''):
        tkinter.messagebox.showinfo(title=None, message="String is empty")
    
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
            webbrowser.open("https://www.scopus.com/results/results.uri?src=s&sot=b&sdt=b&origin=searchbasic&rr=&sl=40&s=TITLE-ABS-KEY("+str(txt_String.get())+")&searchterm1=blockchain%20and%20healthcare&searchTerms=&connectors=&field1=TITLE_ABS_KEY&fields=")
        if(chk_state_scholar.get()):
            engines_names.append("SCHOLAR")
            webbrowser.open("https://scholar.google.com/scholar?hl=pt-BR&as_sdt=0%2C5&q="+str(txt_String.get())+"&btnG=")    
    
        date_ = datetime.datetime.now()

        arquivo = open('history_strings_papers.txt','a')
        arquivo.write(str(txt_String.get()) + " " + convert_list_to_string(engines_names) + ',' + str(date_) + "\n")
        
        
        
        
       


btn = Button(window, text="Engine", command=clicked)
btn.config( height = 2, width = 5 )
btn.place(x=400,y=40)
btn.config(fg='green')





window.mainloop()