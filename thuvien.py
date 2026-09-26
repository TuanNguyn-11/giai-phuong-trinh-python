from tkinter import *
from tkinter import *
from tkinter.messagebox import *
import numpy as np
from sympy import real_roots, symbols

def create_label(entry, output, num_input):
    mess = [0]* num_input
    for i in range(num_input):
        # Trong ma ASCII: 97 la a, 98 la b,...
        mess[i] = Label(text=f'Nhập {chr(97 + i)} = ', font=('Times New Roman', 16))
        mess[i].place(x = 80, y = (30 + i * 40))
        entry[i] = Entry(font=('Times New Roman', 16), width = 17)
        entry[i].place(x = 190, y = (33 + i* 40))
        output[i] = Label(font= ('Times New Roman', 16))
        output[i].place(x=20, y = (45 + num_input * 35 + i * 30))

def sovle_solution(num_input, heso, entry, output, diemcuctri):
    try:
        # Ham try - expect de loai bo du lieu vao khong dung loai
        for i in range(num_input):
            heso[i] = float(entry[i].get())
        if heso[0] == 0: # Loai bo du lieu a == 0
            refresh(num_input, entry, output, diemcuctri)
            showwarning(title='Lỗi', message='Vui lòng nhập giá trị a khác 0!')
        else:
            ketqua = np.roots(heso)
            if num_input == 2:
                cucdai, cuctieu = '', '' # PTB1 khong co cuc tri nen de xau rong
                inketqua(num_input, heso, ketqua, output, cucdai, cuctieu, diemcuctri)
            else:
                cucdai, cuctieu = timcuctri(heso, num_input)
                inketqua(num_input, heso, ketqua, output, cucdai, cuctieu, diemcuctri)
    except ValueError:
        refresh(num_input, entry, output, diemcuctri)
        showwarning(title='Lỗi', message='Vui lòng nhập đúng định dạng!')

def timcuctri(heso, num_input):
    # Cac dong lenh tao ham so co dang f = ax^2 + bx^1 + cx^0
    x = symbols('x')
    f = 0
    for i in range(num_input):
        f += heso[i] * x ** (len(heso)- 1 - i)
    # Tim dao ham cap 1 va cap 2, va tim cuc tri
    diff_1 = f.diff(x)
    diff_2 = diff_1.diff(x)
    cuctri = real_roots(diff_1)
    cuctieu = []
    cucdai = []
    # Kiem tra cuc dai hay cuc tieu
    for val in cuctri:
        if diff_2.subs(x, val) > 0:
            cuctieu.append((val, f.subs(x, val)))
        else:
            cucdai.append((val, f.subs(x, val)))
    # Chuyen ket qua ve dang string
    diemcuctieu='\n'.join([f"({toado[0].evalf():.2f}, {toado[1].evalf():.2f})" for toado in cuctieu])
    diemcucdai='\n'.join([f"({(toado[0].evalf()):.2f}, {(toado[1].evalf()):.2f})" for toado in cucdai])
    return diemcucdai, diemcuctieu

def refresh(num_input, entry, output, diemcuctri):
    # Xoa bo du lieu trong entry, output va diemcuctri
    for i in range(num_input):
        entry[i].delete(0, END)
        output[i].config(text='')
    diemcuctri.config(text='')

def inketqua(num_input, heso, ketqua, output, cucdai, cuctieu, diemcuctri):
    # Chuyen doi he so thanh dang string
    for i in range(1, num_input):
        if heso[i] < 0:
            heso[i] = '- ' + str(-heso[i])
        elif heso[i] >= 0: 
            heso[i] = '+ ' + str(heso[i])
    # Tao tieu de cho ket qua  
    title = 'PT:'
    for i in range(num_input - 2):
        title += f' {heso[i]}x^{num_input - 1 - i}'
    title += f' {heso[num_input - 2]}x {heso[num_input - 1]} = 0 có nghiệm:'
    output[0].config(text = title)
    # In ket qua, lam tron 2 chu so thap phan
    for i in range(0,num_input - 1):
        if ketqua[i].imag == 0:
            output[i + 1].config(text=f"x{i+1} = {float(np.round(ketqua[i],2).real)}")
        else:
            output[i + 1].config(text=f"x{i+1} = {complex(np.round(ketqua[i],2))}")
    # In diem cuc tri        
    if cuctieu or cucdai:
        diemcuctri.config(text=f'Các điểm cực tiểu:\n{cuctieu}\nCác điểm cực đại:\n{cucdai}')
    else:
        diemcuctri.config(text=f'Không có điểm cực trị.')