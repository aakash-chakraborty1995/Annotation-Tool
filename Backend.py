import flask
from flask import Flask, request, render_template,send_from_directory
import json
import json2xml
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
app = flask.Flask(__name__ , static_url_path='')

data = readfromstring('{"login":"mojombo","id":1,"avatar_url":"https://avatars0.githubusercontent.com/u/1?v=4"}')

@app.route('/index')
def root():
    return render_template('marker2.html')

@app.route('/Gain0032.jpg')
def root1():
    return send_from_directory('','Gain0032.jpg')

@app.route('/application/json',methods=["POST"])
def output_json():
    data=flask.request.json
    return(json2xml.Json2xml(data).to_xml())

if __name__ == '__main__':
	app.run()
