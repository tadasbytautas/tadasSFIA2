from application import app
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
import random
import os 

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

class nickname_gen(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    response = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return ''.join([
            'ID: ', str(self.id), '\r\n',
            'response: ', str(self.response)
        ])

@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service_4:5003/randomword')
    print(response)
    sentence = response.text
    post_data = nickname_gen.query.all()    
    return render_template('index.html', sentence = sentence, title = 'Home', post=post_data)
