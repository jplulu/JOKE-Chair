from flask_sqlalchemy import SQLAlchemy
from backend.webapi import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql:///posturechair'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)