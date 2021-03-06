from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
# from main.model.Recipe import Recipe,Ingredient
# from main.model.user import User,UserInf


db_url = "sqlite:///app.db"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True
app.secret_key = os.urandom(24)
db = SQLAlchemy(app)

db.init_app(app)

#
# def db_init():
#     db.drop_all()  # 每次运行，先删除再创建
#     db.create_all()
#
#     admin = User(username='Nicky', password='z5229785', email='z5229785@ad.unsw.edu.au.com')
#     db.session.add(admin)
#
#     guestes = [User(username='JiaqiLi', password='z5239854', email='z5239854@ad.unsw.edu.au.com'),
#                User(username='XiaoshuangSun', password='z5276878', email='z5276878@ad.unsw.edu.au.com'),
#                User(username='YarongWang', password='z5231036', email='z5231036@ad.unsw.edu.au.com'),
#                User(username='GuanxingLi', password='z5240327', email='z5240327@ad.unsw.edu.au.com')]
#     db.session.add_all(guestes)
#     db.session.commit()
#
#     Rec = Recipe(R_name='bouilli', user_id=1, R_description='Porm,onion,ginger,garlic', R_category='breakfast',
#                  R_calorie=10)
#     db.session.add(Rec)
#
#     Rec = [Recipe(R_name='Python', user_id=1, R_description='Need,find ,good ,Python ,tutorial,web', R_calorie=20),
#            Recipe(R_name='lawn', user_id=1, R_description='Find,out,some,tools', R_calorie=33)]
#     #
#     db.session.add_all(Rec)
#     print('datbase init done!')

#
