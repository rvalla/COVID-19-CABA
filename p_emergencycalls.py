import chart_config as cc
import pandas as pd
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import matplotlib.ticker as tk
import matplotlib.dates as mdates

#Importing data from llamados_107_covid.csv
calls_data = pd.read_csv("processed/emergencycalls.csv")
calls_data.set_index("FECHA", inplace=True)

def plot_total_calls():
	print("-- Plotting total calls...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = calls_ratios_texts("total_calls");
	calls_data["COVID_LLAMADOS"][cc.start_date:].plot(kind='line', label=chart_texts[3], linewidth=2.5)
	calls_data["CASOS_SOSPECHOSOS"][cc.start_date:].plot(kind='line', label=chart_texts[4], linewidth=2.5)
	calls_data["CASOS_DERIVADOS"][cc.start_date:].plot(kind='line', label=chart_texts[5], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	cc.grid_and_ticks(1, 3)
	cc.save_plot("totalcalls", f)

def plot_total_calls_avg():
	print("-- Plotting total calls...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = calls_ratios_texts("total_calls");
	calls_data["LLAMADOSAVG"][cc.start_date:].plot(kind='line', label=chart_texts[3], linewidth=2.5)
	calls_data["SOSPECHOSOSAVG"][cc.start_date:].plot(kind='line', label=chart_texts[4], linewidth=2.5)
	calls_data["DERIVADOSAVG"][cc.start_date:].plot(kind='line', label=chart_texts[5], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	cc.grid_and_ticks(1, 3)
	cc.save_plot("totalcallsavg", f)

def plot_calls_ratios():
	print("-- Plotting calls ratios...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = calls_ratios_texts("calls_ratios");
	calls_data["%SOSPECHOSOS"][cc.start_date:].plot(kind='line', label=chart_texts[3], linewidth=2.5)
	calls_data["%TRASLADADOS"][cc.start_date:].plot(kind='line', label=chart_texts[4], linewidth=2.5)
	calls_data["%DERIVADOS"][cc.start_date:].plot(kind='line', label=chart_texts[5], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	cc.grid_and_ticks(1, 3)
	cc.save_plot("callsratios", f)

def plot_calls_ratios_avg():
	print("-- Plotting calls ratios...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = calls_ratios_texts("calls_ratios");
	calls_data["%SOSPECHOSOSAVG"][cc.start_date:].plot(kind='line', label=chart_texts[3], linewidth=2.5)
	calls_data["%TRASLADADOSAVG"][cc.start_date:].plot(kind='line', label=chart_texts[4], linewidth=2.5)
	calls_data["%DERIVADOSAVG"][cc.start_date:].plot(kind='line', label=chart_texts[5], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	cc.grid_and_ticks(1, 3)
	cc.save_plot("callsratiosavg", f)

texts_dict_en = {"calls_ratios": ["COVID-19 CABA: Emergency calls ratios", "Time in days", "Call's result ratio",
								"Suspicious", "Moved", "Derived"],
				"total_calls": ["COVID-19 CABA: Emergency calls", "Time in days", "Number of calls",
								"Total", "Suspicious", "Derived"]}

texts_dict_es = {"calls_ratios": ["COVID-19 CABA: Proporciones de llamados", "Tiempo en días", "Proporción de resultados",
								"Sospechosos", "Trasladados", "Descartados"],
				"total_calls": ["COVID-19 CABA: Llamados 107", "Tiempo en días", "Número de llamados",
								"Total", "Sospechosos", "Derivados"]}

def calls_ratios_texts(type):
	texts = []
	if cc.language == 0:
		return texts_dict_en[type]
	elif cc.language == 1:
		return texts_dict_es[type]
