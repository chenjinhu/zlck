from datetime import datetime

from exts import db


class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(100),nullable=False,unique = True)
    captcha = db.Column(db.String(10),nullable=False)
    create_time = db.Column(db.DateTime,nullable=False,default=datetime.now)





