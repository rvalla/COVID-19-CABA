import chart_config as cc
import pandas as pd
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

data_types = ["Confirmed", "Deaths", "Dropped"]
input_path = "processed/"
deathrate = pd.read_csv(input_path + "analysis_deathrate.csv")
estimation_avg = pd.read_csv(input_path + "analysis_estimation_avg.csv")
estimation_cum = pd.read_csv(input_path + "analysis_estimation_cum.csv")
c_age_ratios = pd.read_csv(input_path + "analysis_ratiosbyage_confirmed.csv")
d_age_ratios = pd.read_csv(input_path + "analysis_ratiosbyage_deaths.csv")
deathrate["FECHA"] = pd.to_datetime(deathrate["FECHA"], format="%Y-%m-%d")
deathrate.set_index("FECHA", inplace=True)
estimation_avg["FECHA"] = pd.to_datetime(estimation_avg["FECHA"], format="%Y-%m-%d")
estimation_avg.set_index("FECHA", inplace=True)
estimation_cum["FECHA"] = pd.to_datetime(estimation_cum["FECHA"], format="%Y-%m-%d")
estimation_cum.set_index("FECHA", inplace=True)
c_age_ratios["FECHA"] = pd.to_datetime(c_age_ratios["FECHA"], format="%Y-%m-%d")
c_age_ratios.set_index("FECHA", inplace=True)
d_age_ratios["FECHA"] = pd.to_datetime(d_age_ratios["FECHA"], format="%Y-%m-%d")
d_age_ratios.set_index("FECHA", inplace=True)

