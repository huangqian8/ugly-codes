import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

 
# 第三方 SMTP 服务
mail_host = "smtp.aaa.com"  # SMTP服务器
mail_user = "aaa@aaa.com"  # 用户名
mail_pass = "PASSWORD"  # 密码
 
sender = mail_user  # 发件人邮箱
receivers = ['bbb@bbb.com']  # 接收人邮箱 

title = 'Python 自动发送邮件'  # 邮件主题

# 邮件正文
content = '''
你好，这是一封由 Python 自动发送的邮件。
该邮件仅作为测试使用，如果影响到了您的正常使用，请忽视！！！
'''
txt = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码

message = MIMEMultipart()
message.attach(txt)
message['Subject'] = title
message['From'] = "{}".format(sender)
message['To'] = ",".join(receivers)
 
try:
    smtpObj = smtplib.SMTP()
    smtpObj = smtplib.SMTP_SSL(mail_host, '465')  # 启用SSL发信, 端口一般是465
    smtpObj.login(mail_user, mail_pass)  # 登录验证
    smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
    smtpObj.quit() 
    print("邮件发送成功")
except smtplib.SMTPException as e:
	print('邮件发送失败: ' + e)