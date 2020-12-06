from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib

class Mail:
    def send_mail(self, html_report):
        # 邮件主题
        subject = '你好，python'

        # #发送HTML类型邮件
        # msg = MIMEText('<html>你好</html>', 'html', 'utf-8')
        # msg['Subject'] = Header(subject, 'utf-8')
        try:
            # 邮件附件
            mail_body = open(html_report, "rb").read()

            att = MIMEText(mail_body, 'GBK', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="text.html"'

            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg.attach(att)

            # 发送邮件
            smtp = smtplib.SMTP()
            smtp.connect("smtp.qq.com")
            smtp.login("454001372@qq.com", "FangJiong900519_")
            smtp.sendmail("454001372@qq.com", "454001372@qq.com", msg.as_string())
            smtp.quit()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    Mail().send_mail()
