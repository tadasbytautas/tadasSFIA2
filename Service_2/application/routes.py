from application import app
import random


@app.route('/randomphrase', methods=['GET'])
def beginning():

	list = ['Brainsucker','Lionel','Grabber','Riley','Crawler','Matterslurper','Abomination','Lurker','Adolf']
	
	return list[random.randrange(8)]