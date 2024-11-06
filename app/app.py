from flask import Flask, render_template, abort, redirect, request
import os
import redis
prog = Flask(__name__)	


@prog.route('/',methods=["GET","POST"])
def inicio():
    noredis=False
    try:
        r = redis.Redis(host="localhost", port=6379, db=0)
        l=r.lrange("lista",0,-1)
        lista=[x.decode('utf-8') for x in l]
    except:
        noredis=True
        lista=[]
    
    return render_template("inicio.html",noredis=noredis,lista=lista)

@prog.route('/add',methods=["GET","POST"])
def add():
    try:
        r = redis.Redis(host="localhost", port=6379, db=0)
        if request.form.get("info")!="":
            l=r.lpush("lista",request.form.get("info"))
    except:
        abort(404)
    return redirect("/")
if __name__ == '__main__':
    prog.run('0.0.0.0',5000,debug=True)
