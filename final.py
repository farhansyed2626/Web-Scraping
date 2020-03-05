from bs4 import BeautifulSoup
from flask import Flask, jsonify, request
import json
import requests

app = Flask(__name__)

@app.route('/',methods=['GET'])
def time():

	
	res = requests.get('https://time.com/')
	txt=res.text
	soup = BeautifulSoup(txt, 'html.parser')

	news_box = soup.find_all('div',{'class': 'headline heading-3 heading-content margin-8-bottom media-heading'})

	a=[]
	

	for i in range(3,9):
		print(news_box[i].text)
		a.append(news_box[i].text)

	di = {}
	for j in range(6):
		di['title' + str(j+1)] = str(a[j]).strip('\n').strip('\t').strip()

	json_string = json.dumps(a)

	return json_string


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=False)
