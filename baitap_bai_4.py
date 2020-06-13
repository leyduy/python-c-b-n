#Bài 00: Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc.
s=[1,2,3,4,5,6,7,8,9]
p=list(s[0:5])
print(p)
#Bài 01: Viết chương trình tính tổng, tích của các phần tử trong một list.
s=[1,2,3,4,5,6,7]
#s=['anh','yeu','em'] 
j=0
tong=0 
for i in range(1,s):
    
    while j<s:
        tong+=s[j]
        j=j+1
        print(tong)
#tong=sum(s)
#print("\n tong ca phan tu la",tong)

    
