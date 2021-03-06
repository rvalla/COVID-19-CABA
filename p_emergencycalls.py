import chart_config as cc
import pandas as pd
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

#Importing data from llamados_107_covid.csv
calls_data = pd.read_csv("processed/emergencycalls.csv")
calls_data["FECHA"] = pd.to_datetime(calls_data["FECHA"], format="%Y-%m-%d")
calls_data.set_index("FECHA", inplace=True)

def plot_total_calls():
	print("-- Plotting total calls...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_calls_ratios_texts("total_calls");
	total = calls_data["COVID_LLAMADOS"][cc.start_date:cc.end_date].plot(kind='line', label=chart_texts[3], color=cc.colors[0], linewidth=2.5)
	cc.x_grid_and_ticks()
	cc.ticks_locator(cc.week_interval)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	other = total.twinx()
	other = calls_data["CASOS_SOSPECHOSOS"][cc.start_date:cc.end_date].plot(kind='line', label=chart_texts[4], color=cc.colors[1], linewidth=2.5)
	other = calls_data["CASOS_DERIVADOS"][cc.start_date:cc.end_date].plot(kind='line', label=chart_texts[5], color=cc.colors[2], linewidth=2.5)
	cc.x_grid_and_ticks()
	cc.ticks_locator(cc.week_interval)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legends(total, other)
	cc.save_plot("totalcalls", f, "C")

def plot_total_calls_avg():
	print("-- Plotting total calls...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_calls_ratios_texts("total_calls");
	total = calls_data["LLAMADOSAVG"][cc.start_date:cc.end_date].plot(kind='line', label=chart_texts[3], color=cc.colors[0], linewidth=2.5)
	cc.x_grid_and_ticks()
	cc.ticks_locator(cc.week_interval)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	other = total.twinx()
	other = calls_data["SOSPECHOSOSAVG"][cc.start_date:cc.end_date].plot(kind='line', label=chart_texts[4], color=cc.colors[1], linewidth=2.5)
	other = calls_data["DERIVADOSAVG"][cc.start_date:cc.end_date].plot(kind='line', label=chart_texts[5], color=cc.colors[2], linewidth=2.5)
	cc.x_grid_and_ticks()
	cc.ticks_locator(cc.week_interval)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legends(total, other)
	cc.save_plot("totalcallsavg", f, "C")

def plot_calls_ratios(y_min, ticks_interval, ticks_divisor):
	print("-- Plotting calls ratios...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_calls_ratios_texts("calls_ratios");
	calls_data["%SOSPECHOSOS"][cc.start_date:cc.end_date].plot(kind='line', label=chart_texts[3], color=cc.colors[0], linewidth=2.5)
	calls_data["%TRASLADADOS"][cc.start_date:cc.end_date].plot(kind='line', label=chart_texts[4], color=cc.colors[1], linewidth=2.5)
	calls_data["%DERIVADOS"][cc.start_date:cc.end_date].plot(kind='line', label=chart_texts[5], color=cc.colors[2], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	s = plt.ylim()
	cc.grid_and_ticks(y_min, s[1], ticks_interval, ticks_divisor, 2)
	cc.ticks_locator(cc.week_interval)
	cc.save_plot("callsratios", f, "C")

def plot_calls_ratios_avg(y_min, ticks_interval, ticks_divisor):
	print("-- Plotting calls ratios...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_calls_ratios_texts("calls_ratios");
	calls_data["%SOSPECHOSOSAVG"][cc.start_date:cc.end_date].plot(kind='line', label=chart_texts[3], color=cc.colors[0], linewidth=2.5)
	calls_data["%TRASLADADOSAVG"][cc.start_date:cc.end_date].plot(kind='line', label=chart_texts[4], color=cc.colors[1], linewidth=2.5)
	calls_data["%DERIVADOSAVG"][cc.start_date:cc.end_date].plot(kind='line', label=chart_texts[5], color=cc.colors[2], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	s = plt.ylim()
	cc.grid_and_ticks(y_min, s[1], ticks_interval, ticks_divisor, 2)
	cc.ticks_locator(cc.week_interval)
	cc.save_plot("callsratiosavg", f, "C")

texts_dict_en = {"calls_ratios": ["COVID-19 CABA: Emergency calls ratios", "Time in days", "Call's result ratio",
								"Suspicious", "Moved", "Derived"],
				"total_calls": ["COVID-19 CABA: Emergency calls", "Time in days", "Number of calls",
								"Total", "Suspicious", "Derived"]}

texts_dict_es = {"calls_ratios": ["COVID-19 CABA: Proporciones de llamados", "Tiempo en d??as", "Proporci??n de resultados",
								"Sospechosos", "Trasladados", "Descartados"],
				"total_calls": ["COVID-19 CABA: Llamados 107", "Tiempo en d??as", "N??mero de llamados",
								"Total", "Sospechosos", "Derivados"]}

def get_calls_ratios_texts(type):
	texts = []
	if cc.language == 0:
		return texts_dict_en[type]
	elif cc.language == 1:
		return texts_dict_es[type]
