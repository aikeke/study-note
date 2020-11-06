# /usr/bin/env/python
# -*- coding:utf-8 -*-

from flask import Flask,request,Response
import json
app=Flask(__name__)
@app.route('/api',methods=['POST','GET'])

def api():
    if request.method=='POST':
        postdata={'date':request.form['tm'],'cpu':request.form['cpu'],'mem':request.form['mem'],'net':request.form['net']}
        f=open('/tmp/cpu_record.txt','a+')
        f.write(json.dumps(postdata))
        f.write('\r\n')
        f.close()
        return 'ok'
    else:
        f=open('/tmp/cpu_record.txt')
        data=f.read()
        f.close()
        return Response(data,mimetype='text/plain')

app.run(host='0.0.0.0',threaded=True,port=8888)
