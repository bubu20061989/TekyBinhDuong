import tkinter as tk
from tkinter import Menu
import tinhSoMolBangTheTich
import tinhSoMolBangKhoiLuong
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
        self.menu.add_cascade(label="Môn", menu=self.new_item)
        # self.new_item.add_cascade(label="Tính số mol",new_item=self.new_item)
        self.new_item.add_separator()


        
        # Add 'Quản lý chuyên cần' as another top-level menu item
        self.new_item.add_command(label="Khối lượng", command=self.open_tinh_so_mol_bang_khoi_luong)

        self.new_item.add_command(label="Thể tích", command=self.open_tinh_so_mol_bang_the_tich)
        
    def open_tinh_so_mol_bang_khoi_luong(self):
        # Clear the current content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # Load the attendance management interface
        app = tinhSoMolBangKhoiLuong.tinhSoMolBangKhoiLuong(self.content_frame)
    
    def open_tinh_so_mol_bang_the_tich(self):
        # Clear the current content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # Load the attendance management interface
        app = tinhSoMolBangTheTich.tinhSoMolBangTheTich(self.content_frame)
        
    
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = MenuApp(root)
    root.mainloop()