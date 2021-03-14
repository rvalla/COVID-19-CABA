import chart_config as cc
import pandas as pd
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import matplotlib.ticker as tk
import matplotlib.dates as mdates

#Importing data from llamados_107_covid.csv
calls_data = pd.read_csv("processed/emergencycalls.csv")
calls_data.set_index("FECHA", inplace=True)

def calls_ratios_texts():
	texts = []
	if cc.language == 0:
		texts.append("COVID-19 CABA: Emergency calls ratios")
		texts.append("Time in days")
		texts.append("Call's result ratio")
		texts.append("Suspicious")
		texts.append("Moved")
		texts.append("Derived")
	elif cc.language == 1:
		texts.append("COVID-19 CABA: Proporciones de llamados")
		texts.append("Tiempo en días")
		texts.append("Proporción de resultados")
		texts.append("Sospechosos")
		texts.append("Trasladados")
		texts.append("Descartados")
	return texts

def plot_calls_ratios():
	print("-- Plotting calls ratios...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = calls_ratios_texts();
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
	chart_texts = calls_ratios_texts();
	calls_data["%SOSPECHOSOSAVG"][cc.start_date:].plot(kind='line', label=chart_texts[3], linewidth=2.5)
	calls_data["%TRASLADADOSAVG"][cc.start_date:].plot(kind='line', label=chart_texts[4], linewidth=2.5)
	calls_data["%DERIVADOSAVG"][cc.start_date:].plot(kind='line', label=chart_texts[5], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	cc.grid_and_ticks(1, 3)
	cc.save_plot("callsratiosavg", f)
