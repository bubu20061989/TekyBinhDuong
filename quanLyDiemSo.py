import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import main

class quanLyDiemSo:
    def __init__(self,master):
        self.master = master
        self.master.title("Quản lí Học Sinh")
        self.master.geometry("400x400")
        
        self.widthEntry = self.width = 45
        self.width = 5
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
        self.entry_class = tk.Entry(self.master,width=self.widthEntry)
        self.entry_class.place(x=self.Tx, y=self.Ty)
        #Point
        self.label_point_math = tk.Label(self.master, text = "Điểm môn Toán")
        self.label_point_math.place(x = self.x , y=self.Ty*2)
        #Point
        self.entry_point_math = tk.Entry(self.master,width=self.widthEntry)
        self.entry_point_math.place(x=self.Tx, y=self.Ty*2)
        #Point
        self.label_point_literature = tk.Label(self.master, text = "Điểm môn Văn")
        self.label_point_literature.place(x = self.x , y=self.Ty*3)
        #Point
        self.entry_point_literature = tk.Entry(self.master,width=self.widthEntry)
        self.entry_point_literature.place(x=self.Tx, y=self.Ty*3)
        #Point
        self.label_point_english = tk.Label(self.master, text = "Điểm môn Anh")
        self.label_point_english.place(x = self.x , y=self.Ty*4)
        #Point
        self.entry_point_english = tk.Entry(self.master,width=self.widthEntry)
        self.entry_point_english.place(x=self.Tx, y=self.Ty*4)
        #Point
        self.label_point_physic = tk.Label(self.master, text = "Điểm môn Lí")
        self.label_point_physic.place(x = self.x , y=self.Ty*5)
        #Point
        self.entry_point_physic = tk.Entry(self.master,width=self.widthEntry)
        self.entry_point_physic.place(x=self.Tx, y=self.Ty*5)
        #Point
        self.label_point_chemistry = tk.Label(self.master, text = "Điểm môn Hóa")
        self.label_point_chemistry.place(x = self.x , y=self.Ty*6)
        #Point
        self.entry_point_chemistry = tk.Entry(self.master,width=self.widthEntry)
        self.entry_point_chemistry.place(x=self.Tx, y=self.Ty*6)

#button
        self.luuLopHoc_button = tk.Button(self.master, text='Thêm', command=self.luuLopHoc,width=self.width)
        self.luuLopHoc_button.place(x=self.x + 190, y=self.Ty * 7)

        self.luuLopHoc_button = tk.Button(self.master, text='Sửa', command=self.luuLopHoc,width=self.width)
        self.luuLopHoc_button.place(x=self.x + 260, y=self.Ty * 7)

        self.luuLopHoc_button = tk.Button(self.master, text='Xóa', command=self.luuLopHoc,width=self.width)
        self.luuLopHoc_button.place(x=self.x + 330, y=self.Ty * 7)
        
    def checkInput(self): 
        if not self.entry_username.get() or not self.entry_class.get() or not self.entry_point_literature.get() or not self.entry_point_math.get()or not self.entry_point_english.get() or not self.entry_point_chemistry.get() or not self.entry_point_physic:
            messagebox.showerror(title='Error', message='Bạn chưa nhập đủ thông tin')
            return False
        if float(self.entry_point_math.get() )< 0 or float(self.entry_point_math.get())>10 :
            messagebox.showerror(title='Error', message='Bạn chưa nhập đúng điểm Toán')
            return False
        if float(self.entry_point_literature.get() )< 0 or float(self.entry_point_literature.get())>10 :
            messagebox.showerror(title='Error', message='Bạn chưa nhập đúng điểm Văn')
            return False 
        if float(self.entry_point_english.get() )< 0 or float(self.entry_point_english.get())>10 :
            messagebox.showerror(title='Error', message='Bạn chưa nhập đúng điểm Anh')
            return False
        if float(self.entry_point_chemistry.get() )< 0 or float(self.entry_point_chemistry.get())>10 :
            messagebox.showerror(title='Error', message='Bạn chưa nhập đúng điểm Hóa')
            return False
        if float(self.entry_point_physic.get() )< 0 or float(self.entry_point_physic.get())>10 :
            messagebox.showerror(title='Error', message='Bạn chưa nhập đúng điểm Lý')
            return False
        return True
    def check_submit(self):
        if self.checkInput():
            student_data = {
                "name": self.entry_username.get(),
                "grade": self.entry_class.get(),
                "math_point": float(self.entry_point_math.get()),
                "literature_point": float(self.entry_point_literature.get()),
                "english_point": float(self.entry_point_english.get()),
                "chemistry_point": float(self.entry_point_chemistry.get()),
                "physic_point": float(self.entry_point_physic.get())
            }
            main.save_to_json(student_data,'./data/quanLyDiemSo.json')
            
    
            
        
           
        
    def luuLopHoc(self):
        # Implement save functionality here
        pass

        
        
        


if __name__ == "__main__":
    root = tk.Tk()
    app = quanLyDiemSo(root)
    root.mainloop()
    root.geometry()

#viên     