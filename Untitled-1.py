import xlsxwriter
#tạo một workbook và thêm một worksheet.
workbook = xlsxwriter.Workbook('thongtinkhachhang.xlsx')
worksheet = workbook.add_worksheet()
thongtinkhachhang = (
    ['TranHoangC', 'tranhoangc@gmail.com'],
    ['TranVanA', 'tranvana@gmail.com'],
    ['NguyenVanB', 'nguyenvanb@gmail.com'],
    ['TranVanC', 'tranvanc2284@gmail.com'],
)#dien thong tin khach hang.    
hang = 0
cot = 0
for tenkhachhang, gmail in (thongtinkhachhang):
    worksheet.write(hang, cot, tenkhachhang)
    worksheet.write(hang, cot + 1, gmail)
    hang += 1
workbook.close()
import smtplib, ssl
gmail_cua_ban=input("mơi bạn nhập điạ chỉ gmail của bạn:")
password = input("nhập mật khẩu của bạn:")
noi_dung_tin_nhan =input("mơi bạn nhập nội dung tin nhắn: ")
''' gửi email cho 1 người:'''
gmail_khach_hang = input("mơi bạn nhập địa chỉ gmail khách hàng:")
port = 465
smtp_server = "smtp.gmail.com"
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  
    server.starttls(context=context) 
    server.ehlo()  
    server.login(gmail_cua_ban, password)
    server.sendmail(gmail_cua_ban, gmail_khach_hang , noi_dung_tin_nhan)
"""giửi gmail cho nhiều người"""
for tenkhachhang, gmail in thongtinkhachhang:
    server.sendmail(gmail_cua_ban, gmail ,noi_dung_tin_nhan.format( nguoinhan=gmail, gmail_cua_ban = gmail_cua_ban ))