# /usr/bin/python
import flask
from flask import Flask
app=Flask(__name__)
@app.route('/',methods=['GET'])
def home():
    data={'wife':'difa','wife2':'alice'}
    return data

if __name__=='__main__':
    app.run('192.168.21.23')
