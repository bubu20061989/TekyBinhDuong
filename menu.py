import tkinter as tk
from tkinter import Menu
import quanLyChuyenCan  # Import your class file
import quanLyDiemSo
import quanLyHocSinh
import quanLyHocTap
import quanLyLopHoc



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
        self.menu.add_cascade(label="Quản lý", menu=self.new_item)

        self.new_item.add_separator()


        
        # Add 'Quản lý chuyên cần' as another top-level menu item
        self.new_item.add_command(label="Quản lý chuyên cần", command=self.open_quan_ly_chuyen_can)

        self.new_item.add_command(label="Quản lý điểm số", command=self.open_quan_ly_diem_so)
        
        self.new_item.add_command(label="Quản lý học sinh", command=self.open_quan_ly_hoc_sinh)
        
        self.new_item.add_command(label="Quản lý học tập", command=self.open_quan_ly_hoc_tap)
        
        self.new_item.add_command(label="Quản lý lớp học", command=self.open_quan_ly_lop_hoc)


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



if __name__ == "__main__":
    root = tk.Tk()
    app = MenuApp(root)
    root.mainloop()
