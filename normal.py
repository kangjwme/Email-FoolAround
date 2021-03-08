import smtplib
import random
from email.mime.text import MIMEText
from email.header import Header

#基本資訊調查
smtpaddress = input("SMTP伺服器(預設port為587)：")
sender = input("寄件人電子信箱：")
senderpasswd = input("寄件人電子信箱密碼：")
receiver = input("收件人電子信箱：")
subject = input("主旨：")
sendtext = input("想傳送的內容：")
#SMTP驗證，初始化
smtp=smtplib.SMTP(smtpaddress, 587)
smtp.ehlo()
smtp.starttls()
smtp.login(sender,senderpasswd)

#郵件寄件人、收件人設定
from_addr=sender
to_addr=receiver

#內文設定
msg = MIMEText(sendtext, 'plain', 'utf-8')
receiver
msg['From'] = Header(sender, 'utf-8')
msg['To'] =  Header(receiver, 'utf-8')


msg['Subject'] = Header(subject, 'utf-8')

status=smtp.sendmail(from_addr, to_addr, msg.as_string())#加密文件，避免私密信息被截取

if status=={}:
    print("郵件傳送成功!")
else:
    print("郵件傳送失敗!")
smtp.quit()
