import tkinter as tk 

from tkinter import ttk, StringVar
from tkinter import messagebox
from tkinter.ttk import *


class tinhSVT : 
    def __init__(self,master):
        self.master = master
        #self.master.title("")
        #self.master.geometry('400x400')
        self.widthEntry=40
        
        self.x = 0
        self.y = 0
        self.Tx = 100
        self.Ty = 50
        
        self.label_a = tk.Label(self.master,text="Nhập giá trị ")
        self.label_a.place(x = self.x , y = self.y)
        
        self.entry_a = tk.Entry(self.master,width = self.widthEntry)
        self.entry_a.place (x = self.Tx,  y = self.y)
        self.var = StringVar(self.master, "1")
        
        self.radio = StringVar()  

        self.R1 = Radiobutton(self.master, text="S", variable=self.radio, value="S")
        self.R1.place(x = self.x+30 , y = 25)
        self.R2 = Radiobutton(self.master, text="V", variable=self.radio, value="V") 
        self.R2.place(x=self.x +60,y=25) 
        self.R3 = Radiobutton(self.master, text="T", variable=self.radio, value="T") 
        self.R3.place(x=self.x +90,y=25)


        
        self.radio2 = StringVar()  

        self.label_b = tk.Label(self.master,text="Nhập giá trị ")
        self.label_b.place(x =self.x  , y = self.Ty)

        self.entry_b = tk.Entry(self.master,width = self.widthEntry)
        self.entry_b.place (x =self.Tx ,  y = self.Ty)
        
        self.R4 = Radiobutton(self.master, text="S", variable=self.radio2, value="S")
        self.R4.place(x = self.x+30 , y = 75)
        self.R5 = Radiobutton(self.master, text="V", variable=self.radio2, value="V")
        self.R5.place(x=self.x +60,y=75) 
        self.R6 = Radiobutton(self.master, text="T", variable=self.radio2, value="T") 
        self.R6.place(x=self.x +90,y=75)

        self.button_tinh = tk.Button(self.master, text = "Tính nghiệm ab ", command= self.checkInput,width=20)
        self.button_tinh.place(x=200, y=100)
        
    def checkInput(self):
    
       
        if not self.entry_a.get() or not self.entry_b.get() or not self.radio.get() or not self.radio2.get():
            messagebox.showerror(title='Error', message='Bạn chưa nhập đủ thông tin')
        else:
            Ert1 = float(self.entry_a.get())
            Ert2 = float(self.entry_b.get())
            ketQua = 0
            #print(self.radio.get())
            if (self.radio.get() =="S" and self.radio2.get()=="V"):
               # print(Ert1/Ert2)
                ketQua = Ert1/Ert2
                messagebox.showinfo(title='Kết quả là', message=ketQua)

            elif (self.radio.get() =="V" and self.radio2.get()=="S"):
                ketQua = Ert2/Ert1
                messagebox.showinfo(title='Kết quả là', message=ketQua)
            elif (self.radio.get() =="S" and self.radio2.get()=="T"):
                ketQua = Ert1/Ert2
                messagebox.showinfo(title='Kết quả là', message=ketQua)
            elif (self.radio.get() =="T" and self.radio2.get()=="S"):
                ketQua = Ert2/Ert1
                messagebox.showinfo(title='Kết quả là', message=ketQua)
            elif (self.radio.get() =="T" and self.radio2.get()=="V"):
                ketQua = Ert2*Ert1
                messagebox.showinfo(title='Kết quả là', message=ketQua)
            elif (self.radio.get() =="V" and self.radio2.get()=="T"):
                ketQua = Ert1*Ert2
                messagebox.showinfo(title='Kết quả là', message=ketQua)

            
            
 

        
    

        
        
            
            
        
if __name__=="__main__":

    root = tk.Tk()
    app = tinhSVT(root)
    root.mainloop()