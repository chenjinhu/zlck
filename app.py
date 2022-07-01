import config
from flask import Flask
from exts import db,mail
from blueprints import qa_blueprint, user_blueprint
from flask_migrate import Migrate
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)
migrate = Migrate(app,db)
app.register_blueprint(qa_blueprint)
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run()
