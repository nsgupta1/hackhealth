from flask import Flask, render_template
from bokeh.plotting import figure, output_file, save
import os

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
	from bokeh.io import output_file
	from bokeh.models import ColumnDataSource
	from bokeh.palettes import Spectral5
	from bokeh.plotting import figure
	from bokeh.sampledata.autompg import autompg as df
	from bokeh.transform import factor_cmap

	output_file("templates/lines.html")

	df.cyl = df.cyl.astype(str)
	group = df.groupby('cyl')

	source = ColumnDataSource(group)
	cyl_cmap = factor_cmap('cyl', palette=Spectral5, factors=sorted(df.cyl.unique()))

	p = figure(plot_height=350, x_range=group, title="MPG by # Cylinders", toolbar_location=None, tools="")
	p.vbar(x='cyl', top='mpg_mean', width=1, source=source, line_color=cyl_cmap, fill_color=cyl_cmap)

	p.y_range.start = 0
	p.xgrid.grid_line_color = None
	p.xaxis.axis_label = "some stuff"
	p.xaxis.major_label_orientation = 1.2
	p.outline_line_color = None

	save(p)
	return render_template("bokeh_line.html")


@app.route("/d3_sam")
def d3_sam():
	return render_template("d3_sam.html")


if __name__ == "__main__":
	app.debug = True
	app.run()
