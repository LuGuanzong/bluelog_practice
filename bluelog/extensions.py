# 扩展实例化，但并不传入程序实例

from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
ckeditor = CKEditor()
mail = Mail()
moment = Moment()
db = SQLAlchemy()