import tkinter as tk 
from tkinter import ttk 

class quanLyHocTap :
    def __init__(self,master):
        self.master = master
        #self.master.title("dragon")
        #self.master.geometry('400x400')

        self.widthEntry = self.width = 45
        self.width = 5
        self.x = 0
        self.y = 0
        self.Tx = 100
        self.Ty = 50


        self.label_MSHS = tk.Label(self.master,text="MSHS")
        self.label_MSHS.place(x = 1 , y = 0)
        
        self.entry_MSHS = tk.Entry(self.master)
        self.entry_MSHS.place (x = 60,  y = 0)
        
        self.label_toan = tk.Label(self.master,text="Diem mon toan")
        self.label_toan.place(x =1  , y = 60)

        self.entry_toan = tk.Entry(self.master)
        self.entry_toan.place (x =90 ,  y = 60)
        
        self.label_van = tk.Label(self.master,text="Diem mon van")
        self.label_van.place(x =1  , y = 120)

        self.entry_van = tk.Entry(self.master)
        self.entry_van.place (x =90 ,  y = 180)
        
        self.label_anh = tk.Label(self.master,text="Diem mon Anh")
        self.label_anh.place(x =1  , y = 180)

        self.entry_anh = tk.Entry(self.master)
        self.entry_anh.place (x =60 ,  y = 120)
        
        self.label_hanhkiem = tk.Label(self.master,text="Hanh kiem")
        self.label_hanhkiem.place(x=1,y=220)

        n = tk.StringVar() 
        self.entry_hanhkiem = ttk.Combobox(self.master, width = 27, textvariable = n) 
        
        # Adding combobox drop down list 
        self.entry_hanhkiem['values'] = (' Gioi',  
                                ' Kha',
                                'Tb',
                                'Yeu',)
        
        self.entry_hanhkiem.place(x =90,y=220)
        self.entry_hanhkiem.current()
#button
        self.luuLopHoc_button = tk.Button(self.master, text='Thêm', command=self.luuLopHoc,width=self.width)
        self.luuLopHoc_button.place(x=self.x + 190, y=self.Ty * 5)

        self.luuLopHoc_button = tk.Button(self.master, text='Sửa', command=self.luuLopHoc,width=self.width)
        self.luuLopHoc_button.place(x=self.x + 260, y=self.Ty * 5)

        self.luuLopHoc_button = tk.Button(self.master, text='Xóa', command=self.luuLopHoc,width=self.width)
        self.luuLopHoc_button.place(x=self.x + 330, y=self.Ty * 5)
        
        

    def luuLopHoc(self):
        # Implement save functionality here
        pass


if __name__=="__main__":

    root = tk.Tk()
    app = quanLyHocTap(root)
    root.mainloop()
    
    
#viên 