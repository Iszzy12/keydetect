from tkinter import *
from tkinter import ttk

import psutil

def keylloger_detection():
    
    SUCCPICOUS = ["keylogger","logger", "keystroke","record"]
    
    #clearing treeview

    for rows in tree.get_children():
        tree.delete(rows)
        
    
    for process in psutil.process_iter(attrs=["name", "exe", "pid"]):
        try:
            process_name = process.info["name"].lower()
            process_path = process.info["exe"]
        
        
            if any(keyword in process_name for keyword in SUCCPICOUS):

            
             tree.insert("", "end", values=(process_name, process_path))
             
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            
            pass
        
        
    

#GUI interface set up
root = Tk()
root.title("key_detect")
root.geometry("800x600")
root.config(bg="#609cfc")


label = Label(master= root,text ="welocome", font = ("Arial", 12))
label.pack(pady=15)

label = Label(master= root,text ="CLICK THE BUTTON BELLOW TO START THE SCAN", font = ("Arial", 12))
label.pack(pady=15)

#button to start the proccess

button = Button(master= root,text= "start scan",bg="#f0f4fa")
button.pack(pady=15)

#creation of table to show the decetion and file path
tree = ttk.Treeview(root, columns=("proccess_name", "file_path"), show="headings")
tree.heading("proccess_name",text="process")
tree.heading("file_path", text="file path")
tree.pack(pady=20, fill="both", expand=True)

root.mainloop()