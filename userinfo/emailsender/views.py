import datetime, hashlib
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from userinfo.emailsender import models as email_models

def hash_code(value):
    hashvalue = hashlib.sha256()
    hashvalue.update(str(value).encode())
    return hashvalue.hexdigest()

def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code((user.username, now))
    email_models.ConfirmString.objects.create(code=code, user=user)
    return code

def send_email(email, code):
    subject = '来自TLCAS-顶会论文分析系统的注册确认邮件'

    text_content = '''感谢注册TLCAS，这里是顶会论文分析系统，\
                    如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''

    html_content = '''
                    <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>TLCAS</a></p>
                    <p>这里是顶会论文分析系统</p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
                    '''.format('https://www.meetinganalysis.top', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
