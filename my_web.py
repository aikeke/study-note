# -*- coding: utf-8 -*-
from flask import Flask,request
app=Flask(__name__)

@app.route('/api',methods=['POST','GET'])
def api():
    if request.method=='POST':
        print(request.form['mem'])
        print(request.form['wife'])
        print(type(request.form['wife']))
        #print(request.POST)
        return 'POST 哈哈'
    else:
        return "GET"

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=False)

