from application import app
import random


@app.route('/randomphrase', methods=['GET'])
def ending():

	list = ['Cole','Ferenczy','Otonashi','Munster','Tepesh','Corvinus','Count','Petrova','Knight']
	
	return list[random.randrange(8)]