from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP


def main():
    sender = 'chenqingliang131@163.com'
    receivers = ['394869042@qq.com']
    message = MIMEText('用Python发送邮件的示例代码', 'plain', 'utf-8')
    message['From'] = Header('陈庆良', 'utf-8')
    message['To'] = Header('陈庆良收', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.163.com')
    smtper.login(sender, 'hinkleung123')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送！')


if __name__ == '__main__':
    main()
