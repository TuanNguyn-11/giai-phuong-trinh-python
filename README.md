# 📐 Giải Phương Trình Đa Thức (Bậc 1 - 4)

<p align="center">
  <img src="banner.png" alt="Banner HCMUTE - Khoa Điện - Điện Tử" width="600"/>
</p>

<p align="center">
  <b>Bài tập lớn môn Thực tập Lập trình với Python</b><br/>
  Trường Đại học Sư phạm Kỹ thuật TP. Hồ Chí Minh (HCMUTE)<br/>
  Khoa Điện - Điện Tử | Faculty of Electrical and Electronics Engineering
</p>

---

## 📝 Mô tả

Chương trình **Giải Phương Trình Đa Thức** cho phép người dùng giải các phương trình đa thức từ **bậc 1 đến bậc 4** thông qua giao diện đồ họa (GUI) được xây dựng bằng thư viện **Tkinter** của Python.

### ✨ Tính năng chính

- ✅ Giải phương trình bậc 1: `ax + b = 0`
- ✅ Giải phương trình bậc 2: `ax² + bx + c = 0`
- ✅ Giải phương trình bậc 3: `ax³ + bx² + cx + d = 0`
- ✅ Giải phương trình bậc 4: `ax⁴ + bx³ + cx² + dx + e = 0`
- ✅ Tìm **nghiệm thực** và **nghiệm phức**
- ✅ Tìm **điểm cực đại** và **cực tiểu** (từ bậc 2 trở lên)
- ✅ Giao diện trực quan, dễ sử dụng
- ✅ Kiểm tra và xử lý lỗi đầu vào

---

## 📁 Cấu trúc dự án

```
giai_pt-main/
│
├── main_ui.py       # File chính - Khởi chạy chương trình, tạo giao diện trang chủ
├── giaipt_ui.py     # Giao diện trang giải phương trình theo từng bậc
├── thuvien.py       # Thư viện hàm: tạo label, giải phương trình, tìm cực trị, in kết quả
├── banner.png       # Ảnh banner hiển thị trên trang chủ
├── FEEE.ico         # Icon ứng dụng (logo Khoa Điện - Điện Tử)
└── README.md        # Tài liệu hướng dẫn
```

---

## ⚙️ Yêu cầu hệ thống

- **Python** >= 3.7
- Các thư viện Python:
  - `numpy`
  - `sympy`
  - `tkinter` (có sẵn trong Python)

---

## 🚀 Hướng dẫn cài đặt và chạy

### 1. Clone repository

```bash
git clone https://github.com/TuanNguyn-11/giai-phuong-trinh-python.git
cd giai-phuong-trinh-python
```

### 2. Cài đặt thư viện cần thiết

```bash
pip install numpy sympy
```

### 3. Chạy chương trình

```bash
python main_ui.py
```

---

## 🖥️ Hướng dẫn sử dụng

1. **Chạy chương trình** bằng lệnh `python main_ui.py`
2. **Chọn bậc phương trình** từ danh sách thả xuống (bậc 1 → bậc 4)
3. **Nhấn nút "Chọn"** để chuyển sang trang giải phương trình
4. **Nhập các hệ số** (a, b, c, d, e) tương ứng với bậc đã chọn
5. **Nhấn "Tìm nghiệm"** để xem kết quả nghiệm và điểm cực trị
6. **Nhấn "Làm mới"** để xóa dữ liệu và nhập lại
7. **Nhấn "Trang chính"** để quay về trang chủ

---

## 🛠️ Công nghệ sử dụng

| Công nghệ | Mục đích |
|---|---|
| **Python** | Ngôn ngữ lập trình chính |
| **Tkinter** | Xây dựng giao diện đồ họa (GUI) |
| **NumPy** | Tính toán nghiệm phương trình đa thức (`numpy.roots`) |
| **SymPy** | Tính đạo hàm và tìm điểm cực trị |

---

## 👤 Tác giả

- **Phan Ngọc Tuấn Nguyên**
- Sinh viên Trường Đại học Sư phạm Kỹ thuật TP. Hồ Chí Minh (HCMUTE)
- Khoa Điện - Điện Tử

---

## 📄 Giấy phép

Dự án này được phát triển phục vụ mục đích học tập.