def plot_deathrate_by_sex_and_age(y_min_a, y_min_b, ticks_interval_A, ticks_interval_B):
	print("-- Plotting deathrate evolution...", end="\n")
	f = figure(num=None, figsize=(cc.d_w, cc.d_h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	totalrate = plt.subplot2grid((2, 1), (0, 0))
	chart_texts = get_chart_texts("deathratebysex")
	totalrate = deathrate["TotalM"][cc.e_start_date:cc.end_date].plot(kind='line', label=chart_texts[3], color=cc.colors[0], linewidth=2.5)
	totalrate = deathrate["TotalF"][cc.e_start_date:cc.end_date].plot(kind='line', label=chart_texts[4], color=cc.colors[1], linewidth=2.5)
	totalrate = deathrate["Total"][cc.e_start_date:cc.end_date].plot(kind='line', label=chart_texts[5], color=cc.colors[2], linewidth=2.5)
	cc.build_axis_texts(totalrate, chart_texts[0], "", chart_texts[2])
	cc.build_legend()
	xaxis = plt.xlim()
	s = plt.ylim()
	cc.grid_and_ticks(y_min_a, s[1] * 1.1, ticks_interval_A, 1, 2)
	cc.ticks_locator(cc.e_week_interval)
	plt.gca().xaxis.set_ticklabels([])
	byagerate = plt.subplot2grid((2, 1), (1, 0))
	chart_texts = get_chart_texts("deathratebyage")
	for a in range(len(age_groups)):
		byagerate = deathrate[age_groups[a]][cc.e_start_date:cc.end_date].plot(kind='line', label=age_groups[a], color=cc.a_colors[a], linewidth=2.5)
	cc.build_axis_texts(byagerate, chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	plt.xlim(xaxis[0], xaxis[1])
	s = plt.ylim()
	cc.grid_and_ticks(y_min_b, s[1] * 1.1, ticks_interval_B, 1, 2)
	cc.ticks_locator(cc.e_week_interval)
	cc.save_plot("deathratebysexage_evolution", f, "A")

def plot_deathrate_by_age(y_min, ticks_interval):
	print("-- Plotting deathrate evolution...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_chart_texts("deathratebyage")
	for a in range(len(age_groups)):
		byagerate = deathrate[age_groups[a]][cc.start_date:cc.end_date].plot(kind='line', label=age_groups[a], color=cc.a_colors[a], linewidth=2.5)
	cc.build_axis_texts(byagerate, chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	s = plt.ylim()
	cc.grid_and_ticks(y_min, s[1] * 1.1, ticks_interval, 1, 2)
	cc.ticks_locator(cc.week_interval)
	cc.save_plot("deathratebyage_evolution", f, "A")

def plot_estimation(y_min_a, y_min_b, ticks_interval_A, ticks_divisor_A, ticks_interval_B, ticks_divisor_B):
	print("-- Plotting deathrate evolution...", end="\n")
	f = figure(num=None, figsize=(cc.d_w, cc.d_h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	cumestimation = plt.subplot2grid((2, 1), (0, 0))
	chart_texts = get_chart_texts("estimationcum")
	cumestimation = estimation_cum["confirmed"][cc.e_start_date:cc.end_date].plot(kind='line', color=cc.colors[0], linewidth=2.5, alpha=0.5)
	cumestimation = estimation_cum["estimation"][cc.e_start_date:cc.end_date].plot(kind='line', color=cc.colors[0], linewidth=2.5)
	cc.build_axis_texts(cumestimation, chart_texts[0], "", chart_texts[2])
	xaxis = plt.xlim()
	s = plt.ylim()
	cc.grid_and_ticks(y_min_a, s[1] * 1.1, ticks_interval_A, ticks_divisor_A, 1)
	cc.ticks_locator(cc.e_week_interval)
	plt.gca().xaxis.set_ticklabels([])
	knownratio = plt.subplot2grid((2, 1), (1, 0))
	chart_texts = get_chart_texts("knownratio")
	knownratio = estimation_cum["knownratio"][cc.e_start_date:cc.end_date].plot(kind='line', color=cc.colors[0], linewidth=2.5)
	cc.build_axis_texts(knownratio, chart_texts[0], chart_texts[1], chart_texts[2])
	plt.xlim(xaxis[0], xaxis[1])
	s = plt.ylim()
	cc.grid_and_ticks(y_min_b, s[1] * 1.1, ticks_interval_B, ticks_divisor_B, 2)
	cc.ticks_locator(cc.e_week_interval)
	cc.save_plot("estimation_cum", f, "A")

def plot_estimation_avg(y_min_a, y_min_b, ticks_interval_A, ticks_divisor_A, ticks_interval_B, ticks_divisor_B):
	new_end_date = pd.to_datetime(cc.end_date, format="%Y-%m-%d") - pd.Timedelta(days=30)
	print("-- Plotting deathrate evolution...", end="\n")
	f = figure(num=None, figsize=(cc.d_w, cc.d_h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	estimationavg = plt.subplot2grid((2, 1), (0, 0))
	chart_texts = get_chart_texts("estimationavg")
	estimationavg = estimation_avg["confirmed"][cc.e_start_date:new_end_date].plot(kind='line', color=cc.colors[0], linewidth=2.5, alpha=0.5)
	estimationavg = estimation_avg["estimation"][cc.e_start_date:new_end_date].plot(kind='line', color=cc.colors[0], linewidth=2.5)
	cc.build_axis_texts(estimationavg, chart_texts[0], "", chart_texts[2])
	xaxis = plt.xlim()
	s = plt.ylim()
	cc.grid_and_ticks(y_min_a, s[1] * 1.1, ticks_interval_A, ticks_divisor_A, 0)
	cc.ticks_locator(cc.e_week_interval)
	plt.gca().xaxis.set_ticklabels([])
	knownratio = plt.subplot2grid((2, 1), (1, 0))
	chart_texts = get_chart_texts("knownratio")
	knownratio = estimation_avg["knownratio"][cc.e_start_date:new_end_date].plot(kind='line', color=cc.colors[0 ], linewidth=2.5)
	cc.build_axis_texts(knownratio, chart_texts[0], chart_texts[1], chart_texts[2])
	plt.xlim(xaxis[0], xaxis[1])
	s = plt.ylim()
	cc.grid_and_ticks(y_min_b, s[1] * 1.1, ticks_interval_B, ticks_divisor_B, 2)
	cc.ticks_locator(cc.e_week_interval)
	cc.save_plot("estimation_avg", f, "A")

def plot_age_ratios(y_min_a, y_min_b, y_max_a, y_max_b, ticks_interval_A, ticks_interval_B):
	print("-- Plotting age ratios...", end="\n")
	f = figure(num=None, figsize=(cc.d_w, cc.d_h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	confirmed = plt.subplot2grid((2, 1), (0, 0))
	chart_texts = get_chart_texts("c_ageratios")
	for i in range(len(age_groups)):
		confirmed = c_age_ratios[age_groups[i]][cc.start_date:cc.end_date].plot(kind='line', color=cc.a_colors[i], label=age_groups[i], linewidth=2.5)
	cc.build_axis_texts(confirmed, chart_texts[0], "", chart_texts[2])
	xaxis = plt.xlim()
	s = plt.ylim()
	cc.grid_and_ticks(y_min_a, y_max_a, ticks_interval_A, 1, 2)
	cc.ticks_locator(cc.week_interval)
	plt.gca().xaxis.set_ticklabels([])
	deaths = plt.subplot2grid((2, 1), (1, 0))
	chart_texts = get_chart_texts("d_ageratios")
	new_end_date = pd.to_datetime(cc.end_date, format="%Y-%m-%d") - pd.Timedelta(days=7)
	for i in range(len(age_groups)):
		confirmed = d_age_ratios[age_groups[i]][cc.start_date:new_end_date].plot(kind='line', color=cc.a_colors[i], label=age_groups[i], linewidth=2.5)
	cc.build_axis_texts(deaths, chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	plt.xlim(xaxis[0], xaxis[1])
	s = plt.ylim()
	cc.grid_and_ticks(y_min_b, y_max_b, ticks_interval_B, 1, 2)
	cc.ticks_locator(cc.week_interval)
	cc.save_plot("confirmedanddeaths_ageratios", f, "A")

def plot_sex_ratios(y_min_a, y_min_b, y_max_a, y_max_b, ticks_interval_A, ticks_interval_B):
	print("-- Plotting sex ratios...", end="\n")
	f = figure(num=None, figsize=(cc.d_w, cc.d_h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	confirmed = plt.subplot2grid((2, 1), (0, 0))
	chart_texts = get_chart_texts("c_sexratios")
	confirmed = c_age_ratios["TotalM"][cc.start_date:cc.end_date].plot(kind='line', color=cc.colors[0], label=chart_texts[3], linewidth=2.5)
	confirmed = c_age_ratios["TotalF"][cc.start_date:cc.end_date].plot(kind='line', color=cc.colors[1], label=chart_texts[4], linewidth=2.5)
	cc.build_axis_texts(confirmed, chart_texts[0], "", chart_texts[2])
	xaxis = plt.xlim()
	s = plt.ylim()
	cc.grid_and_ticks(y_min_a, y_max_a, ticks_interval_A, 1, 2)
	cc.ticks_locator(cc.week_interval)
	plt.gca().xaxis.set_ticklabels([])
	deaths = plt.subplot2grid((2, 1), (1, 0))
	new_end_date = pd.to_datetime(cc.end_date, format="%Y-%m-%d") - pd.Timedelta(days=7)
	chart_texts = get_chart_texts("d_sexratios")
	deaths = d_age_ratios["TotalM"][cc.start_date:new_end_date].plot(kind='line', color=cc.colors[0], label=chart_texts[3], linewidth=2.5)
	deaths = d_age_ratios["TotalF"][cc.start_date:new_end_date].plot(kind='line', color=cc.colors[1], label=chart_texts[4], linewidth=2.5)
	cc.build_axis_texts(deaths, chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	plt.xlim(xaxis[0], xaxis[1])
	s = plt.ylim()
	cc.grid_and_ticks(y_min_b, y_max_b, ticks_interval_B, 1, 2)
	cc.ticks_locator(cc.week_interval)
	cc.save_plot("confirmedanddeaths_sexratios", f, "A")


texts_dict_en = {"deathratebysex": ["COVID-19 CABA: Death rate evolution", "Time in days", "Death rate",
				"Male", "Female", "Total"],
				"deathratebyage": ["COVID-19 CABA: Death rate evolution", "Time in days", "Death rate",
				"Male", "Female", "Total"],
				"estimationcum": ["COVID-19 CABA: Real cases estimation (12d, 0.01IFR)", "Time in days", "Estimated cases"],
				"estimationavg": ["COVID-19 CABA: Real cases estimation (7 days) (12d, 0.01IFR)", "Time in days", "Estimated cases"],
				"knownratio": ["COVID-19 CABA: Estimated known ratio (14d, 0.005IFR)", "Time in days", "Known ratio"],
				"c_ageratios": ["COVID-19 CABA: Confirmed cases proportions by age", "Time in days", "% confirmed cases"],
				"d_ageratios": ["COVID-19 CABA: Deaths proportions by age", "Time in days", "% deaths"],
				"c_sexratios": ["COVID-19 CABA: Confirmed cases proportions by sex", "Time in days", "% confirmed cases",
				"Male", "Female"],
				"d_sexratios": ["COVID-19 CABA: Deaths proportions by sex", "Time in days", "% deaths",
				"Male", "Female"]}

texts_dict_es = {"deathratebysex": ["COVID-19 CABA: Tasa de letalidad", "Tiempo en días", "Tasa de letalidad",
				"Hombres", "Mujeres", "Total"],
				"deathratebyage": ["COVID-19 CABA: Tasa de letalidad", "Tiempo en días", "Tasa de letalidad",
				"Hombres", "Mujeres", "Total"],
				"estimationcum": ["COVID-19 CABA: Estimación de casos reales (12d, 0.01IFR)", "Tiempo en días", "Casos estimados"],
				"estimationavg": ["COVID-19 CABA: Estimación de casos reales (7 días) (12d, 0.01IFR)", "Tiempo en días", "Casos estimados"],
				"knownratio": ["COVID-19 CABA: Proporción estimada de casos conocidos", "Tiempo en días", "Proporción conocida"],
				"c_ageratios": ["COVID-19 CABA: Proporciones de casos por edad", "Tiempo en días", "% casos confirmados"],
				"d_ageratios": ["COVID-19 CABA: Proporciones de fallecidos por edad", "Tiempo en días", "% fallecidos"],
				"c_sexratios": ["COVID-19 CABA: Proporciones de casos por sexo", "Tiempo en días", "% casos confirmados",
				"Hombres", "Mujeres"],
				"d_sexratios": ["COVID-19 CABA: Proporciones de fallecidos por sexo", "Tiempo en días", "% Fallecidos",
				"Hombres", "Mujeres"]}

age_groups = ["<=10","11-20", "21-30","31-40","41-50","51-60","61-70","71-80","81-90",">=91"]

def get_chart_texts(type):
	texts = []
	if cc.language == 0:
		return texts_dict_en[type]
	elif cc.language == 1:
		return texts_dict_es[type]
