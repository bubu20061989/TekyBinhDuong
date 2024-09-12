import tkinter as tk
from tkinter import ttk 

class quanLyHocSinh:
    def __init__(self,master):
        self.master = master
        self.master.title("Quản lí Học Sinh")
        self.master.geometry("400x400")
        self.widthEntry = self.width = 45
        self.x = 0
        self.y = 0
        self.Tx = 100
        self.Ty = 1
        #Label tên
        self.label_username = tk.Label(self.master, text = "Tên học sinh")
        self.label_username.place(x = self.x , y=10)
        #nhập tên
        self.entry_username = tk.Entry(self.master,width=self.widthEntry)
        self.entry_username.place(x=110, y=10)
        #Label class
        self.label_class = tk.Label(self.master, text = "Lớp")
        self.label_class.place(x = self.x , y=50)
        #Nhập class
        self.entry_class = tk.Entry(self.master, show= '*',width=self.widthEntry)
        self.entry_class.place(x=140, y=50)
        #Subjects
        self.label_subject = tk.Label(self.master, text = "Môn học",width=self.widthEntry)
        self.label_status.place(x = self.x , y=250)
        
        
        
        
        self.subjectValue = tk.StringVar() 
        gender = ttk.Combobox(self.master, width = 10, textvariable = self.subjectValue)
        gender['values'] = ("Toán", "Văn","Anh","Sử","Địa","Lý","Hóa","Tin") 
        gender.place(x = 200, y = 200)
        gender.current()



if __name__ == "__main__":
    root = tk.Tk()
    app = quanLyHocSinh(root)
    root.mainloop()
    root.geometry()