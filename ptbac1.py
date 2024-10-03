import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox

class register : 
    def __init__(self,master):
        self.master = master
        self.master.title("dragon")
        self.master.geometry('400x400')
        self.widthEntry=40
        
        self.label_a = tk.Label(self.master,text="Nhập a ")
        self.label_a.place(x = 0 , y = 0)
        
        self.entry_a = tk.Entry(self.master,width = self.widthEntry)
        self.entry_a.place (x = 100,  y = 0)

        self.label_b = tk.Label(self.master,text="Nhập b ")
        self.label_b.place(x =1  , y = 60)

        self.entry_b = tk.Entry(self.master,width = self.widthEntry)
        self.entry_b.place (x =100 ,  y = 60)

        self.button_tinh = tk.Button(self.master, text = "Tính nghiệm ab ", command= self.master,width=20)
        self.button_tinh.place(x=200, y=100)
        
    def nghiem (self):
        if not self.entry_a.get() or not self.entry_b.get():
            messagebox.showerror(title='Error', message='Bạn chưa nhập đủ dữ liệu')
        else:
            a = float(self.entry_a.get()),
            b = float(self.entry_b.get()),
            
            ketQua = 'Nghiệm của phương trình ' + str(-b/a)
            messagebox.showerror(title='Kết quả', message=ketQua)

            
        
    

        
        
            
            
        
if __name__=="__main__":

    root = tk.Tk()
    app = register(root)
    root.mainloop()