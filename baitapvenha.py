
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
        print(x1)
        x2=float((-b+denta**1/2)/2*a)
        print(x2)
    elif denta == 0:
        x=float(-b/2*a)
        print(x)
    else:
        print('ptvn')
else:
    if b!=0:
        x=float(-c/b)
        print(x)
    if b==0 or c!=0:
        print('ptvn')
    elif b==0 or c==0:
        print('ptvsn')
        """Bài 2. Lập chương trình tính các tổng sau:
    S_1 = 1 + x + x^2 + x^3 + ... + x^n
    S_2 = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n
    S_3 = 1 + \dfrac{x}{1!} + \dfrac{x}{2!} + ... + \dfrac{x^n}{n!}
    Trong đó, n là số nguyên dương và x là một số thực bất kì. Cả 2 đều được nhập từ bàn phím"""
n=int(input())
x=float(input())
while n>0:
    for i in range(0,n,1):
        t=float(x**i)
        s_1+=float(t)
        print(s_1)
        t2=float((-1)**i*x**i)
        s_2+=t2
        print(s_2)
    break
'''Bài 3. Lập trình thực hiện các công việc sau:
    Nhập 3 số a, b, c bất kì
    Hãy kiểm tra xem ba số đó có phải là độ dài của các cạnh của một tam giác hay không? 
    Nếu đúng là tam giác thì xác định là tam giác vuông hay không?'''
a=float(input())
b=float(input())
c=float(input())
if a+b<c or a+c<b or b+c<a:
    print('3 so tren ko tao thanh 1 tam giac:')
else:
    print('3 so tren tao thanh 1 tam giac:')
    if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b :
        print('3 so tren tao thanh 1 tam giac vuong:')
    else:
        print('3 so tren ko tao thanh tam giac vuong')