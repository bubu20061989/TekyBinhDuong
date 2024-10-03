import tkinter as tk
 
from tkinter import Menu
class tinhSoMolBangTheTich:
    def __init__(self,master):
        self.master = master
        #self.master.title("Quản lí Học Sinh")
        #self.master.geometry("400x400")
        
        self.widthEntry = self.width = 45
        self.width = 15
        self.x = 0
        self.y = 0
        self.Tx = 100
        self.Ty = 50
        #Label tên
        self.label_the_tich = tk.Label(self.master, text = "Nhập thể tích")
        self.label_the_tich.place(x = self.x , y=self.y)
        #nhập tên
        self.entry_the_tich = tk.Entry(self.master,width=self.widthEntry)
        self.entry_the_tich.place(x=self.Tx, y=self.y)
     # button
        self.tinh_so_mol_button = tk.Button(self.master, text='TÍNH', command=self.calculator,width=self.width)
        self.tinh_so_mol_button.place(x=self.Tx + 150, y=self.Ty - 15)
    def calculator(self):
        m = float(self.entry_the_tich.get())
        M = 22.4 
        answer = m/M
        print("Số mol là:",answer)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = tinhSoMolBangTheTich(root)
    root.mainloop()