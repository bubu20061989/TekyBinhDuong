import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox

class tinhChuViVaDienTich : 
    def __init__(self,master):
        self.master = master
        #self.master.title("dragon")
        #self.master.geometry('400x400')
        self.widthEntry=40
        
        self.label_length = tk.Label(self.master,text="Nhập chiều dài hình chữ nhật ")
        self.label_length.place(x = 0 , y = 0)
        
        self.entry_length = tk.Entry(self.master,width = self.widthEntry)
        self.entry_length.place (x = 180,  y = 0)

        self.label_width = tk.Label(self.master,text="Nhập chiều rộng hình chữ nhật ")
        self.label_width.place(x =1  , y = 60)

        self.entry_width = tk.Entry(self.master,width = self.widthEntry)
        self.entry_width.place (x =180 ,  y = 60)

        self.button_chuvi = tk.Button(self.master, text = "Tính chu vi ", command= self.chuVi,width=20)
        self.button_chuvi.place(x=200, y=300)

        self.button_dientich = tk.Button(self.master, text = "Tính diện tích ", command= self.dienTich,width=20)
        self.button_dientich.place(x=50, y=300)

    def check_submit(self):
        if self.checkInput():
            student_data = {
                "chuvi": float(self.entry_chuvi.get()),
                "dientich": float(self.entry_dientich.get())
            }
            self.save_to_json(student_data,'./data/quanLyDiemSo.json')
        if not self.entry_length.get() or not self.entry_width.get():
            messagebox.showerror(title='Error', message='Bạn chưa nhập đủ thông tin')
    def chuVi(self):
        ketQuachuVi = (self.entry_length.get() + self.entry_width.get())*2
        messagebox.showinfo(title="Kết quả", message=ketQuachuVi)
    def dienTich(self):
        ketQuaDienTich = self.entry_length.get() * self.entry_width.get()
        messagebox.showinfo(title="Kết quả", message=ketQuaDienTich)    

if __name__=="__main__":

    root = tk.Tk()
    app = tinhChuViVaDienTich(root)
    root.mainloop()
#viên 