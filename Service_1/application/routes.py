from application import app
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
import random
import os
from os import environ 

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_DB_NAME')

db = SQLAlchemy(app)

class nickname_gen(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    response = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return ''.join([
            'ID: ', str(self.id), '\n',
            'response: ', str(self.response)
        ])

@app.route('/', methods=['GET','POST'])
def home():
    response = requests.get('http://service_4:5003/randomword')
    print(response)
    sentence = response.text
    new_input = nickname_gen(
        response=sentence
    )
    nickname_data = nickname_gen.query.order_by(nickname_gen.id.desc()).limit(5)
    print(sentence)
    db.session.add(new_input)
    db.session.commit()   
    return render_template('index.html', sentence = sentence, nickname_gen = nickname_data, title = 'Home')
