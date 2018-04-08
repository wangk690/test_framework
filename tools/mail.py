
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror, error
from tools.log import Log

class Email:
    '''
    邮件类。用来给指定用户发送邮件，可指定多个收件人，可带附件
    '''
    log = Log()
    def __init__(self, server, sender, password, receiver, title, message=None, path=None):
        '''
        初始化Email

        server: smtp服务器，必填
        sender: 发件人，必填
        password: 发件人密码，必填
        receiver: 收件人。多收件人用“;”隔开，必填
        title：邮件标题，必填
        message: 邮件正文，非必填
        path: 附件路径，可传入list(多附件)或str(单附件)，非必填
        '''
        self.title = title
        self.message = message
        self.files = path

        self.msg = MIMEMultipart('related')

        self.server = server
        self.sender = sender
        self.receiver = receiver
        self.password = password

    def _attach_file(self, att_file):
        '''将单个文件添加到附件列表中'''
        att = MIMEText(open('%s' % att_file,'rb').read(), 'palin', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]
        self.msg.attach(att)
        self.log.info('attach file {}'.format(att_file))

    def send(self):
        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        #邮件正文
        if self.message:
            self.msg.attach(MIMEText(self.message))


        #添加附件，支持多个附件(传入list)
        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self._attach_file(f)

            elif isinstance(self.files, str):
                self._attach_file(self.files)
                
        #连接服务器并发送
        try:
            smtp_server = smtplib.SMTP(self.server) #连接服务器
        except Exception as e:
            self.log.exception('发送邮件失败,无法连接到SMTP服务器，检查网络以及SMTP服务器. %s', e)
        else:
            try:
                smtp_server.login(self.sender, self.password)
            except smtplib.SMTPAuthenticationError as e:
                self.log.exception('用户名密码验证失败！%s' %e)
            else:
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())  # 发送邮件
            finally:
                smtp_server.quit()  # 断开连接
                self.log.info('发送邮件"{0}"成功! 收件人：{1}。如果没有收到邮件，请检查垃圾箱，'
                            '同时检查收件人地址是否正确'.format(self.title, self.receiver))



        