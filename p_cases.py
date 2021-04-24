import chart_config as cc
import pandas as pd
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

data_types = ["Confirmed", "Deaths", "Dropped"]
input_path = "processed/"
d_byage_avg = []
d_byage_cum = []
d_byzone_avg = []
d_byzone_cum = []
d_byage_avg.append(pd.read_csv(input_path + "cases_confirmed_byage_avg.csv"))
d_byage_avg.append(pd.read_csv(input_path + "cases_deaths_byage_avg.csv"))
d_byage_cum.append(pd.read_csv(input_path + "cases_confirmed_byage_cum.csv"))
d_byage_cum.append(pd.read_csv(input_path + "cases_deaths_byage_cum.csv"))
d_byzone_avg.append(pd.read_csv(input_path + "cases_confirmed_byzone_avg.csv"))
d_byzone_avg.append(pd.read_csv(input_path + "cases_deaths_byzone_avg.csv"))
d_byzone_cum.append(pd.read_csv(input_path + "cases_confirmed_byzone_cum.csv"))
d_byzone_cum.append(pd.read_csv(input_path + "cases_deaths_byzone_cum.csv"))
for i in range(2):
	d_byage_avg[i]["FECHA"] = pd.to_datetime(d_byage_avg[i]["FECHA"], format="%Y-%m-%d")
	d_byage_avg[i].set_index("FECHA", inplace=True)
	d_byage_cum[i]["FECHA"] = pd.to_datetime(d_byage_cum[i]["FECHA"], format="%Y-%m-%d")
	d_byage_cum[i].set_index("FECHA", inplace=True)
	d_byzone_avg[i]["FECHA"] = pd.to_datetime(d_byzone_avg[i]["FECHA"], format="%Y-%m-%d")
	d_byzone_avg[i].set_index("FECHA", inplace=True)
	d_byzone_cum[i]["FECHA"] = pd.to_datetime(d_byzone_cum[i]["FECHA"], format="%Y-%m-%d")
	d_byzone_cum[i].set_index("FECHA", inplace=True)

