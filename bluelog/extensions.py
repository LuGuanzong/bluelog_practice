# 扩展实例化，但并不传入程序实例

from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
ckeditor = CKEditor()
login_manager = LoginManager()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


@login_manager.user_loader
def load_user(user_id):
    from bluelog.models import Admin
    user = Admin.query.get(int(user_id))
    return user


login_manager.login_view = 'auth.login'
login_manager.login_message = u'请先登录'
login_manager.login_message_category = 'warning'