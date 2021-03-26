import chart_config as cc
import pandas as pd
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import matplotlib.ticker as tk
import matplotlib.dates as mdates

def plot_total_vac_by_sex():
	cum_age_sex = pd.read_csv("processed/cum_vaccinationbyageandsex.csv")
	cum_age_sex.set_index("FECHA", inplace=True)
	print("-- Plotting total vaccinations by sex...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_chart_texts("total_by_sex")
	cum_age_sex["TotalM"][cc.start_date:].plot(kind='line', label=chart_texts[3], linewidth=2.5)
	cum_age_sex["TotalF"][cc.start_date:].plot(kind='line', label=chart_texts[4], linewidth=2.5)
	cum_age_sex["Total"][cc.start_date:].plot(kind='line', label=chart_texts[5], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	cc.grid_and_ticks(1, 3)
	cc.save_plot("totalvaccinationsbysex", f, "V")

def plot_total_vac_by_dose():
	cum_age_dose = pd.read_csv("processed/cum_vaccinationbyageanddose.csv")
	cum_age_dose.set_index("FECHA", inplace=True)
	print("-- Plotting total vaccinations by dose...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_chart_texts("total_by_dose")
	cum_age_dose["TotalA"][cc.start_date:].plot(kind='line', label=chart_texts[3], linewidth=2.5)
	cum_age_dose["TotalB"][cc.start_date:].plot(kind='line', label=chart_texts[4], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	cc.grid_and_ticks(1, 3)
	cc.save_plot("totalvaccinationsbydose", f, "V")

def plot_doses_by_age():
	age_dose = pd.read_csv("processed/vaccinationbyageanddose.csv")
	age_dose.set_index("FECHA", inplace=True)
	print("-- Plotting total vaccinations by age...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_chart_texts("by_age")
	for i in range(len(age_groups)):
		age_dose[age_groups[i]][cc.start_date:].plot(kind='line', label=age_groups[i], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	cc.grid_and_ticks(1, 3)
	cc.save_plot("vaccinationsbyage", f, "V")

def plot_doses_by_age_avg():
	age_dose_avg = pd.read_csv("processed/vaccinationbyageanddoseavg.csv")
	age_dose_avg.set_index("FECHA", inplace=True)
	print("-- Plotting total vaccinations by age...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_chart_texts("by_age_avg")
	for i in range(len(age_groups)):
		age_dose_avg[age_groups[i]][cc.start_date:].plot(kind='line', label=age_groups[i], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	cc.grid_and_ticks(1, 3)
	cc.save_plot("vaccinationsbyageavg", f, "V")

def plot_doses_by_vac_avg():
	vac_dose_avg = pd.read_csv("processed/vaccinationbyvaccineavg.csv")
	vac_dose_avg.set_index("FECHA", inplace=True)
	print("-- Plotting total vaccinations by vaccine...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_chart_texts("by_vac_avg")
	for i in range(len(vaccines)):
		vac_dose_avg[vaccines[i]][cc.start_date:].plot(kind='line', label=vaccines[i], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	cc.grid_and_ticks(1, 3)
	cc.save_plot("vaccinationsbyvac", f, "V")

texts_dict_en = {"total_by_sex": ["COVID-19 CABA: Vaccination champaign by sex", "Time in days", "Number of doses",
								"Male", "Female", "Total"],
				"total_by_dose": ["COVID-19 CABA: Vaccination champaign by dose", "Time in days", "Number of doses",
												"Firts dose", "Second dose"],
				"by_age": ["COVID-19 CABA: Vaccination champaign by age", "Time in days", "Number of doses"],
				"by_age_avg": ["COVID-19 CABA: Vaccination champaign by age (7 days)", "Time in days", "Number of doses"],
				"by_vac_avg": ["COVID-19 CABA: Vaccination champaign by age (7 days)", "Time in days", "Number of doses"]}

texts_dict_es = {"total_by_sex": ["COVID-19 CABA: Vacunación según género", "Tiempo en días", "Dosis administradas",
								"Masculinos", "Femeninos", "Total"],
				"total_by_dose": ["COVID-19 CABA: Vacunación según número de dosis", "Tiempo en días", "Dosis administradas",
								"Primera dosis", "Segunda dosis"],
				"by_age": ["COVID-19 CABA: Vacunación según edad", "Tiempo en días", "Dosis administradas"],
				"by_age_avg": ["COVID-19 CABA: Vacunación según edad (7 días)", "Tiempo en días", "Dosis administradas"],
				"by_vac_avg": ["COVID-19 CABA: Vacunación según vacuna (7 días)", "Tiempo en días", "Dosis administradas"]}

age_groups = ["<=30","31-40","41-50","51-60","61-70","71-80","81-90",">=91"]
vaccines = ["Sputnik", "Covishield", "Sinopharm"]

def get_chart_texts(type):
	texts = []
	if cc.language == 0:
		return texts_dict_en[type]
	elif cc.language == 1:
		return texts_dict_es[type]
