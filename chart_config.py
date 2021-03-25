from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import matplotlib.ticker as tk
import matplotlib.dates as mdates
import numpy as np

w = 8
h = 4.5
chart_path = "charts/"
default_font = "Oswald" #Change this if you don't like it or is not available in your system
legend_font = "Myriad Pro" #Change this to edit legends' font
background_plot = "silver" #Default background color for charts
background_figure = "white" #Default background color for figures
major_grid_color = "dimgrey" #Default colors for grids...
minor_grid_color = "dimgray"
alphaMGC = 0.7
alphamGC = 0.9
image_resolution = 120
language = 1 #0 = english, 1 = spanish
plot_scale = "linear"
legend_text_size = 8
start_date = "2021-01-01"

def save_plot(name, figure, code):
	plt.yscale(plot_scale)
	plt.tight_layout()
	plt.savefig(chart_path + code + "_" + str(language) + "_" + name + ".png", facecolor=figure.get_facecolor())
	print("-- The chart was saved!", end="\n")

def grid_and_ticks(yMax, ticksinterval):
	plt.grid(which='both', axis='both')
	plt.minorticks_on()
	plt.grid(True, "major", "y", ls="-", lw=0.8, c=major_grid_color, alpha=alphaMGC)
	plt.grid(True, "minor", "y", ls="--", lw=0.3, c=minor_grid_color, alpha=alphamGC)
	plt.grid(True, "major", "x", ls="-", lw=0.8, c=major_grid_color, alpha=alphaMGC)
	plt.grid(True, "minor", "x", ls="--", lw=0.3, c=minor_grid_color, alpha=alphamGC)
	plt.xticks(fontsize=6)
	plt.yticks(fontsize=6)
	plt.yticks(np.arange(0, yMax, ticksinterval))
	plt.gca().set_facecolor(background_plot)

def ticks_locator(weekInterval):
	plt.gca().xaxis.set_minor_locator(tk.AutoMinorLocator(7))
	plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(interval = weekInterval))
	plt.gca().xaxis.set_major_formatter(dateFormat)
	plt.gca().xaxis.set_minor_formatter(tk.NullFormatter())

def build_texts(title, x_axis, y_axis):
	plt.title(title, fontname=default_font)
	plt.xlabel(x_axis, fontname=legend_font)
	plt.ylabel(y_axis, fontname=legend_font)

def build_legend():
	plt.legend(loc=0, shadow = True, facecolor = background_figure,
			prop={'family' : legend_font, 'size' : legend_text_size})
