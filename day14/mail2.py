"""
如果要发送带有附件的邮件，那么可以按照下面的方式进行操作。
"""
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP


def main():
    # 创建一个带附件的邮件消息
    message = MIMEMultipart()

    # 创建文本内容
    text_content = MIMEText('附件中有本月数据请查收', 'plain', 'utf-8')
    message['Subject'] = Header('本月数据', 'utf-8')
    # 将文本内容添加到邮件消息对象中
    message.attach(text_content)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('res/hello.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment;filename=hello.txt'
        message.attach(txt)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('res/汇总数据.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment;filename=month-data.xlsx'
        message.attach(xls)

    # 创建SMTP对象
    smtper = SMTP('smtp.163.com')
    sender = 'chenqingliang131@163.com'
    receivers = ['394869042@qq.com']
    smtper.login(sender, 'hinkleung123')
    smtper.sendmail(sender, receivers, message.as_string())
    smtper.quit()
    print('邮件发送！')


if __name__ == '__main__':
    main()
