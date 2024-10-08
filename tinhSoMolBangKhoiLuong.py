import tkinter as tk
from tkinter import messagebox

 
from tkinter import Menu
class tinhSoMolBangKhoiLuong:
    def __init__(self,master):
        self.master = master
        # self.master.title("Quản lí Học Sinh")
        # self.master.geometry("400x400")
        
        self.widthEntry = self.width = 45
        self.width = 15
        self.x = 0
        self.y = 0
        self.Tx = 100
        self.Ty = 50
        #Label tên
        self.label_khoi_luong = tk.Label(self.master, text = "Nhập khối lượng")
        self.label_khoi_luong.place(x = self.x , y=self.y)
        #nhập tên
        self.entry_khoi_luong = tk.Entry(self.master,width=self.widthEntry)
        self.entry_khoi_luong.place(x=self.Tx, y=self.y)
        #Label class
        self.label_khoi_luong_rieng = tk.Label(self.master, text = "Nhập M")
        self.label_khoi_luong_rieng.place(x = self.x , y=self.Ty)
        #Nhập class
        self.entry_khoi_luong_rieng = tk.Entry(self.master,width=self.widthEntry)
        self.entry_khoi_luong_rieng.place(x=self.Tx, y=self.Ty)
        # button
        self.tinh_so_mol_button = tk.Button(self.master, text='TÍNH', command=self.calculator,width=self.width)
        self.tinh_so_mol_button.place(x=self.Tx + 150 , y=self.Tx - 10)
    def checkInput(self):
        if self.entry_khoi_luong.get()<0 or self.entry_khoi_luong_rieng<0:
             messagebox.showerror(title='Error', message="Vui lòng nhập giá trị dương")
        else:
            self.calculator()

    def calculator(self):
        m = float(self.entry_khoi_luong.get())
        M = float(self.entry_khoi_luong_rieng.get())
        answer = m/M
        messagebox.showinfo(title='Answer', message=answer)
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = tinhSoMolBangKhoiLuong(root)
    root.mainloop()