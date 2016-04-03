import os
from flask import Flask, jsonify, render_template
from infection import *
# from jinja2 import *

app = Flask(__name__)

@app.route("/")
def infection():
	return render_template('index.html')

@app.route("/total_infection/<graph>/<user>")
def total_infection(graph, user):
	L = total_infection_wrapper(graph, user)

	return jsonify(steps=L)

@app.route("/limited_infection/<graph>/<amount>")
def limited_infection(graph, amount):
	L = limited_infection_wrapper(graph, int(amount))

	return jsonify(steps=L)


@app.route("/graph/<name>")
def graph(name):
	G = read_graph_with_name(name)
	nodes, links = process_graph(G)
	return jsonify(nodes=nodes, links=links)


if __name__ == '__main__':
	# port = int(os.environ.get("PORT", 31322))
	# app.run(host='0.0.0.0', port=port)
	app.debug = True
	app.run()