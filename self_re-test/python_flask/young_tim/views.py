from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html", name="Tim", age=22)
    #return "Home page"

# #for the route parameters
# @views.route("/profile/<username>")
# def profile(username):
#     return render_template("index.html", name=username)

# #for query parameters 
# @views.route("/profile/")
# def profile():
#     args = request.args
#     name = args.get('name')
#     return render_template("index.html", name=name)

#for returning json
@views.route('/json')
def get_json():
    return jsonify({'name' : 'tim', 'coolness' : 10})

#for getting json from a route
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.get_json"))

@views.route("/next")
def next(): 
    return render_template("next.html")