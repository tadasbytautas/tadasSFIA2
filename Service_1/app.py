from application import app
from os import environ
# from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy(app)

# app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
#                                         environ.get('MYSQL_USER') + \
#                                         ':' + \
#                                         environ.get('MYSQL_PASSWORD') + \
#                                         '@' + \
#                                         environ.get('MYSQL_HOST') + \
#                                         ':' + \
#                                         environ.get('MYSQL_PORT') + \
#                                         '/' + \
#                                         environ.get('MYSQL_DB_NAME')

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')

