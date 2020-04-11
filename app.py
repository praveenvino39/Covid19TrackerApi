from flask import Flask,request, jsonify
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route('/')
def index():
    html = requests.get('https://www.mohfw.gov.in/')
    if html.status_code == 200:
        content = {
        'status_code':200,
        'active':None,
        'cured':None,
        'death':None,
        'migrated': None,
        'update-on':None
        }
        print("page downloaded successfully")
        soup = BeautifulSoup(html.content, 'html.parser')
        content['active'] = int(soup.select('.bg-blue > strong:nth-child(2)')[0].text)
        content['cured'] = int(soup.select('.bg-green > strong:nth-child(2)')[0].text)
        content['death'] = int(soup.select('.bg-red > strong:nth-child(2)')[0].text)
        content['migrated'] = int(soup.select('.bg-orange > strong:nth-child(2)')[0].text)
        content['update-on'] = soup.select('.status-update > h2:nth-child(1) > span:nth-child(1)')[0].text
    else:
        content = {'status_code':404}
    return jsonify(content)

if __name__ == '__main__':
    app.run(debug=True)
