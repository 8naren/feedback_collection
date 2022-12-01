from flask_sqlalchemy import SQLAlchemy
from  flask import Flask



app=Flask(__name__)

db=SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{username}:{password}@{server}/mydata".format("root", "Amar@18250113","localhost")

class Feedback(db.Model):
    __tablename__="feedback"
    id=db.Column(db.Integer,primary_key=True)
    customer=db.Column(db.String(200),unique=True)
    dealer=db.Column(db.String(200))
    rating=db.Column(db.Integer)
    comments=db.Column(db.Text())

if __name__ =="__main__":
    app.debug=True
    app.run()