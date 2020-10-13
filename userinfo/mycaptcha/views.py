import json
from django.http import HttpResponse

from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

# 生成验证码
def generate_captcha():
    hashkey = CaptchaStore.generate_key()
    image_url = captcha_image_url(hashkey)
    mycaptcha = {"hashkey": hashkey, "image_url": image_url}
    return mycaptcha

# 刷新验证码
def refresh_captcha(request):
    return HttpResponse(json.dumps(generate_captcha()), content_type="application/json")

# 验证验证码
def verify_captcha(captchaStr:str, captchaHashkey:str):
    if captchaStr and captchaHashkey:
        try:
            get_captcha = CaptchaStore.objects.get(hashkey=captchaHashkey)
            return get_captcha.response == captchaStr.lower()
        except:
            return False
    else:
        return False 