import tkinter as tk

class ez3:
    def __init__(self,master):
        self.master = master
        self.master.title("ez")
        self.master.geometry('400x400')

        self.label_lop = tk.Label(self.master,text = 'Lớp:')
        self.label_lop.place(x = 0, y= 0)
        
        self.entry_lop = tk.Entry(self.master)
        self.entry_lop.place(x = 100, y = 0)
        
        self.label_phong_hoc = tk.Label(self.master,text = 'Phòng học:')
        self.label_phong_hoc.place(x = 0, y= 50)
        
        self.entry_phong_hoc = tk.Entry(self.master)
        self.entry_phong_hoc.place(x = 100, y = 50)
        
        self.label_GVCN = tk.Label(self.master,text = 'GVCN')
        self.label_GVCN.place(x = 0, y= 100)
        
        self.entry_GVCN = tk.Entry(self.master)
        self.entry_GVCN.place(x = 100, y = 100)
        
        self.label_lop_truong = tk.Label(self.master,text = 'Lớp trưởng')
        self.label_lop_truong.place(x = 0, y= 150)
        
        self.entry_lop_truong = tk.Entry(self.master)
        self.entry_lop_truong.place(x = 100, y = 150)
        
        self.label_lop_pho = tk.Label(self.master,text = 'Lớp phó')
        self.label_lop_pho.place(x = 0, y= 200)
        
        self.entry_lop_pho = tk.Entry(self.master)
        self.entry_lop_pho.place(x = 100, y = 200)
        
        self.label_soluonghs = tk.Label(self.master,text = 'Số lượng học sinh')
        self.label_soluonghs.place(x = 0, y = 250)
        
        self.entry_soluonghs = tk.Entry(self.master)
        self.entry_soluonghs.place(x = 100, y = 250)
        
        self.login_button = tk.Button(self.master,text = 'Login',command = self.Login)
        self.login_button.place(x = 150, y = 300 )
        
        
        
    def Login(self):
        Lop = self.entry_lop.get()
        print(Lop)
        phong_hoc = self.entry_phong_hoc.get()
        print(phong_hoc)
        gvcn = self.entry_GVCN.get()
        print(gvcn)
        lop_truong = self.entry_lop_truong.get()
        print(lop_truong)
        lop_pho = self.entry_lop_pho.get()
        print(lop_pho)
        soluonghs = self.entry_soluonghs.get()
        print(soluonghs)
        
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ez3(root)
    root.mainloop()

