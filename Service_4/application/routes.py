from application import app
import requests


@app.route('/randomword', methods=['GET'])
def sentence():
    beginning = requests.get('http://service_2:5001/randomphrase')
    ending = requests.get('http://service_3:5002/randomphrase')
    response = beginning.text + " " + ending.text
    return response