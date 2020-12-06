import yagmail

def send_mail(html_report):

    # 链接游戏服务器
    yag = yagmail.SMTP(user='454001372@qq.com', password='FangJiong900519_', host='smtp.qq.com')

    #邮件正文
    contents = ["你好"]

    #发送邮件
    yag.send("454001372@qq.com", "API接口自动化测试报告", contents, [html_report])

    yag.close()
