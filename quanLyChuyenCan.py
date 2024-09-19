import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class quanLyChuyenCan:
    def __init__(self,master):
        self.master = master
        self.master.title("Quản lý chuyên cần")
        self.master.geometry('400x400')
        
        self.widthEntry = 45
        
        self.x = 0
        self.y = 0

        self.Tx = 100

        self.Tlbly = 50

        self.label_HSNghiHoc = tk.Label(self.master,text = 'Học sinh nghỉ học:')
        self.label_HSNghiHoc.place(x = self.x, y = self.y)

        self.entry_HSNghiHoc = tk.Entry(self.master,width = self.widthEntry)
        self.entry_HSNghiHoc.place(x = self.x + self.Tx , y = self.y)
  
        self.label_lop_hoc = tk.Label(self.master,text = 'Lớp:')
        self.label_lop_hoc.place(x = self.x, y = self.Tlbly)

        self.entry_lop_hoc = tk.Entry(self.master,width = self.widthEntry)
        self.entry_lop_hoc.place(x = self.x + self.Tx, y = self.Tlbly)

        self.label_CPvaKP = tk.Label(self.master,text = 'Có phép(Ko phép)')
        self.label_CPvaKP.place(x = self.x, y = self.Tlbly * 2 )

        self.label_liDoNghiHoc = tk.Label(self.master,text = 'Lí do nghỉ học')
        self.label_liDoNghiHoc.place(x = self.x, y = self.Tlbly * 3 )
        
        # self.entry_lop_truong = tk.Entry(self.master,width = self.widthEntry)
        # self.entry_lop_truong.place(x = self.x + self.Tx, y = self.Tlbly * 3 )
        
        self.luuLopHoc_button = tk.Button(self.master,text = 'Lưu chuyên cần',command = self.luuLopHoc)
        self.luuLopHoc_button.place(x = self.x + 175, y = self.Tlbly * 4 )
        
        self.CPvaKPValue = tk.StringVar() 
        self.CPvaKPValue = tk.StringVar() 
        CPvaKP = ttk.Combobox(self.master, width = self.widthEntry, textvariable = self.CPvaKPValue)
        CPvaKP['values'] = ("Có phép", "Không phép") 
        CPvaKP.place(x = self.x + self.Tx, y = self.Tlbly * 2)
        CPvaKP.current()
    
        self.liDoNghiHocValue = tk.StringVar() 
        self.vValue = tk.StringVar() 
        liDoNghiHoc = ttk.Combobox(self.master, width = self.widthEntry, textvariable = self.liDoNghiHocValue)
        liDoNghiHoc['values'] = ("Bị ốm", "Ngủ quên","Có việc") 
        liDoNghiHoc.place(x = self.x + self.Tx, y = self.Tlbly * 3)
        liDoNghiHoc.current()
    
    
    
    def luuLopHoc(self):

        Lop = self.entry_lop.get()
        phong_hoc = self.entry_phong_hoc.get()
        gvcn = self.entry_GVCN.get()
        lop_truong = self.entry_lop_truong.get()
        lop_pho = self.entry_lop_pho.get()
        soluonghs = self.entry_soluonghs.get()

if __name__ == "__main__":
    root = tk.Tk()
    app = quanLyChuyenCan(root)
    root.mainloop()



