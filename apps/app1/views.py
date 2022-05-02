from flask import Blueprint,request, url_for, redirect,render_template, flash,json,current_app,jsonify,send_file


app1= Blueprint('app1',__name__,template_folder="/templates/app1")


@app1.route("/hello")
def hello():
    return "newapp1"
