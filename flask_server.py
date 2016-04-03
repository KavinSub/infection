from flask import Flask, jsonify
from infection import *

app = Flask(__name__)

@app.route("/")
def hello():

	return "Hello world!"

@app.route("/total_infection/<graph>/<user>")
def total_infection(graph, user):
	L = total_infection_wrapper(graph, user)

	return jsonify(steps=L)

@app.route("/limited_infection/<graph>/<amount>")
def limited_infection(graph, amount):
	L = limited_infection_wrapper(graph, int(amount))

	return jsonify(steps=L)

if __name__ == '__main__':
	app.debug = True
	app.run()