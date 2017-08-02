import smtplib
from email.mime.text import MIMEText

import getpass
password = ''

fromEmail = ""
toEmail = ""
 
contents = """안녕하세요 입니다
본 메일은 python으로 보내는 자동화 메일 입니다"""
message = MIMEText(contents, _charset='utf-8')
 
message["Subject"] = "pyhon"
message["From"] = fromEmail
message["To"] = toEmail
 
s = smtplib.SMTP("smtp.naver.com", )
s.login("", password)
s.sendmail(fromEmail, toEmail, message.as_string())
s.quit()


