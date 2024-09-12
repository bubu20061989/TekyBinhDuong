import tkinter as tk
 
from tkinter import Menu
class menu:
    def __init__(self,master):
        self.master = master
        self.master.title("")
        self.master.geometry("400x400")
        #khởi tạo menu
        self.menu = Menu(master)
        self.master.config(menu=self.menu)
 #1       
        #Thêm mục
        self.new_item =Menu(self.menu,tearoff = 0)
        self.menu.add_cascade(label = "Chi tiêu",menu = self.new_item)
        self.new_item.add_separator()
        #Quản lí chi tiêu
        self.quan_li_chi_tieu =Menu(self.new_item,tearoff = 0)
        self.new_item.add_cascade(label = "Quản lí chi Tiêu",menu = self.quan_li_chi_tieu)
        
        self.quan_li_chi_tieu_ngay =Menu(self.quan_li_chi_tieu,tearoff = 0)
        self.quan_li_chi_tieu.add_cascade(label = "Ngày",menu = self.quan_li_chi_tieu_ngay)
        
        self.quan_li_chi_tieu_thang =Menu(self.quan_li_chi_tieu,tearoff = 0)
        self.quan_li_chi_tieu.add_cascade(label = "Tháng",menu = self.quan_li_chi_tieu_thang)
        
        self.quan_li_chi_tieu_nam =Menu(self.quan_li_chi_tieu,tearoff = 0)
        self.new_item.add_separator()
        self.quan_li_chi_tieu.add_cascade(label = "Năm",menu = self.quan_li_chi_tieu_nam)
        #Báo cáo chi tiêu
        self.bao_cao_chi_tieu =Menu(self.new_item,tearoff = 0)
        self.new_item.add_cascade(label = "Báo Cáo chi Tiêu",menu = self.bao_cao_chi_tieu)
        
        self.bao_cao_chi_tieu_ngay =Menu(self.bao_cao_chi_tieu,tearoff = 0)
        self.bao_cao_chi_tieu.add_cascade(label = "Ngày",menu = self.bao_cao_chi_tieu_ngay)
        
        self.bao_cao_chi_tieu_thang =Menu(self.bao_cao_chi_tieu,tearoff = 0)
        self.bao_cao_chi_tieu.add_cascade(label = "Tháng",menu = self.bao_cao_chi_tieu_thang)
        
        self.bao_cao_chi_tieu_nam =Menu(self.bao_cao_chi_tieu,tearoff = 0)
        self.new_item.add_separator()
        self.bao_cao_chi_tieu.add_cascade(label = "Năm",menu = self.bao_cao_chi_tieu_nam)
        
        
        
    
if __name__ == "__main__":
    root = tk.Tk()
    app = menu(root)
    root.mainloop()
    root.geometry()