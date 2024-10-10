import tkinter as tk
from tkinter import Menu
import quanLyChuyenCan  # Import your class file
import quanLyDiemSo
import quanLyHocSinh
import quanLyHocTap
import quanLyLopHoc
import tinhSoMolBangKhoiLuong
import tinhSoMolBangTheTich
import tinhPhuongTrinhBacMot
import tinhPTbac2
import tinhSVT
import doiDonVi

class MenuApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Menu Application")
        self.master.geometry("400x400")  # Set geometry for the main window
        
        # Initialize the menu
        self.menu = Menu(master)
        self.master.config(menu=self.menu)
        

        # Add main menu items
        self.new_item = Menu(self.menu, tearoff=0)
        self.new_item2 = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Quản lý", menu=self.new_item)

        self.menu.add_cascade(label="Môn", menu=self.new_item2)
        # self.new_item.add_cascade(label="Tính số mol",new_item=self.new_item)
        self.new_item.add_separator()
        self.new_item2.add_separator()


        
        # Add 'Quản lý chuyên cần' as another top-level menu item
        self.new_item.add_command(label="Quản lý chuyên cần", command=self.open_quan_ly_chuyen_can)

        self.new_item.add_command(label="Quản lý điểm số", command=self.open_quan_ly_diem_so)
        
        self.new_item.add_command(label="Quản lý học sinh", command=self.open_quan_ly_hoc_sinh)
        
        self.new_item.add_command(label="Quản lý học tập", command=self.open_quan_ly_hoc_tap)
        
        self.new_item.add_command(label="Quản lý lớp học", command=self.open_quan_ly_lop_hoc)

        self.new_item.add_command(label="Quản lý chuyên cần", command=self.open_quan_ly_chuyen_can) 

        #Môn hóa
        self.new_item3 = Menu(self.menu, tearoff=0)
        self.new_item2.add_cascade(label="Hóa",menu=self.new_item3)
        self.new_item3.add_command(label="Tính số mol bằng khối lượng", command =self.open_tinh_so_mol_bang_khoi_luong)
        self.new_item3.add_command(label="Tính số mol bằng thể tích",command =self.open_tinh_so_mol_bang_the_tich)
        
        #môn toán
        self.new_item4 = Menu(self.menu, tearoff= 0)
        self.new_item2.add_cascade(label="Toán", menu=self.new_item4)
        self.new_item4.add_command(label="Tính phương trình bậc 1", command =self.open_tinh_phuong_trinh_bac_mot)
        
        self.new_item5 = Menu(self.menu, tearoff= 0)
        self.new_item4.add_command(label="Tính phương trình bậc 2", command =self.open_tinh_phuong_trinh_bac_hai)

        
        self.new_item6 = Menu(self.menu, tearoff= 0)
        self.new_item2.add_cascade(label="Vật lí", menu = self.new_item6)
        self.new_item6.add_command(label="Tính SVT", command =self.open_tinh_SVT)

        self.new_item7 = Menu(self.menu, tearoff= 0)

        self.new_item6.add_command(label="Đổi đơn vị", command =self.open_doiDonVi)
        # Frame to hold the content
        self.content_frame = tk.Frame(self.master)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

    #def open_chuyen_can(self):
        # Clear the current content frame
        #for widget in self.content_frame.winfo_children():
            #widget.destroy()
        # You can implement your Chuyên cần functionality here
        #app = quanLyDiemSo.quanLyDiemSo(self.content_frame)

    def open_quan_ly_chuyen_can(self):
        # Clear the current content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # Load the attendance management interface
        app = quanLyChuyenCan.quanLyChuyenCan(self.content_frame)

    def open_quan_ly_diem_so(self):
        # Clear the current content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # Load the attendance management interface
        app = quanLyDiemSo.quanLyDiemSo(self.content_frame)
    
    def open_quan_ly_hoc_sinh(self):
        # Clear the current content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # Load the attendance management interface
        app = quanLyHocSinh.quanLyHocSinh(self.content_frame)
    
    def open_quan_ly_hoc_tap(self):
        # Clear the current content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # Load the attendance management interface
        app = quanLyHocTap.quanLyHocTap(self.content_frame)
        
    def open_quan_ly_lop_hoc(self):
        # Clear the current content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # Load the attendance management interface
        app = quanLyLopHoc.quanLyLopHoc(self.content_frame)
    def open_tinh_so_mol_bang_khoi_luong(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # Load the attendance management interface
        app = tinhSoMolBangKhoiLuong.tinhSoMolBangKhoiLuong(self.content_frame)
    def open_tinh_so_mol_bang_the_tich(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # Load the attendance management interface
        app = tinhSoMolBangTheTich.tinhSoMolBangTheTich(self.content_frame)
    def open_tinh_phuong_trinh_bac_mot(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # Load the attendance management interface
        app = tinhPhuongTrinhBacMot.tinhPhuongTrinhBacMot(self.content_frame)    
    def open_tinh_phuong_trinh_bac_hai(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # Load the attendance management interface
        app = tinhPTbac2.tinhPhuongTrinhBac2(self.content_frame)  
    def open_tinh_SVT(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # Load the attendance management interface
        app = tinhSVT.tinhSVT(self.content_frame)
    def open_doiDonVi(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # Load the attendance management interface
        app = doiDonVi.doiDonVi(self.content_frame)    
if __name__ == "__main__":
    root = tk.Tk()
    app = MenuApp(root)
    root.mainloop()
