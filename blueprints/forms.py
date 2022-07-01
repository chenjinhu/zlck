import wtforms
from wtforms.validators import length,email,EqualTo

from models import EmailCaptchaModel, UserModel


class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=6,max=15)])
    email = wtforms.StringField(validators=[length(min=6,max=35)])
    captcha = wtforms.StringField(validators=[length(min=4,max=4)])
    password = wtforms.StringField(validators=[length(min=6,max=15)])
    repassword = wtforms.StringField(validators=[EqualTo("password")])

    def validate_email(self, field):
        email = field.data

        user_model = UserModel.query.filter_by(email=email).first()
        if user_model:
            raise wtforms.ValidationError("user exist")


    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if not captcha_model or captcha_model.captcha.lower() != captcha.lower():
            raise wtforms.ValidationError("captcha error")
