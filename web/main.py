from flask import Flask, render_template, make_response, request, jsonify
from bokeh.plotting import figure, output_file, save
import os, sqlite3
from face_detection import recognize, upload
from monitor import build_response

app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route("/")
def main():
	return render_template("home.html", name="MicroSoft Band 2")


@app.route("/demoLine")
def bokeh_line():
	# prepare some data
	x = [1, 2, 3, 4, 5]
	y = [6, 7, 2, 4, 5]

	# output to static HTML file
	output_file("templates/lines.html")

	# create a new plot with a title and axis labels
	p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

	# add a line renderer with legend and line thickness
	p.line(x, y, legend="Temp.", line_width=2)

	save(p)
	return render_template("bokeh_line.html")


@app.route("/thing2")
def thing2():
	import datetime
	from io import BytesIO
	import random

	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.figure import Figure
	from matplotlib.dates import DateFormatter

	import matplotlib.pyplot as plt

	# create data
	names = 'groupA', 'groupB', 'groupC', 'groupD',
	size = [12, 11, 3, 30]

	# Create a circle for the center of the plot
	my_circle = plt.Circle((0, 0), 0.7, color='white')

	# Give color names
	plt.pie(size, labels=names, colors=['red', 'green', 'blue', 'skyblue'])
	p = plt.gcf()
	p.gca().add_artist(my_circle)
	plt.show()

	# Custom colors --> colors will cycle
	plt.pie(size, labels=names, colors=['red', 'green'])
	p = plt.gcf()
	p.gca().add_artist(my_circle)
	plt.show()

	from palettable.colorbrewer.qualitative import Pastel1_7
	plt.pie(size, labels=names, colors=Pastel1_7.hex_colors)
	p = plt.gcf()
	p.gca().add_artist(my_circle)
	plt.savefig()

	fig = Figure()
	ax = fig.add_subplot(111)
	x = []
	y = []
	now = datetime.datetime.now()
	delta = datetime.timedelta(days=1)
	for i in range(10):
		x.append(now)
		now += delta
		y.append(random.randint(0, 1000))
	ax.plot_date(x, y, '-')
	ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
	fig.autofmt_xdate()
	canvas = FigureCanvas(fig)
	png_output = BytesIO()
	canvas.print_png(png_output)
	response = make_response(png_output.getvalue())
	response.headers['Content-Type'] = 'image/png'

	return response


@app.route("/d3_sam")
def d3_sam():
	return render_template("d3_sam.html")

@app.route('/recognize', methods=['POST'])
def recon():
    image = request.form['image']
    url = upload(image)
    data = recognize(url)
    res = build_response(data)   
    return jsonify(res)
    


if __name__ == "__main__":
	app.debug = True
	app.run()
