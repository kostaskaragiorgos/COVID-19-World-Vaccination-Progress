from tkinter import Menu, messagebox as msg, filedialog, Tk, simpledialog
import csv
import pandas as pd
import matplotlib.pyplot as plt

def userinput(titlel = "", promptl=""):
    userinput = simpledialog.askstring(title=titlel, prompt=promptl)
    return userinput

def helpmenu():
    pass

def aboutmenu():
    msg.showinfo("About", "VACCINATIONS ANALYSER\nVERSION 1.0")

class Vaccinations_Analyser():
    def __init__(self,master):
        self.master = master
        self.master.title("Vaccinations Analyser")
        self.master.geometry("250x200")
        self.master.resizable(False, False)
        self.filename = ""
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label="Insert a csv",
                                   accelerator='Ctrl+O', command= self.insert_csv)
        self.file_menu.add_command(label="Close File", accelerator="Ctrl+F4", command=self.closefile)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.show_menu = Menu(self.menu, tearoff=0)
        self.show_menu.add_command(label="Vaccination Process of A Country", command=self.vaccprossofacountry)
        self.show_menu.add_command(label="Vaccination Process of A Continent", command=self.vaccprossofacontinent)
        self.menu.add_cascade(label="Show", menu=self.show_menu)

        self.plot_menu = Menu(self.menu, tearoff=0)
        self.plot_menu.add_command(label="Vaccination Process of A Country", command=self.vaccprossplotcountry)
        self.plot_menu.add_command(label="Vaccination Process of A Continent", command=self.vaccprossplotcontinent)
        self.menu.add_cascade(label="Plot", menu=self.plot_menu)


        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: helpmenu())
        self.master.bind('<Control-i>',lambda event: aboutmenu())

    
    def vaccprossofacontinent(self):
        """vaccination process of a continent based on user's input"""
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        else:
            cont = userinput(titlel="Continent", promptl="Enter the name of the continent")

    
    def vaccprossofacountry(self):
        """vaccination process of a country based on user's input"""
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        else:
            pass
    
    def vaccprossplotcountry(self):
        """plots vaccination process of a country based on user's input"""
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        else:
            pass

    def vaccprossplotcontinent(self):
        """plots vaccination process of a continent based on user's input"""
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        else:
            pass

    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def closefile(self):
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        else:
            self.filename = ""
            msg.showinfo("SUCCESS", "CSV FILE SUCCESSFULLY CLOSED")

    def insert_csv(self):
        if self.filename == "":
            self.filename = filedialog.askopenfilename(initialdir="/", title="Select csv file",
                                                       filetypes=(("csv files", "*.csv"),
                                                                  ("all files", "*.*")))
        else:
            msg.showerror("ERROR", "A CSV FILE IS ALREADY OPEN")


        

def main():
    root=Tk()
    Vaccinations_Analyser(root)
    root.mainloop()
    
if __name__=='__main__':
    main()