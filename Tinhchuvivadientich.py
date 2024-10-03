import tkinter as tk 
from tkinter import ttk 

class register : 
    def __init__(self,master):
        self.master = master
        self.master.title("dragon")
        self.master.geometry('400x400')
        self.widthEntry=40
        
        self.label_chuvi = tk.Label(self.master,text="Nhập phép tính về chu vi ")
        self.label_chuvi.place(x = 0 , y = 0)
        
        self.entry_chuvi = tk.Entry(self.master,width = self.widthEntry)
        self.entry_chuvi.place (x = 180,  y = 0)

        self.label_dientich = tk.Label(self.master,text="Nhập phép tính về diện tích ")
        self.label_dientich.place(x =1  , y = 60)

        self.entry_dientich = tk.Entry(self.master,width = self.widthEntry)
        self.entry_dientich.place (x =180 ,  y = 60)

        self.button_chuvi = tk.Button(self.master, text = "Tính chu vi ", command= self.master,width=20)
        self.button_chuvi.place(x=200, y=300)

        self.button_dientich = tk.Button(self.master, text = "Tính diện tích ", command= self.master,width=20)
        self.button_dientich.place(x=50, y=300)

    def check_submit(self):
        if self.checkInput():
            student_data = {
                "chuvi": float(self.entry_chuvi.get()),
                "dientich": float(self.entry_dientich.get())
            }
            self.save_to_json(student_data,'./data/quanLyDiemSo.json')
        
            
        
        
        

if __name__=="__main__":

    root = tk.Tk()
    app = register(root)
    root.mainloop()
#viên 