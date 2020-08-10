from application import app
import random


@app.route('/randomphrase', methods=['GET'])
def beginning():

	# list = ['Brainsucker','Lionel','Grabber','Riley','Crawler','Matterslurper','Abomination','Lurker','Adolf']
	list = ['change on service 1a','change on service 1b','change on service 1c','change on service 1d','change on service 1e','change on service 1f','change on service 1g','change on service 1k','change on service 1l']
	
	return list[random.randrange(8)]