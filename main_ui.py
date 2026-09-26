from tkinter import *
from tkinter import ttk, messagebox
from giaipt_ui import giai_UI

class Trang_khoi_dau:
    # Ham tao cua so
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x400')
        self.root.title('Giải Phương Trình')
        self.root.resizable(False, False)
        self.banner_path = PhotoImage(file='banner.png')
        self.root.iconbitmap('FEEE.ico')
        self.equation_values = ['Phương trình bậc 1', 'Phương trình bậc 2', 'Phương trình bậc 3', 'Phương trình bậc 4']
        self.equation_combo = None

    # Ham tao trang khoi dau
    def start_window(self):
        self.banner_label = Label(self.root, image=self.banner_path)
        self.banner_label.place(x=0,y=0)
        self.message_label = Label(self.root, text='Chọn bậc của phương trình:', font=('Times New Roman', 16, 'bold'))
        self.message_label.place(x= 175, y = 130)
        self.equation_combo = ttk.Combobox(self.root, values=self.equation_values, font=('Times New Roman', 16))
        self.equation_combo.place(x= 175, y = 200)
        self.choose_button = Button(self.root, text= 'Chọn', font=('Times New Roman', 16), command=self.choose_equation)
        self.choose_button.place(x=270, y= 310)
        self.return_button = Button(self.root, text='Trang chính', font=('Times New Roman', 16), command=self.return_home)
        self.return_button.place(x= 480, y= 355)

    # Ham chon bac phuong trinh
    def choose_equation(self):
        equation = self.equation_combo.get()
        for i in range(len(self.equation_values)):
            num_input = 2 + i # PTB1 can nhap 2 he so, PTB2 can nhap 3 he so,... 
            if equation == self.equation_values[i]:
                # Xoa tat ca phan tu trong cua so roi tao cua so giai phuong trinh
                self.delete_window()
                giaipt = giai_UI(self.root, num_input)
                
    def delete_window(self):
        # Ham winfo_children() goi cac phan tu trong cua so duoi dang list, destroy() de xoa phan tu
        for widget in self.root.winfo_children():
            widget.destroy()
        # Sau khi xoa trang thi tao nut tro ve trang chinh
        self.return_button = Button(self.root, text='Trang chính', font=('Times New Roman', 16), command=self.return_home)
        self.return_button.place(x= 480, y= 355)

    def return_home(self):
        # Xoa tat ca phan tu roi goi lai trang khoi dau
        self.delete_window()
        self.start_window()

    # Ham chay chuong trinh
    def run_program(self):
        self.start_window()
        self.root.mainloop()

if __name__ == '__main__':
    app = Trang_khoi_dau()
    app.run_program()
