HOSTNAME = "localhost"
PORT = "3306"
DATABASE = "zlckqa"
USERNAME = "root"
PASSWORD = "123456"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY="QQQ1111as5d1as65d4a65d4q68341641653e165d1a63s1fc3z2x 0.0z"


# EmailConfig

MAIL_SERVER  = "smtp.qq.com"
MAIL_PORT =465
MAIL_USE_TLS = False
MAIL_USE_SSL  = True
MAIL_DEBUG = True
MAIL_USERNAME = "2625112940@qq.com"
MAIL_PASSWORD  = "xjczxyylqnnjdhfi"
MAIL_DEFAULT_SENDER  = "2625112940@qq.com"