import tkinter as tk
from tkinter import Menu
import quanLyChuyenCan  # Import your class file
import quanLyDiemSo



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

        # Add 'Chuyên cần' as a top-level menu item
        self.new_item.add_command(label="Chuyên cần", command=self.open_chuyen_can)
        
        # Add 'Quản lý chuyên cần' as another top-level menu item
        self.new_item.add_command(label="Quản lý chuyên cần", command=self.open_quan_ly_chuyen_can)

        self.new_item.add_command(label="Quản lý điểm số", command=self.open_quan_ly_diem_so)


        # Frame to hold the content
        self.content_frame = tk.Frame(self.master)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

    def open_chuyen_can(self):
        # Clear the current content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # You can implement your Chuyên cần functionality here
        app = quanLyDiemSo.quanLyDiemSo(self.content_frame)

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



if __name__ == "__main__":
    root = tk.Tk()
    app = MenuApp(root)
    root.mainloop()
