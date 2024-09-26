import tkinter as tk
from tkinter import ttk

class quanLyChuyenCan:
    def __init__(self, master):
        self.master = master

        # Remove geometry setting from here
        self.master.geometry('400x400')  # Remove this line

        self.widthEntry = 45
        self.width = 5
        self.x = 0
        self.y = 0
        self.Tlbly = 50

        self.label_HSNghiHoc = tk.Label(self.master, text='Học sinh nghỉ học:')
        self.label_HSNghiHoc.place(x=self.x, y=self.y)

        self.entry_HSNghiHoc = tk.Entry(self.master, width=self.widthEntry)
        self.entry_HSNghiHoc.place(x=self.x + 100, y=self.y)

        self.label_lop_hoc = tk.Label(self.master, text='Lớp:')
        self.label_lop_hoc.place(x=self.x, y=self.Tlbly)

        self.entry_lop_hoc = tk.Entry(self.master, width=self.widthEntry)
        self.entry_lop_hoc.place(x=self.x + 100, y=self.Tlbly)

        self.label_lop_hoc = tk.Label(self.master, text='Có phép/Ko phép:')
        self.label_lop_hoc.place(x=self.x, y=self.Tlbly+50)

        self.label_lop_hoc = tk.Label(self.master, text='Lý do nghỉ:')
        self.label_lop_hoc.place(x=self.x, y=self.Tlbly+100)


# button
        self.luuLopHoc_button = tk.Button(self.master, text='Thêm', command=self.luuLopHoc,width=self.width)
        self.luuLopHoc_button.place(x=self.x + 190, y=self.Tlbly * 4)

        self.luuLopHoc_button = tk.Button(self.master, text='Sửa', command=self.luuLopHoc,width=self.width)
        self.luuLopHoc_button.place(x=self.x + 260, y=self.Tlbly * 4)

        self.luuLopHoc_button = tk.Button(self.master, text='Xóa', command=self.luuLopHoc,width=self.width)
        self.luuLopHoc_button.place(x=self.x + 330, y=self.Tlbly * 4)

        self.CPvaKPValue = tk.StringVar() 
        CPvaKP = ttk.Combobox(self.master, width=self.widthEntry, textvariable=self.CPvaKPValue)
        CPvaKP['values'] = ("Có phép", "Không phép") 
        CPvaKP.place(x=self.x + 100, y=self.Tlbly * 2)

        self.liDoNghiHocValue = tk.StringVar() 
        liDoNghiHoc = ttk.Combobox(self.master, width=self.widthEntry, textvariable=self.liDoNghiHocValue)
        liDoNghiHoc['values'] = ("Bị ốm", "Ngủ quên", "Có việc") 
        liDoNghiHoc.place(x=self.x + 100, y=self.Tlbly * 3)

    def luuLopHoc(self):
        # Implement save functionality here
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = quanLyChuyenCan(root)
    root.mainloop()
