from application import app
import random


@app.route('/randomphrase', methods=['GET'])
def beginning():

	# list = ['Brainsucker','Lionel','Grabber','Riley','Crawler','Matterslurper','Abomination','Lurker','Adolf']
	list = ['change on service 2a','change on service 2b','change on service 2c','change on service 2d','change on service 2e','change on service 2f','change on service 2g','change on service 2k','change on service 2l']
	
	return list[random.randrange(8)]