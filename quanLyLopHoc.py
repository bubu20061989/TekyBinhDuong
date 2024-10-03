import tkinter as tk
from tkinter import messagebox
class quanLyLopHoc:
    def __init__(self,master):
        self.master = master
        #self.master.title("Quản lý lớp học")
        #self.master.geometry('400x400')
        
        self.widthEntry = 45
        self.width = 5
        self.x = 0
        self.y = 0

        self.Tx = 100

        self.Tlbly = 50

        self.label_lop = tk.Label(self.master,text = 'Lớp:')
        self.label_lop.place(x = self.x, y = self.y)

        self.entry_lop = tk.Entry(self.master,width = self.widthEntry)
        self.entry_lop.place(x = self.x + self.Tx , y = self.y)
  
        self.label_phong_hoc = tk.Label(self.master,text = 'Phòng học:')
        self.label_phong_hoc.place(x = self.x, y = self.Tlbly)

        self.entry_phong_hoc = tk.Entry(self.master,width = self.widthEntry)
        self.entry_phong_hoc.place(x = self.x + self.Tx, y = self.Tlbly)

        self.label_GVCN = tk.Label(self.master,text = 'GVCN')
        self.label_GVCN.place(x = self.x, y = self.Tlbly * 2 )
        
        self.entry_GVCN = tk.Entry(self.master,width = self.widthEntry)
        self.entry_GVCN.place(x = self.x + self.Tx, y = self.Tlbly * 2 )
        
        self.label_lop_truong = tk.Label(self.master,text = 'Lớp trưởng')
        self.label_lop_truong.place(x = self.x, y = self.Tlbly * 3 )
        
        self.entry_lop_truong = tk.Entry(self.master,width = self.widthEntry)
        self.entry_lop_truong.place(x = self.x + self.Tx, y = self.Tlbly * 3 )
        
        self.label_lop_pho = tk.Label(self.master,text = 'Lớp phó')
        self.label_lop_pho.place(x = self.x, y = self.Tlbly * 4 )
        
        self.entry_lop_pho = tk.Entry(self.master,width = self.widthEntry)
        self.entry_lop_pho.place(x = self.x + self.Tx, y = self.Tlbly * 4 )
        
        self.label_soluonghs = tk.Label(self.master,text = 'Số lượng học sinh')
        self.label_soluonghs.place(x = self.x, y = self.Tlbly * 5 )
        
        self.entry_soluonghs = tk.Entry(self.master,width = self.widthEntry)
        self.entry_soluonghs.place(x = self.x + self.Tx, y = self.Tlbly * 5 )
# button
        self.luuLopHoc_button = tk.Button(self.master, text='Thêm', command=self.luuLopHoc,width=self.width)
        self.luuLopHoc_button.place(x=self.x + 190, y=self.Tlbly * 6)

        self.luuLopHoc_button = tk.Button(self.master, text='Sửa', command=self.luuLopHoc,width=self.width)
        self.luuLopHoc_button.place(x=self.x + 260, y=self.Tlbly * 6)

        self.luuLopHoc_button = tk.Button(self.master, text='Xóa', command=self.luuLopHoc,width=self.width)
        self.luuLopHoc_button.place(x=self.x + 330, y=self.Tlbly * 6)


    
    def checkNumber(self, string):
        try:
            int(string)
            return True
        except ValueError:
            messagebox.showerror("Error","Số lượng học sinh phải là số nguyên")
            return False
    def checkInput(self):
        if not self.entry_lop.get() or not self.entry_phong_hoc.get() or not self.entry_GVCN.get() or not self.entry_lop_truong.get() or not self.entry_lop_pho.get() or not self.entry_soluonghs.get():
            messagebox.showerror("Error","Vui lòng nhập đầy đ�� thông tin")
            return False
        if not self.checkNumber(self.entry_soluonghs.get()) and int(self.entry_soluonghs.get()) < 0:
            return False
        
    def luuLopHoc(self):
        if self.checkInput():
            Lop = self.entry_lop.get()
            phong_hoc = self.entry_phong_hoc.get()
            gvcn = self.entry_GVCN.get()
            lop_truong = self.entry_lop_truong.get()
            lop_pho = self.entry_lop_pho.get()
            soluonghs = self.entry_soluonghs.get()

        

        
    def luuLopHoc(self):
        Lop = self.entry_lop.get()
        phong_hoc = self.entry_phong_hoc.get()
        gvcn = self.entry_GVCN.get()
        lop_truong = self.entry_lop_truong.get()
        lop_pho = self.entry_lop_pho.get()
        soluonghs = self.entry_soluonghs.get()



    def luuLopHoc(self):
        # Implement save functionality here
        pass

        
if __name__ == "__main__":
    root = tk.Tk()
    app = quanLyLopHoc(root)
    root.mainloop()

