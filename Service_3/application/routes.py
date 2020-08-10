from application import app
import random


@app.route('/randomphrase', methods=['GET'])
def ending():

	list = ['Cole','Ferenczy','Otonashi','Munster','Tepesh','Corvinus','Count','Petrova','Knight']
	# list = ['change on service 3a','change on service 3b','change on service 3c','change on service 3d','change on service 3e','change on service 3f','change on service 3g','change on service 3k','change on service 3l']
	
	return list[random.randrange(8)]