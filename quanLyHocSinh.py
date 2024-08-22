import tkinter as tk
from tkinter import ttk 

class hocsinh:
    def __init__(self,master):
        self.master = master
        self.master.title("Quản lí Học Sinh")
        self.master.geometry("400x400")
        #Label tên
        self.label_username = tk.Label(self.master, text = "Tên học sinh")
        self.label_username.place(x = 20 , y=10)
        #nhập tên
        self.entry_username = tk.Entry(self.master)
        self.entry_username.place(x=140, y=10)
        #Label class
        self.label_class = tk.Label(self.master, text = "Lớp")
        self.label_class.place(x = 20 , y=50)
        #Nhập class
        self.entry_class = tk.Entry(self.master, show= '*')
        self.entry_class.place(x=140, y=50)
        #Label PHONE 
        self.label_phone = tk.Label(self.master, text = "SĐT")
        self.label_phone.place(x = 20 , y=100)
        #Entry label_phone
        self.entry_phone = tk.Entry(self.master, show= '*')
        self.entry_phone.place(x = 140 , y=100)
        #gmail
        self.label_gmail = tk.Label(self.master, text = "Gmail")
        self.label_gmail.place(x = 20 , y=150)
        #Entry gmail
        self.entry_gmail = tk.Entry(self.master)
        self.entry_gmail.place(x = 140 , y=150)
        #Gender
        self.label_gender = tk.Label(self.master, text = "Giới tính")
        self.label_gender.place(x= 20, y= 200 )
        #button
        self.button_register = tk.Button(self.master, text = "REGISTER", command = self.login)
        self.button_register.place(x=150, y=350)
        #tình trạng
        self.label_status = tk.Label(self.master, text = "Trạng thái")
        self.label_status.place(x = 20 , y=250)
        
        
        
        
        n = tk.StringVar() 
        gender = ttk.Combobox(self.master, width = 10, textvariable = n)
        status = ttk.Combobox(self.master, width = 10, textvariable = n) 
        
        # Adding combobox drop down list 
        gender['values'] = ("Male", "Female","Other") 
        status["values"] = ("Bảo lưu","Đang học","Đã tốt nghiệp")
        gender.place(x = 140, y = 200)
        gender.current()
        status.place(x=140,y = 250)
        status.current()
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()
        gmail = self.entry_gmail.get()
        if not self.entry_username.get() or not self.entry_class.get() or not self.entry_phone.get() or not self.entry_gmail.get():
            print("False")
        else:
            print("True")
        
        
        
        
        
        
        

if __name__ == "__main__":
    root = tk.Tk()
    app = hocsinh(root)
    root.mainloop()
    root.geometry()