def plot_total_cases(y_minA, y_minB, ticks_interval_A, ticks_divisor_A, ticks_interval_B, ticks_divisor_B):
	print("-- Plotting total cases...", end="\n")
	f = figure(num=None, figsize=(cc.d_w, cc.d_h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	confirmed = plt.subplot2grid((2, 1), (0, 0))
	chart_texts = get_chart_texts("total_confirmed")
	confirmed = d_byage_cum[0]["TotalM"][cc.e_start_date:cc.end_date].plot(kind='line', label=chart_texts[3], color=cc.colors[0], linewidth=2.5)
	confirmed = d_byage_cum[0]["TotalF"][cc.e_start_date:cc.end_date].plot(kind='line', label=chart_texts[4], color=cc.colors[1], linewidth=2.5)
	confirmed = d_byage_cum[0]["Total"][cc.e_start_date:cc.end_date].plot(kind='line', label=chart_texts[5], color=cc.colors[2], linewidth=2.5)
	cc.build_axis_texts(confirmed, chart_texts[0], "", chart_texts[2])
	cc.build_legend()
	s = plt.ylim()
	xaxis = plt.xlim()
	cc.grid_and_ticks(y_minA, s[1], ticks_interval_A, ticks_divisor_A, 0)
	cc.ticks_locator(cc.e_week_interval)
	plt.gca().xaxis.set_ticklabels([])
	deaths = plt.subplot2grid((2, 1), (1, 0))
	chart_texts = get_chart_texts("total_death")
	deaths = d_byage_cum[1]["TotalM"][cc.e_start_date:cc.end_date].plot(kind='line', label=chart_texts[3], color=cc.colors[0], linewidth=2.5)
	deaths = d_byage_cum[1]["TotalF"][cc.e_start_date:cc.end_date].plot(kind='line', label=chart_texts[4], color=cc.colors[1], linewidth=2.5)
	deaths = d_byage_cum[1]["Total"][cc.e_start_date:cc.end_date].plot(kind='line', label=chart_texts[5], color=cc.colors[2], linewidth=2.5)
	cc.build_axis_texts(deaths, chart_texts[0], chart_texts[1], chart_texts[2])
	s = plt.ylim()
	plt.xlim(xaxis[0], xaxis[1])
	cc.grid_and_ticks(y_minB, s[1], ticks_interval_B, ticks_divisor_B, 1)
	cc.ticks_locator(cc.e_week_interval)
	cc.save_plot("totalcasesanddeaths_cum", f, "E")

def plot_total_avg(y_minA, y_minB, ticks_interval_A, ticks_divisor_A, ticks_interval_B, ticks_divisor_B):
	print("-- Plotting total cases...", end="\n")
	f = figure(num=None, figsize=(cc.d_w, cc.d_h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	confirmed = plt.subplot2grid((2, 1), (0, 0))
	chart_texts = get_chart_texts("total_confirmed")
	confirmed = d_byage_avg[0]["TotalM"][cc.e_start_date:cc.end_date].plot(kind='line', label=chart_texts[3], color=cc.colors[0], linewidth=2.5)
	confirmed = d_byage_avg[0]["TotalF"][cc.e_start_date:cc.end_date].plot(kind='line', label=chart_texts[4], color=cc.colors[1], linewidth=2.5)
	confirmed = d_byage_avg[0]["Total"][cc.e_start_date:cc.end_date].plot(kind='line', label=chart_texts[5], color=cc.colors[2], linewidth=2.5)
	cc.build_axis_texts(confirmed, chart_texts[0], "", chart_texts[2])
	cc.build_legend()
	s = plt.ylim()
	xaxis = plt.xlim()
	cc.grid_and_ticks(y_minA, s[1], ticks_interval_A, ticks_divisor_A, 0)
	cc.ticks_locator(cc.e_week_interval)
	plt.gca().xaxis.set_ticklabels([])
	deaths = plt.subplot2grid((2, 1), (1, 0))
	chart_texts = get_chart_texts("total_death")
	deaths = d_byage_avg[1]["TotalM"][cc.e_start_date:cc.end_date].plot(kind='line', label=chart_texts[3], color=cc.colors[0], linewidth=2.5)
	deaths = d_byage_avg[1]["TotalF"][cc.e_start_date:cc.end_date].plot(kind='line', label=chart_texts[4], color=cc.colors[1], linewidth=2.5)
	deaths = d_byage_avg[1]["Total"][cc.e_start_date:cc.end_date].plot(kind='line', label=chart_texts[5], color=cc.colors[2], linewidth=2.5)
	cc.build_axis_texts(deaths, chart_texts[0], chart_texts[1], chart_texts[2])
	s = plt.ylim()
	plt.xlim(xaxis[0], xaxis[1])
	cc.grid_and_ticks(y_minB, s[1], ticks_interval_B, ticks_divisor_B, 0)
	cc.ticks_locator(cc.e_week_interval)
	cc.save_plot("totalcasesanddeaths_avg", f, "E")

def plot_cases_by_age_avg(y_minA, y_minB, ticks_interval_A, ticks_divisor_A, ticks_interval_B, ticks_divisor_B):
	print("-- Plotting cases by age...", end="\n")
	f = figure(num=None, figsize=(cc.d_w, cc.d_h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	confirmed = plt.subplot2grid((2, 1), (0, 0))
	chart_texts = get_chart_texts("total_confirmed")
	for i in range(len(age_groups)):
		confirmed = d_byage_avg[0][age_groups[i]][cc.start_date:cc.end_date].plot(kind='line', label=age_groups[i], color=cc.colors[i], linewidth=2.5)
	cc.build_texts(chart_texts[0], "", chart_texts[2])
	cc.build_legend()
	s = plt.ylim()
	xaxis = plt.xlim()
	cc.grid_and_ticks(y_minA, s[1], ticks_interval_A, ticks_divisor_A, 0)
	cc.ticks_locator(cc.week_interval)
	plt.gca().xaxis.set_ticklabels([])
	deaths = plt.subplot2grid((2, 1), (1, 0))
	chart_texts = get_chart_texts("total_death")
	for i in range(len(age_groups)):
		deaths = d_byage_avg[1][age_groups[i]][cc.start_date:cc.end_date].plot(kind='line', label=age_groups[i], color=cc.colors[i], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	s = plt.ylim()
	plt.xlim(xaxis[0], xaxis[1])
	cc.grid_and_ticks(y_minB, s[1], ticks_interval_B, ticks_divisor_B, 0)
	cc.ticks_locator(cc.week_interval)
	cc.save_plot("totalcasesanddeathsbyage_avg", f, "E")

def plot_delay_evol(y_minA, y_minB, ticks_interval_A, ticks_divisor_A, ticks_interval_B, ticks_divisor_B):
	print("-- Plotting delays...", end="\n")
	f = figure(num=None, figsize=(cc.d_w, cc.d_h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	confirmed = plt.subplot2grid((2, 1), (0, 0))
	chart_texts = get_chart_texts("total_confirmed_delay")
	confirmed = d_byage_avg[0]["DelayAvg"][cc.start_date:cc.end_date].plot(kind='line', label=chart_texts[3], color=cc.colors[0], linewidth=2.5)
	cc.build_axis_texts(confirmed, chart_texts[0], "", chart_texts[2])
	s = plt.ylim()
	xaxis = plt.xlim()
	cc.grid_and_ticks(y_minA, s[1], ticks_interval_A, ticks_divisor_A, 0)
	cc.ticks_locator(cc.week_interval)
	plt.gca().xaxis.set_ticklabels([])
	deaths = plt.subplot2grid((2, 1), (1, 0))
	chart_texts = get_chart_texts("total_death_delay")
	deaths = d_byage_avg[1]["DelayAvg"][cc.start_date:cc.end_date].plot(kind='line', label=chart_texts[3], color=cc.colors[0], linewidth=2.5)
	cc.build_axis_texts(deaths, chart_texts[0], chart_texts[1], chart_texts[2])
	s = plt.ylim()
	plt.xlim(xaxis[0], xaxis[1])
	cc.grid_and_ticks(y_minB, s[1], ticks_interval_B, ticks_divisor_B, 0)
	cc.ticks_locator(cc.week_interval)
	cc.save_plot("confirmedanddeathsdelays_avg", f, "E")

texts_dict_en = {"total_confirmed": ["COVID-19 CABA: Confirmed cases", "Time in days", "Number of cases",
				"Male", "Female", "Total"],
				"total_confirmed_delay": ["COVID-19 CABA: Confirmed cases delay", "Time in days", "Days of delay",
								"Total"],
				"total_death_delay": ["COVID-19 CABA: Deaths delay since test", "Time in days", "Days of delay",
								"Total"],
				"total_death": ["COVID-19 CABA: Deaths", "Time in days", "Number of deaths",
				"Hombres", "Mujeres", "Total"]}

texts_dict_es = {"total_confirmed": ["COVID-19 CABA: Casos confirmados", "Tiempo en días", "Casos confirmados",
				"Hombres", "Mujeres", "Total"],
				"total_confirmed_delay": ["COVID-19 CABA: Demora de confirmación", "Tiempo en días", "Demora en días",
								"Total"],
				"total_death_delay": ["COVID-19 CABA: Días entre test y fallecimiento", "Tiempo en días", "Demora en días",
								"Total"],
				"total_death": ["COVID-19 CABA: Fallecimientos", "Tiempo en días", "Fallecimientos",
				"Hombres", "Mujeres", "Total"]}

age_groups = ["<=10", "11-20", "21-30","31-40","41-50","51-60","61-70","71-80","81-90",">=91"]

def get_chart_texts(type):
	texts = []
	if cc.language == 0:
		return texts_dict_en[type]
	elif cc.language == 1:
		return texts_dict_es[type]
