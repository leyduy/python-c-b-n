""" Cú pháp của if-elif-else
    if biểu_thức_điều_kiện_01:
        các câu lệnh cần chạy nếu biểu_thức_điều_kiện_01 là Đúng (True)
    elif biểu_thức_điều_kiện_02:
        các câu lệnh cần chạy nếu biểu_thức_điều_kiện_02 là Đúng (True)
    else:
        các câu lệnh cần chạy nếu các biểu_thức_điều_kiện ở trên đềy là Sai (False)
"""
""" Bài tập về nhà:
Bài 1. Lập chương trình thực hiện công việc sau:
    Nhập ba số a, b, c bất kì từ bàn phím
    Giải nghiệm phương trình bậc 2: ax^2 + bx + c = 0  (Kể cả trường hợp a=0)"""
a=float(input())
b=float(input())
c=float(input())
if a!=0:
    denta=float(b**2-4*a*c)
    if denta > 0:
        x1=float((-b-denta**1/2)/2*a)
        print('x1')
        x2=float((-b+denta**1/2)/2*a)
        print('x2')
    elif denta < 0:
        x=float(-b/2*a)
        print('x')
    else:
        print('ptvn')
else:
    if b!=0:
        x=float(-c/b)
        print('x')
    if b==0 or c!=0:
        print('ptvn')
    elif b==0 or c==0:
        print('ptvsn')
        