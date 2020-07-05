from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/height_collector'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=Peso_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sucesso", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        print(email, Peso)
        if db.session.query(Data).filter(Data.email_ == email).count()== 0:
            data=Data(email,Peso)
            db.session.add(data)
            db.session.commit()
            media_height=db.session.query(func.avg(Data.height_)).scalar()
            media_height=round(media_height, 1)
            count = db.session.query(Data.height_).count()
            send_email(email,Peso, media_peso, conta)
            print(media_peso)
            return render_template("sucesso.html")
    return render_template('index.html', text="Parece que recebemos algo desse e-mail uma vez!")

if __name__ == '__main__':
    app.debug=True
    app.run(port=5005)
