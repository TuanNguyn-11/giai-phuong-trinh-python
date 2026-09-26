from tkinter import *
from tkinter.messagebox import *
import numpy as np
from sympy import symbols, real_roots
import thuvien

class giai_UI:
    def __init__(self, root, num_input):
        self.root = root
        self.num_input = num_input
        self.entry = [0] * self.num_input
        self.output = [0] * self.num_input
        self.heso = [0] * self.num_input
        # Code tao tieu de cua trang
        self.name_title = f'Giải phương trình bậc {self.num_input - 1}:'
        for i in range(self.num_input - 2):
            self.name_title += f' {chr(97 + i)}x^{self.num_input - 1 - i} +'
        else:
            self.name_title += f' {chr(97 + self.num_input - 2)}x + {chr(97 + self.num_input - 1)} = 0'
        # Ham tao trang giai phuong trinh
        self.create_ui()

    def create_ui(self):
        title = Label(text = self.name_title, font = ('Times New Roman', 16, 'bold'))
        title.place(x = 25, y = 0)
        thuvien.create_label(self.entry, self.output, self.num_input)
        
        self.giai_button = Button(text="Tìm nghiệm", font=('Times New Roman', 16), command=self.sovle_solution, width=10)
        self.giai_button.place(x=430, y = 88)
        self.xoa_button = Button(text="Làm mới", font=('Times New Roman', 16), command= self.delFunc, width=10)
        self.xoa_button.place(x=430, y = 133)
        self.diemcuctri = Label(font=('Times New Roman', 16))
        # Neu phuong trinh bac 3 hoac bac 4, cho hien thi diem cuc tri o ben phai nghiem
        if self.num_input == 4 or self.num_input == 5:
            self.diemcuctri.place(x= 250, y= 50 + self.num_input * 40)
        else:
        # Con lai hien thi o ben duoi nghiem
            self.diemcuctri.place(x= 20, y= 30 + self.num_input * 70)

    def sovle_solution(self):
        thuvien.sovle_solution(self.num_input, self.heso, self.entry, self.output, self.diemcuctri)

    def delFunc(self):
        thuvien.refresh(self.num_input, self.entry, self.output, self.diemcuctri)
