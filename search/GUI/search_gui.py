#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 15:22:47 2021

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

from tkinter import *
import tkinter.messagebox

window = Tk()



window.title("Welcome to Search Engine")
window.geometry('550x100')
lbl_String = Label(window, text="String")
lbl_Number = Label(window, text="Number of Results")

lbl_String.grid(column=0, row=0)
lbl_Number.grid(column=0, row=1)

txt_String = Entry(window,width=50)
txt_Number = Entry(window,width=10)
txt_String.grid(column=1, row=0)
txt_Number.grid(column=1, row=1)

txt_Number.place(x=130,y=50)
lbl_Number.place(x=5,y=50)


txt_String.place(x=60,y=10)
lbl_String.place(x=5,y=10)


def google_results(keyword, n_results):
    query = keyword
    query = urllib.parse.quote_plus(query) # Format into URL encoding
    number_result = n_results
    ua = UserAgent()
    google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
    response = requests.get(google_url, {"User-Agent": ua.random})
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find_all('div', attrs = {'class': 'ZINbbc'})
    results=[re.search('\/url\?q\=(.*)\&sa',str(i.find('a', href = True)['href'])) for i in result if "url" in str(i)]
    links=[i.group(1) for i in results if i != None]
    return (links)



def open_links(links):
    for link in links:
        webbrowser.open(link)



def clicked_commands():
    tkinter.messagebox.showinfo(title=None, message='''intext:""\nintitle:""\nfiletype:"" ''')


def clicked():
    
    
    if(txt_Number.get() == '' or txt_String.get() == ''):
        tkinter.messagebox.showinfo(title=None, message="Fill in all fields")
    
    else:
    
        links = google_results(str(txt_String.get()), int(txt_Number.get()))
        arquivo = open('history.txt','a')
        arquivo.write(str(txt_String.get()) + "\n")
        
        open_links(links)




btn = Button(window, text="Engine", command=clicked)
btn.config( height = 2, width = 5 )
btn.place(x=250,y=45)



menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Commands',command=clicked_commands)
menu.add_cascade(label='Help', menu=new_item)
window.config(menu=menu)



window.mainloop()