import chart_config as cc
import pandas as pd
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import matplotlib.ticker as tk
import matplotlib.dates as mdates

#Importing data from processed csv files
cum_age_sex = pd.read_csv("processed/cum_vaccinationbyageandsex.csv")
age_sex = pd.read_csv("processed/vaccinationbyageandsex.csv")
cum_age_dose = pd.read_csv("processed/cum_vaccinationbyageanddose.csv")
age_dose = pd.read_csv("processed/vaccinationbyageanddose.csv")

cum_age_sex.set_index("FECHA", inplace=True)
age_sex.set_index("FECHA", inplace=True)
cum_age_dose.set_index("FECHA", inplace=True)
age_dose.set_index("FECHA", inplace=True)

def plot_total_vac_by_sex():
	print("-- Plotting total vaccinations by sex...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_chart_texts("total_by_sex");
	cum_age_sex["TotalM"][cc.start_date:].plot(kind='line', label=chart_texts[3], linewidth=2.5)
	cum_age_sex["TotalF"][cc.start_date:].plot(kind='line', label=chart_texts[4], linewidth=2.5)
	cum_age_sex["Total"][cc.start_date:].plot(kind='line', label=chart_texts[5], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	cc.grid_and_ticks(1, 3)
	cc.save_plot("totalvaccinationsbysex", f, "V")

texts_dict_en = {"total_by_sex": ["COVID-19 CABA: Vaccination champaign by sex", "Time in days", "Number of doses",
								"Male", "Female", "Total"]}

texts_dict_es = {"total_by_sex": ["COVID-19 CABA: Vacunación según género", "Tiempo en días", "Dosis administradas",
								"Masculinos", "Femeninos", "Total"]}

def get_chart_texts(type):
	texts = []
	if cc.language == 0:
		return texts_dict_en[type]
	elif cc.language == 1:
		return texts_dict_es[type]
