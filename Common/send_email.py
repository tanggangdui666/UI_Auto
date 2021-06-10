# coding = utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.header import make_header


class SendMail:

    def __init__(self, mail_host):
        self.mail_host = mail_host

    def send(self, title, content, sender, auth_code, receivers,filename):
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message.attach(MIMEText(content, 'html', 'utf-8'))
        message['From'] = "{}".format(sender)
        message['To'] = ",".join(receivers)
        message["Subject"] = title
        # 构造附件1
        att1 = MIMEText(open(filename, 'rb').read(), 'html', 'utf-8')
        att1['Content-Type'] = 'application/octet-stream'
        att1['Content-Disposition'] = 'attachment;filename="lyg_ui_auto_report.html"'
        message.attach(att1)
        try:
            smtp_obj = smtplib.SMTP_SSL(self.mail_host, 465)  # 启用ssl发信，端口一般是465
            smtp_obj.login(sender, auth_code)  # 登录
            smtp_obj.sendmail(sender, receivers, message.as_string())
            print("Mail 发送成功")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # 第三方 SMTP 服务
    mail = SendMail("smtp.163.com")
    sender = "ggboytgg@163.com"
    # 收件人
    receivers = ['ggboytgg1@163.com','ggboytgg2@163.com']
    title = "邮件测试"
    content = """
    <a href="https://www.laoyuegou.com/">捞月狗官网 </a>
    """

    # 授权码不是邮箱登录密码，网易邮箱可以通过 "设置"->客户端授权密码，
    auth_code = "CJTKWQUKTDXNLOSP"
    mail.send(title, content, sender, auth_code, receivers,"/Users/lyg/Desktop/Python/Auto_MesUI/report/lyg_report/lyg_自动化测试报告2021-05-27_14:34:54.html")

