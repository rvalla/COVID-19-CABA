from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import matplotlib.ticker as tk
import matplotlib.dates as mdates
import numpy as np

w = 8
h = 4.5
d_w = 8
d_h = 6.5
chart_path = "charts/"
default_font = "Oswald" #Change this if you don't like it or is not available in your system
legend_font = "Myriad Pro" #Change this to edit legends' font
background_plot = "silver" #Default background color for charts
background_figure = "white" #Default background color for figures
major_grid_color = "dimgrey" #Default colors for grids...
minor_grid_color = "dimgray"
colors = ["tab:red", "tab:blue", "tab:green", "limegreen", "orange", "indianred", "teal", "darkslategray", \
			"mediumseagreen", "orangered", "goldenrod", "dimgrey", "whitesmoke", "mediumpurple", "indigo"]
a_colors = ["forestgreen", "darkgreen", "lightseagreen", "teal", "tab:blue", "darkblue", "indigo", \
			"mediumpurple", "firebrick", "darkred"]
alphaMGC = 0.7
alphamGC = 0.9
image_resolution = 120
language = 1 #0 = english, 1 = spanish
legend_text_size = 8
plot_scale = "linear"
start_date = "2020-03-15"
end_date = "2022-01-05"
week_interval = 6
v_start_date = "2021-01-01"
v_week_interval = 3
e_start_date = "2020-03-15"
e_week_interval = 6

if language == 1:
	date_format = mdates.DateFormatter("%d/%m")
elif language == 0:
	date_format = mdates.DateFormatter("%B %d")

def save_plot(name, figure, code):
	if (plot_scale != "linear"):
		plt.yscale(plot_scale)
	plt.tight_layout(rect=[0, 0, 1, 1])
	plt.savefig(chart_path + code + "_" + str(language) + "_" + name + ".png", facecolor=figure.get_facecolor())
	plt.close(figure)
	print("-- The chart was saved!", end="\n")

def grid_and_ticks(y_min, y_max, ticks_interval, ticks_divisor, dp):
	plt.grid(which='both', axis='both')
	plt.minorticks_on()
	plt.grid(True, "major", "y", ls="-", lw=0.8, c=major_grid_color, alpha=alphaMGC)
	plt.grid(True, "minor", "y", ls="--", lw=0.3, c=minor_grid_color, alpha=alphamGC)
	plt.grid(True, "major", "x", ls="-", lw=0.8, c=major_grid_color, alpha=alphaMGC)
	plt.grid(True, "minor", "x", ls="--", lw=0.3, c=minor_grid_color, alpha=alphamGC)
	yticks, ylabels = get_ticks_labels(y_min, y_max + ticks_interval, ticks_interval, ticks_divisor, dp)
	plt.xticks(fontsize=6)
	plt.yticks(fontsize=6)
	plt.yticks(yticks, ylabels)
	plt.gca().set_facecolor(background_plot)

def x_grid_and_ticks():
	plt.grid(which='both', axis='x')
	plt.minorticks_on()
	plt.grid(True, "major", "x", ls="-", lw=0.8, c=major_grid_color, alpha=alphaMGC)
	plt.grid(True, "minor", "x", ls="--", lw=0.3, c=minor_grid_color, alpha=alphamGC)
	plt.xticks(fontsize=6)
	plt.yticks(fontsize=6)
	plt.gca().set_facecolor(background_plot)

def get_ticks_labels(y_min, y_max, interval, divisor, dp):
	values = []
	if y_min < 0 and y_max > 0:
		a = np.arange(0, y_max, interval)
		b = a[:0:-1] * (-1)
		values = np.concatenate((b, a),axis=0)
	else:
		values =  np.arange(y_min, y_max, interval)
	labels = (values / divisor).tolist()
	format = "{:." + str(dp) + "f}"
	for l in range(len(labels)):
		labels[l] = format.format(labels[l])
		labels[l] += get_ticks_divisor_label(divisor)
	return values, labels

def get_ticks_divisor_label(divisor):
	if divisor == 1000:
		return "K"
	elif divisor == 1000000:
		return "M"
	else:
		return ""

def ticks_locator(weekInterval):
	plt.gca().xaxis.set_minor_locator(tk.AutoMinorLocator(7))
	plt.gca().xaxis.set_major_formatter(date_format)
	plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(interval = weekInterval))

	plt.gca().xaxis.set_minor_formatter(tk.NullFormatter())

def get_simetrical_limits(y_min, y_max):
	if abs(y_min) > abs(y_max):
		round(y_min, 2)
		return y_min, -y_min
	else:
		round(y_max, 2)
		return -y_max, y_max

def build_texts(title, x_axis, y_axis):
	plt.title(title, fontname=default_font)
	plt.xlabel(x_axis, fontname=legend_font)
	plt.ylabel(y_axis, fontname=legend_font)

def build_axis_texts(axis, title, x_axis, y_axis):
	axis.set_title(title, fontname=default_font)
	axis.set_xlabel(x_axis, fontname=legend_font)
	axis.set_ylabel(y_axis, fontname=legend_font)

def build_legend():
	plt.legend(loc=2, shadow = True, facecolor = background_figure,
			prop={'family' : legend_font, 'size' : legend_text_size})

def build_legends(axis_a, axis_b):
	a, al = axis_a.get_legend_handles_labels()
	b, bl = axis_b.get_legend_handles_labels()
	axis_b.legend(a + b, al + bl, loc=2, shadow = True, facecolor = background_figure,
				prop={'family' : legend_font, 'size' : legend_text_size})
