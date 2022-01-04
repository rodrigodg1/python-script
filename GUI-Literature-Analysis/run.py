# -*- coding: UTF-8 -*-

from typing import cast
import codecs
import os
import json
from tkinter import filedialog
from datetime import date

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

from tkinter import messagebox
from tkinter.messagebox import askyesno
import time
from tkinter import *
from tkinter import simpledialog
from tkinter import scrolledtext


def get_date():
    today = date.today()
    today_formated_br = f"{today.day}/{today.month}/{today.year}"
    return today_formated_br


def get_line_count(filename):
    file = open(filename, "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    return line_count


def msg_inicial():
    lbl_scopus_file_atual.set("Resultados SCOPUS não carregados")
    lbl_google_file_atual.set("Resultados SCHOLAR não carregados")
    lbl_dblp_file_atual.set("Resultados DBLP não carregados")


    color_google = "tomato"
    color_scopus = "tomato"
    color_dblp = "tomato"


    lbl_google = tk.Label(fr_buttons,bg=color_google, textvariable=lbl_google_file_atual)
    lbl_google.grid(row=6, column=0, sticky="ew", padx=5,pady=5)

    lbl_scopus = tk.Label(fr_buttons,bg=color_scopus, textvariable=lbl_scopus_file_atual)
    lbl_scopus.grid(row=7, column=0, sticky="ew", padx=5,pady=5)

    lbl_dblp = tk.Label(fr_buttons,bg=color_dblp, textvariable=lbl_dblp_file_atual)
    lbl_dblp.grid(row=8, column=0, sticky="ew", padx=5,pady=5)

   



def reset_results():
    try:
        os.system('rm -rf results_from_dblp.txt')
        os.system('rm -rf results_from_google.txt')
        os.system('rm -rf results_from_scopus.txt')
        os.system('rm -rf results_from_all_engines.txt')
        messagebox.showinfo("Sucesso", "Resultados removidos com sucesso !")
    except Exception as e:
        messagebox.showerror("Erro", e)

# click event handler
def confirm():
    answer = askyesno(title='Confirmation',
                    message='Você tem certeza que deseja apagar todos os resultados?')
    if answer:
        clear_screen()
        msg_inicial()




def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("json", "*.json"), ("All Files", "*.*")]
    )
    if not filepath:
        return False
    #txt_edit.delete(1.0, tk.END)

    '''
    with open(filepath, "rb") as input_file:
        text = input_file.read()

    return text
    '''

    return filepath



def write_result_in_screen(filename,source,extract_info):
    #results_from_dblp.txt

    date = get_date()


    textfile = open(f"{filename}", "a")
   #textfile.write(search_term)
    #textfile.write("\n")

    list_string_title_year = extract_info
    for paper in list_string_title_year:
        textfile.write(paper + "; " + source + "; " + date + "\n")
    textfile.close()



    #total file 
    '''
    textfile = open("results_from_all_engines.txt", "a")
   #textfile.write(search_term)
    #textfile.write("\n")

    list_string_title_year = extract_info
    for paper in list_string_title_year:
        textfile.write(paper + "; " + source + "; " + date + "\n")
    textfile.close()


    print(get_line_count("results_from_all_engines.txt"))
    '''

    with open(f"{filename}", "r") as input_file:
        text = input_file.read()
    
    return text


    

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor Application - {filepath}")


def clear_screen():
     txt_edit.delete(1.0, tk.END)   
     reset_results()



def extract_dblp_step_1():
    try:
        data_path = open_file()
        f = open(data_path)
    
        # returns JSON object as
        # a dictionary
        data = json.load(f)
        # Closing file
        f.close()


        result = data['result']
        hits = result['hits']
        hit = hits['hit']
        titles_list = []
        years_list = []
        doi_list = []
        list_string_title_year = []
        for i in hit:
            title = i['info']['title']
            year = i['info']['year']
            doi = i['info']['ee']
            #print(title,year)
            titles_list.append(title)
            years_list.append(year)
            doi_list.append(doi)
            title_year = f"{title}; {year}; {doi}"
            list_string_title_year.append(title_year)

        text = write_result_in_screen("results_from_dblp.txt","DBLP",list_string_title_year)

            #txt_edit.delete(1.0, tk.END)

        txt_edit.insert(tk.END, text)

        messagebox.showinfo("Sucesso", "Dados extraidos com sucesso !")


        lbl_dblp_file_atual.set("Resultados DBLP Carregados")
        color_dblp = "light green"
        lbl_dblp = tk.Label(fr_buttons,bg=color_dblp, textvariable=lbl_dblp_file_atual)
        lbl_dblp.grid(row=8, column=0, sticky="ew", padx=5,pady=5)

    except Exception as e:
        messagebox.showerror("Erro", e)



