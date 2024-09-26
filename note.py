import tkinter as tk#CÔNG THỨC 'COPY"
from tkinter import ttk 
#copy
class note: 
    def __init__(self,master):
        self.master = master
        self.master.title("note") #Đặt tên cửa sổ
        self.master.geometry("400x400")
        #########
        #Giá trị (hỏi Hoàng)
        self.widthEntry = self.width = 45 #Nhập độ rộng entry
        self.x = 0 #Nhập x
        self.y = 0 #Nhập y
        self.Tx = 100 #Độ tăng x
        self.Ty = 50 #Độ tăng y
        
        #Label 1 (Bảng)
        self.label_1 = tk.Label(self.master, text = "Label 1") #Đổi tên "label_1", thay đổi nội dung "text"
        self.label_1.place(x = self.x , y = self.y)#Vị trí x,y của label thảy đổi "x=...", "y=..."
        
        #Entry 1 (Nhập)
        self.entry_1 = tk.Entry(self.master,width=self.widthEntry)#thay đổi tên "entry_1"
        self.entry_1.place(x = self.x +self.Tx, y= self.y )#Vị trí x, y của entry
        
        #Combobox
        self.label_combobox = tk.Label(self.master, text = "Tên Combobox",width=self.widthEntry)#Tên của combobox, thay đổi nội dung "text"
        self.label_combobox.place(x = -115 , y=self.Ty)#Vị trí x, y của combobox
        
        #Ô chọn combobox
        self.comboboxValue = tk.StringVar()#Có thể thay đổi tên "self.combobox" 
        combobox = ttk.Combobox(self.master, width = self.widthEntry-3, textvariable = self.comboboxValue)#"Textvariable" phải giống tên dòng trên
        combobox['values'] = ("1", "2","3","...") #Các giá trị nằm trong combobox
        combobox.place(x=100, y =self.Ty)#vị trí x, y
        combobox.current()
        #button
        self.button_register = tk.Button(self.master, text = "REGISTER", command = self.login)#Tạo nút, có thể thay đổi "text"
        self.button_register.place(x=150, y=150)#Vị trí x,y
    #đăng nhập    
    def login(self):
        entry = self.entry_1.get()#Nhận giá trị của entry_1. "self.entry_1" phải giống phía trên
        combobox = self.comboboxValue.get()#Nhận giá trị của combobox. "self.comboboxValue" phải giống phía trên
        if not self.entry_1.get() or not self.comboboxValue.get():#Nếu không nhận được giá trị bên trong "If" thì           
            print("False")
        else:#nếu không thì
            print("True")
        
        
        
        
        
        
        
#Công thức "COPY"       
if __name__ == "__main__":
    root = tk.Tk()
    app = note(root)#"note" bên trong phải cùng tên với "class" phía trên
    root.mainloop()
    root.geometry()



    #  viên  