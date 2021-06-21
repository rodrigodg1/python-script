import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import tkinter.messagebox
from tkinter import *
from tkinter import scrolledtext  



window = tk.Tk()
window.resizable(False, False)
window.title("Text Editor Engine v1.0 (Auto Saving)")
#window.rowconfigure(0, minsize=740, weight=1)
#window.columnconfigure(1, minsize=740, weight=1)
window.geometry('970x650')


scrolW=73 
scrolH=32
txt_edit=scrolledtext.ScrolledText(window,width=scrolW, height=scrolH, wrap=tk.WORD,font='Consolas 16')  


#autosaving
path_file_save_this = "/Users/rodrigodutra/Desktop/python-script/search/blank_file.txt"



def alert_msg(msg):
    tkinter.messagebox.showinfo(title=None, message=msg)


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


def save_changes():
    try:
        with open(path_file_save_this, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
            
        
    except:
        alert_msg("Fail to save :(\nOpen the file again or Create a File First")
    
    


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
    
    return filepath

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
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor Engine - {filepath}")
    alert_msg("Success !")
    
    
    
def new_file():
    txt_edit.delete("1.0","end") 
    save_file()
    

def autosave():
    save_changes()
    time_in_s = 50
    time_to_auto_save_in_ms = time_in_s * 1000
    window.after(time_to_auto_save_in_ms, autosave) # time in milliseconds   
    print("saved")
            
    
    


fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_new = tk.Button(fr_buttons, text="New", command=new_file)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_upload = tk.Button(fr_buttons, text="Up. to Drive", command=drive_upload)

btn_new.grid(row=0, column=0, sticky="ew", padx=5, pady=2)
btn_open.grid(row=1, column=0, sticky="ew", padx=5, pady=2)
btn_save.grid(row=3, column=0, sticky="ew", padx=5,pady=2)
btn_upload.grid(row=4, column=0, sticky="ew", padx=5,pady=2)

btn_new.config( height = 2, width = 9 )
btn_open.config( height = 2, width = 9 )
btn_save.config( height = 2, width = 9 )
btn_upload.config( height = 2, width = 9 )

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


autosave() 
window.mainloop()