import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox


class vatli : 
    def __init__(self,master):
        self.master = master
        self.master.title("dragon")
        self.master.geometry('400x400')
        self.widthEntry=40
        
        self.label_nhap_so_can_doi = tk.Label(self.master,text="Nhập số cần quy đổi ")
        self.label_nhap_so_can_doi.place(x = 0 , y = 0)
        
        self.entry_nhap_so_can_doi = tk.Entry(self.master,width = self.widthEntry)
        self.entry_nhap_so_can_doi.place (x = 130,  y = 0)
        
        self.label_don_vi = tk.Label(self.master,text="Đơn vị")
        self.label_don_vi.place(x=0,y=60)

        n = tk.StringVar() 
        self.entry_don_vi = ttk.Combobox(self.master, width = 37, textvariable = n) 
        
        # Adding combobox drop down list 
        self.entry_don_vi['values'] = ('km',  
                                'm',
                                'dm',
                                'm',)
        
        self.entry_don_vi.place(x =130,y=60)
        self.entry_don_vi.current()
        
        self.label_don_vi_can_doi = tk.Label(self.master,text="Đơn vị cần đổi")
        self.label_don_vi_can_doi.place(x=0,y=120)

        n = tk.StringVar() 
        self.entry_don_vi_can_doi = ttk.Combobox(self.master, width = 37, textvariable = n) 
        
        # Adding combobox drop down list 
        self.entry_don_vi_can_doi['values'] = ('km',  
                                'm',
                                'dm',
                                'cm',)
        
        self.entry_don_vi_can_doi.place(x =130,y=120)
        self.entry_don_vi_can_doi.current()
        
        self.button_doi = tk.Button(self.master, text = "Đổi ", command= self.donvi,width=20)
        self.button_doi.place(x=220, y=160)
        
    def donvi (self):


        if not self.entry_nhap_so_can_doi.get(): 
            messagebox.showerror(title='Error', message='Bạn chưa nhập đủ dữ liệu')
        else:
            soQuiDoi = float(self.entry_nhap_so_can_doi.get())
            ketQuaQuiDoi = 0
           
            don_vi = self.entry_don_vi.get()
            don_vi_can_doi = self.entry_don_vi_can_doi.get()
            print(don_vi)
            print(don_vi_can_doi)
            if don_vi == 'km' and don_vi_can_doi == 'm':
                ketQuaQuiDoi =  soQuiDoi*1000
            elif don_vi == 'm' and don_vi_can_doi == 'km':
                ketQuaQuiDoi = soQuiDoi/1000
            elif don_vi == 'm' and don_vi_can_doi == 'dm':
                ketQuaQuiDoi = soQuiDoi*10
            elif don_vi == 'dm' and don_vi_can_doi == 'm':
                ketQuaQuiDoi = soQuiDoi/10
            elif don_vi == 'dm' and don_vi_can_doi == 'cm':
                ketQuaQuiDoi = soQuiDoi*10
            elif don_vi == 'cm' and don_vi_can_doi == 'dm':
                ketQuaQuiDoi = soQuiDoi/10
            elif don_vi == 'km' and don_vi_can_doi == 'dm':
                ketQuaQuiDoi = soQuiDoi*10000
            elif don_vi == 'dm' and don_vi_can_doi == 'km':
                ketQuaQuiDoi = soQuiDoi/10000
            elif don_vi == 'km' and don_vi_can_doi == 'cm':
                ketQuaQuiDoi = soQuiDoi*100000
            elif don_vi == 'cm' and don_vi_can_doi == 'km':
                ketQuaQuiDoi = soQuiDoi/100000
            elif don_vi == 'm' and don_vi_can_doi == 'cm':
                ketQuaQuiDoi = soQuiDoi*100
            elif don_vi == 'cm' and don_vi_can_doi == 'm':
                ketQuaQuiDoi = soQuiDoi/100
            
                
                
                
            messagebox.showerror(title='Kết quả', message=str(ketQuaQuiDoi))
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    

            
        
    

        
        
            
            
        
if __name__=="__main__":

    root = tk.Tk()
    app = vatli(root)
    root.mainloop()