from tkinter import Menu, messagebox as msg, filedialog, Tk, simpledialog
import csv
from numpy.lib.twodim_base import triu_indices_from
import pandas as pd
import matplotlib.pyplot as plt

def userinput(titlel = "", promptl=""):
    userinput = simpledialog.askstring(title=titlel, prompt=promptl)
    return userinput

def userinputvalidation(userinput="", validation=""):
    ##while  not self.df['Country/Region'].str.contains(str(self.asked_country)).any():
    if  not validation.str.contains(str(userinput)).any():
        return False
    else:
        return True
    

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

    def file_input_validation(self):
        """ user input validation """
        if ".csv" in self.filename:
            self.df = pd.read_csv(self.filename)
            self.check_columns()
        else:
            self.filename = ""
            msg.showerror("ERROR", "NO CSV IMPORTED")

    def check_columns(self):
        """ checks the columns name from the importrd .csv file """
        if all([item in self.df.columns for item in ['location',
                                                     'iso_code',
                                                     'date', 'total_vaccinations',
                                                     'people_vaccinated', 'people_fully_vaccinated',
                                                     'daily_vaccinations_raw', 'daily_vaccinations',
                                                     'total_vaccinations_per_hundred',
                                                     'people_vaccinated_per_hundred',
                                                     'people_fully_vaccinated_per_hundred',
                                                     'daily_vaccinations_per_million']]):
            self.df.drop_duplicates(subset='location', keep='last', inplace=True)
            msg.showinfo("SUCCESS", "CSV FILE ADDED SUCCESSFULLY")
        else:
            self.filename = ""
            msg.showerror("ERROR", "NO PROPER CSV ")

    def vaccprossofacontinent(self):

        """vaccination process of a continent based on user's input"""
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        else:
            cont = userinput(titlel="Continent", promptl="Enter the name of the continent")
            flag = userinputvalidation(cont, self.df['location'])
            if flag:
                pass
            else:
                msg.showerror("INVALID USER INPUT", "ENTER A VALID USER INPUT")


    
    def vaccprossofacountry(self):
        """vaccination process of a country based on user's input"""
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        else:
            count = userinput(titlel="Country", promptl="Enter the name of the counntry")
            flag = userinputvalidation(count, self.df['location'])
            if flag:
                pass
            else:
                msg.showerror("INVALID USER INPUT", "ENTER A VALID USER INPUT")
    
    def vaccprossplotcountry(self):
        """plots vaccination process of a country based on user's input"""

        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        else:
            count = userinput(titlel="Country", promptl="Enter the name of the counntry")
            flag = userinputvalidation(count, self.df['location'])
            if flag:
                pass
            else:
                msg.showerror("INVALID USER INPUT", "ENTER A VALID USER INPUT")

    def vaccprossplotcontinent(self):
        """plots vaccination process of a continent based on user's input"""
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        else:
            cont = userinput(titlel="Continent", promptl="Enter the name of the continent")
            flag = userinputvalidation(cont, self.df['location'])
            if flag:
                pass
            else:
                msg.showerror("INVALID USER INPUT", "ENTER A VALID USER INPUT")

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
            self.file_input_validation()
        else:
            msg.showerror("ERROR", "A CSV FILE IS ALREADY OPEN")


        

def main():
    root=Tk()
    Vaccinations_Analyser(root)
    root.mainloop()
    
if __name__=='__main__':
    main()