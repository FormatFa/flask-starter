from flask import Blueprint,request, url_for, redirect,render_template, flash,json,current_app,jsonify,send_file


app1= Blueprint('app1',__name__,template_folder="template")

# redirect
@app1.route("/")
def index():
    return redirect('/index')

# 返回一个html template的
@app1.route('/index')
def html():
    return render_template('index.html')

# 返回一个json数据
@app1.route('/apitest')
def apitest():
    return jsonify({"name":"shaw"})