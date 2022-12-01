
from flask import render_template,request,Flask
from flask_sqlalchemy import SQLAlchemy
from model import db,Feedback
import smtplib

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///mydata.db" 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit",methods=["POST"])
def submit():
    if request.method=="POST":
        customer=request.form["customer"]
        dealer=request.form["dealer"]
        rating=request.form["rating"]
        comments=request.form["comments"]
        #print(customer,dealer,rating,comments)
        if customer=="" or  dealer=="" or rating=="":
            return render_template("index.html",message="pls entr the req feilds")
        #return render_template("success.html")
        if db.session.query(Feedback).filter(Feedback.customer==customer).count()==0:
            data=Feedback(customer,dealer,rating,comments)
            db.session.add(data)
            db.session.commit()

            return render_template("success.html")
        return render_template("index.html",message="you have aldy entr te dtls")


if __name__ =="__main__":
    app.debug=True
    app.run()