from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


# 设置邮件服务器地址
smtpserver = 'smtp.163.com'
# 设置邮件服务器端口
port = 25

# 授权码
password = 'AVNCNFWSUJQEALFA'
# 发件人地址
sender = 'jingying0037@163.com'
# 收件人地址
receivers = 'jingying0037@163.com;wzy944454197@163.com;l15591464532@163.com'

'''创建邮件'''
# 创建邮件对象
mail = MIMEMultipart()
# 初始化发件人
mail['from'] = sender
# 初始化收件人
mail['to'] = receivers
# 添加主题
mail['subject'] = 'Ran之自动化测试报告'

'''添加附件'''
# 读取附件
path = r'D:\workspace\selenium\ranzhi\report\report_2021-01-11_16-59-09.html'
with open(path,'rb') as file:
    report = file.read()

# 对附件进行编码
attchment = MIMEText(report,'base64','utf-8')
# 设置附件的类型
attchment['Content-Type'] = 'application/octet-stream'
# 设置附件的处理方式
attchment['Content-Disposition'] = 'attchment;filename=%s'%path.split('\\')[-1]
# 添加附件
mail.attach(attchment)

'''添加正文'''
# 邮件正文
content = '''
<h3>Dear All,</h3>
<p>这是Ranzhi项目的测试报告，请您查收！</p>

<p>此致，</p>
<p>敬礼，Tom</p>
'''

# 对正文进行编码
body = MIMEText(content,'html','utf-8')
# 添加正文
mail.attach(body)

'''发送邮件'''
# 创建smtp对象
smtp = smtplib.SMTP()
# 连接邮件服务器
smtp.connect(smtpserver,port)
# 登陆服务器
smtp.login(sender,password)
# 发送邮件
smtp.sendmail(sender,receivers.split(';'),mail.as_string())
# 关闭服务器
smtp.close()
print('邮件发送完毕！')