def extract_google_step_1():
    try:
        
        file_path_results_from_google = open_file()
        if(file_path_results_from_google):
            data = json.load(codecs.open(file_path_results_from_google, 'r', 'utf-8-sig'))


            list_string_title_year = []

            #extract data from dict
            for i in data:
                title = i['title']
                year = i['year']

                if "article_url" in i: 
                    url_ = i['article_url']
                else:
                    url_ = "null"


                title_year_url = f"{title}; {year}; {url_}"
                list_string_title_year.append(title_year_url)


            text = write_result_in_screen("results_from_google.txt","SCHOLAR",list_string_title_year)

            #txt_edit.delete(1.0, tk.END)

            txt_edit.insert(tk.END, text)

            messagebox.showinfo("Sucesso", "Dados extraidos com sucesso !")


            lbl_google_file_atual.set("Resultados SCHOLAR Carregados")
            color_google = "light green"
            lbl_google = tk.Label(fr_buttons,bg=color_google, textvariable=lbl_google_file_atual)
            lbl_google.grid(row=6, column=0, sticky="ew", padx=5,pady=5)
           
    except Exception as e:
        messagebox.showerror("Erro",e)
        #messagebox.showerror("Descriptografar", "Chave Privada Não Carregada !")


def extract_scopus_step_1():
    try:
        
        file_path_results_from_scopus= open_file()
        if(file_path_results_from_scopus):
            data = json.load(codecs.open(file_path_results_from_scopus, 'r', 'utf-8-sig'))


            list_string_title_year = []

            #extract data from dict
            for i in data:
                title = i['title']
                year = i['year']

                if "article_url" in i: 
                    url_ = i['article_url']
                else:
                    url_ = "null"


                title_year_url = f"{title}; {year}; {url_}"
                list_string_title_year.append(title_year_url)


            text = write_result_in_screen("results_from_scopus.txt","SCOPUS",list_string_title_year)

            #txt_edit.delete(1.0, tk.END)
            txt_edit.insert(tk.END, text)

            messagebox.showinfo("Sucesso", "Dados extraidos com sucesso !")

            lbl_scopus_file_atual.set("Resultados SCOPUS Carregados")
            color_scopus = "light green"
            lbl_scopus = tk.Label(fr_buttons,bg=color_scopus, textvariable=lbl_scopus_file_atual)
            lbl_scopus.grid(row=7, column=0, sticky="ew", padx=5,pady=5)
        
    except Exception as e:
        messagebox.showerror("Erro",e)
        #messagebox.showerror("Descriptografar", "Chave Privada Não Carregada !")







def size_12():
   txt_edit.config(font=('Helvetica',12))

def size_20():
   txt_edit.config(font=('Helvetica',20))



window = tk.Tk()
window.title("Text Editor Application")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


lbl_scopus_file_atual = StringVar()
lbl_google_file_atual = StringVar()
lbl_dblp_file_atual = StringVar()


global color_google
global color_scopus
global color_dblp

color_google = "tomato"
color_scopus = "tomato"
color_dblp = "tomato"



#txt_edit = tk.Text(window)
txt_edit = scrolledtext.ScrolledText(window)

fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)


msg_inicial()


#btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...",height=2, width=21 ,command=save_file)
#btn_clear = tk.Button(fr_buttons, text="Clear Results...",height=2, width=21, command=clear_screen)
btn_clear= tk.Button(fr_buttons,text='Clear Results',height=2, width=21,command=confirm)

btn_google = tk.Button(fr_buttons, text="Load SCHOLAR Results...",height=2, width=21, command=extract_google_step_1)
btn_scopus = tk.Button(fr_buttons, text="Load SCOPUS Results...",height=2, width=21, command=extract_scopus_step_1)
btn_dblp = tk.Button(fr_buttons, text="Load DBLP Results...",height=2, width=21, command=extract_dblp_step_1)



#btn_create_key_pair = tk.Button(fr_buttons, text="Criar par de chaves ...", height=2, width=21, command=create_key_pair)

lbl_font_size = tk.Label(fr_buttons, text="Font Size:")
lbl_google= tk.Label(fr_buttons,bg=color_google, textvariable=lbl_google_file_atual)
lbl_scopus = tk.Label(fr_buttons,bg=color_scopus, textvariable=lbl_scopus_file_atual)
lbl_dblp = tk.Label(fr_buttons,bg=color_scopus, textvariable=lbl_dblp_file_atual)


button_size_12= Button(fr_buttons, text="12", height=2, width=21, command= size_12)
button_size_20= Button(fr_buttons, text="20", height=2, width=21, command= size_20)
#btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_google.grid(row=2, column=0, sticky="ew", padx=5)
btn_scopus.grid(row=3, column=0, sticky="ew", padx=5)
btn_dblp.grid(row=4, column=0, sticky="ew", padx=5)
btn_save.grid(row=5, column=0, sticky="ew", padx=5)
lbl_google.grid(row=6, column=0, sticky="ew", padx=5,pady=5)
lbl_scopus.grid(row=7, column=0, sticky="ew", padx=5,pady=5)
lbl_dblp.grid(row=8, column=0, sticky="ew", padx=5,pady=5)



lbl_font_size.grid(row=12, column=0, sticky="ew", padx=5,pady=15)
button_size_12.grid(row=13, column=0, sticky="ew", padx=5)
button_size_20.grid(row=14, column=0, sticky="ew", padx=5)





btn_clear.grid(row=15, column=0, sticky="ew", padx=5)



#btn_decrypt.grid(row=3, column=0, sticky="ew", padx=5)
#btn_load_public_key.grid(row=4, column=0, sticky="ew", padx=5, pady=0)
#btn_load_private_key.grid(row=5, column=0, sticky="ew", padx=5,pady=0)
#btn_create_key_pair.grid(row=6, column=0, sticky="ew", padx=5,pady=0)







fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")




window.mainloop()
