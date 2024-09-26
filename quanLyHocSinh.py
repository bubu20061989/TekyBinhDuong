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
        self.Ty = 50
        #Label tên
        self.label_username = tk.Label(self.master, text = "Tên học sinh")
        self.label_username.place(x = self.x , y=self.y)
        #nhập tên
        self.entry_username = tk.Entry(self.master,width=self.widthEntry)
        self.entry_username.place(x=self.Tx, y=self.y)
        #Label class
        self.label_class = tk.Label(self.master, text = "Lớp")
        self.label_class.place(x = self.x , y=self.Ty)
        #Nhập class
        self.entry_class = tk.Entry(self.master, show= '*',width=self.widthEntry)
        self.entry_class.place(x=self.Tx, y=self.Ty)
        #Label PHONE 
        self.label_phone = tk.Label(self.master, text = "SĐT")
        self.label_phone.place(x = self.x , y=self.Ty*2)
        #Entry label_phone
        self.entry_phone = tk.Entry(self.master, show= '*',width=self.widthEntry)
        self.entry_phone.place(x=self.Tx , y=self.Ty*2)
        #gmail
        self.label_gmail = tk.Label(self.master, text = "Gmail")
        self.label_gmail.place(x = self.x , y=self.Ty*3)
        #Entry gmail
        self.entry_gmail = tk.Entry(self.master,width=self.widthEntry)
        self.entry_gmail.place(x=self.Tx , y=self.Ty*3)
        #Gender
        self.label_gender = tk.Label(self.master, text = "Giới tính",width=self.widthEntry)
        self.label_gender.place(x =-136, y= self.Ty*4 )
        #button
        self.button_register = tk.Button(self.master, text = "REGISTER", command = self.login)
        self.button_register.place(x=150, y=300)
        #tình trạng
        self.label_status = tk.Label(self.master, text = "Trạng thái",width=self.widthEntry)
        self.label_status.place(x =-135 , y=self.Ty*5)
        
        
        
        
        self.genderValue = tk.StringVar() 
        gender = ttk.Combobox(self.master, width = self.widthEntry, textvariable = self.genderValue)
        gender['values'] = ("Male", "Female","Other") 
        gender.place(x = self.Tx, y = self.Ty*4)
        gender.current()
        
        self.statusValue = tk.StringVar()
        status = ttk.Combobox(self.master, width = self.widthEntry, textvariable = self.statusValue) 
        status["values"] = ("Bảo lưu","Đang học","Đã tốt nghiệp")
        status.place(x=self.Tx,y = self.Ty*5)
        status.current()
        
    def login(self):
        username = self.entry_username.get()
        classs = self.entry_class.get()
        phone = self.entry_phone.get()
        gmail = self.entry_gmail.get()
        gender = self.genderValue.get()
        status = self.statusValue.get()
        if not self.entry_username.get() or not self.entry_class.get() or not self.entry_phone.get() or not self.entry_gmail.get()or not self.genderValue.get()or not self.statusValue.get():
            print("False")
        else:
            print("True")
        
        
        
        
        
        
        

if __name__ == "__main__":
    root = tk.Tk()
    app = quanLyHocSinh(root)
    root.mainloop()
    root.geometry()


#viên 