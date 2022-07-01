import random
import string
from datetime import datetime

from flask import Blueprint, render_template, request
from flask_mail import Message
from exts import mail, db
from models import EmailCaptchaModel

bp = Blueprint("user",__name__,url_prefix="/user")

@bp.route("/login")
def login():
    return render_template("login.html")



@bp.route("/register")
def register():
    return render_template("register.html")


@bp.route("/captcha")
def send_mail():
    email = request.args.get("email")
    if not email:
        return 'error'

    base_str = string.ascii_letters + string.digits
    code = ''.join(random.sample(base_str,4))
    message = Message(
        subject="[小胖工具箱]注册验证码",
        recipients=['2625112940@qq.com'],
        body=f"【小胖工具箱】您的注册验证码为:{code},请不要把验证码告诉任何人！"
    )
    mail.send(message)
    captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
    if captcha_model:
        captcha_model.captcha = code
        captcha_model.create_time = datetime.now()
    else:
        captcha_model = EmailCaptchaModel(email=email,captcha = code)
        db.session.add(captcha_model)
    db.session.commit()
    return 'success'