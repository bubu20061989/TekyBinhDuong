import tkinter as tk
 
from tkinter import Menu
from tkinter import messagebox
import math

class tinhPhuongTrinhBac2:
    def __init__(self,master):
        self.master = master
        self.master.title("Quản lí Học Sinh")
        self.master.geometry("400x400")
        
        self.widthEntry = self.width = 45
        self.width = 15
        self.x = 0
        self.y = 0
        self.Ty = 50
        self.Tx = 100
        self.Txy = 150
        #Label tên
        self.label_so_a = tk.Label(self.master, text = "Số a")
        self.label_so_a.place(x = self.x , y=self.y)
        #nhập tên
        self.entry_so_a = tk.Entry(self.master,width=self.widthEntry)
        self.entry_so_a.place(x=self.Tx, y=self.y)
        
        #Label tên
        self.label_so_b = tk.Label(self.master, text = "Số b")
        self.label_so_b.place(x = self.x , y=self.Ty)
        #nhập tên
        self.entry_so_b = tk.Entry(self.master,width=self.widthEntry)
        self.entry_so_b.place(x=self.Tx, y=self.Ty)
        
        #Label tên
        self.label_so_c = tk.Label(self.master, text = "Số c")
        self.label_so_c.place(x = self.x , y=self.Tx)
        #nhập tên
        self.entry_so_c = tk.Entry(self.master,width=self.widthEntry)
        self.entry_so_c.place(x=self.Tx, y=self.Tx)
        
     # button
        self.tinh_so_mol_button = tk.Button(self.master, text='TÍNH', command=self.tinh,width=self.width)
        self.tinh_so_mol_button.place(x=self.Txy + 100, y=self.Txy)

    def tinh(self):
        
        if not self.entry_so_a.get() or not self.entry_so_b.get() or not self.entry_so_c.get():
            messagebox.showerror(title='Error', message='Bạn chưa nhập đủ dữ liệu')
        
        so_a = float(self.entry_so_a.get())
        so_b = float(self.entry_so_b.get())
        so_c= float(self.entry_so_c.get())
         
        delta = so_b*so_b - 4*so_a*so_c
        
        if delta < 0:
            ketQua = 'Phương trình có vô nghiệm' 
            messagebox.showinfo(title='Kết quả', message=ketQua)
        if delta == 0:
            ketQua = 'Phương trình có nghiệm kép' + str(-so_b/so_a)
            messagebox.showerror(title='Kết quả', message=ketQua)
        if delta > 0:
            ketQua = 'Phương trình có hai nghiệm' + str((-so_b + math.sqrt(delta))/2* so_a) + " và " + str((-so_b - math.sqrt(delta))/2* so_a)
            messagebox.showerror(title='Kết quả', message=ketQua)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = tinhPhuongTrinhBac2(root)
    root.mainloop()
    