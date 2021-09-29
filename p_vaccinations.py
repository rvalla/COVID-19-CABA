import chart_config as cc
import pandas as pd
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

cum_age_sex = pd.read_csv("processed/vaccinationbyageandsex_cum.csv")
cum_age_sex["FECHA"] = pd.to_datetime(cum_age_sex["FECHA"], format="%Y-%m-%d")
cum_age_sex.set_index("FECHA", inplace=True)
cum_age_dose = pd.read_csv("processed/vaccinationbyageanddose_cum.csv")
cum_age_dose["FECHA"] = pd.to_datetime(cum_age_dose["FECHA"], format="%Y-%m-%d")
cum_age_dose.set_index("FECHA", inplace=True)
age_dose = pd.read_csv("processed/vaccinationbyageanddose.csv")
age_dose["FECHA"] = pd.to_datetime(age_dose["FECHA"], format="%Y-%m-%d")
age_dose.set_index("FECHA", inplace=True)
age_dose_avg = pd.read_csv("processed/vaccinationbyageanddoseavg.csv")
age_dose_avg["FECHA"] = pd.to_datetime(age_dose_avg["FECHA"], format="%Y-%m-%d")
age_dose_avg.set_index("FECHA", inplace=True)
vac_dose_avg = pd.read_csv("processed/vaccinationbyvaccineavg.csv")
vac_dose_avg["FECHA"] = pd.to_datetime(vac_dose_avg["FECHA"], format="%Y-%m-%d")
vac_dose_avg.set_index("FECHA", inplace=True)
reached_s = pd.read_csv("processed/vaccinationbyageandsex_reached.csv")
reached_s["FECHA"] = pd.to_datetime(reached_s["FECHA"], format="%Y-%m-%d")
reached_s.set_index("FECHA", inplace=True)
reached_d = pd.read_csv("processed/vaccinationbyageanddose_reached.csv")
reached_d["FECHA"] = pd.to_datetime(reached_d["FECHA"], format="%Y-%m-%d")
reached_d.set_index("FECHA", inplace=True)

def plot_total_vac_by_sex(y_min, ticks_interval, ticks_divisor):
	print("-- Plotting total vaccinations by sex...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_chart_texts("total_by_sex")
	plot = plt.subplot2grid((1, 1), (0, 0))
	plot = cum_age_sex["TotalM"][cc.v_start_date:cc.end_date].plot(kind='line', label=chart_texts[3], color=cc.colors[0], linewidth=2.5)
	plot = cum_age_sex["TotalF"][cc.v_start_date:cc.end_date].plot(kind='line', label=chart_texts[4], color=cc.colors[1], linewidth=2.5)
	plot = cum_age_sex["Total"][cc.v_start_date:cc.end_date].plot(kind='line', label=chart_texts[5], color=cc.colors[2], linewidth=2.5)
	cc.build_axis_texts(plot, chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	s = plt.ylim()
	cc.grid_and_ticks(y_min, s[1], ticks_interval, ticks_divisor, 0)
	cc.ticks_locator(cc.v_week_interval)
	plt.tight_layout()
	cc.save_plot("totalvaccinationsbysex", f, "V")

def plot_total_vac_by_dose(y_min, ticks_interval, ticks_divisor):
	print("-- Plotting total vaccinations by dose...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_chart_texts("total_by_dose")
	cum_age_dose["TotalA"][cc.v_start_date:cc.end_date].plot(kind='line', label=chart_texts[3], color=cc.colors[0], linewidth=2.5)
	cum_age_dose["TotalB"][cc.v_start_date:cc.end_date].plot(kind='line', label=chart_texts[4], color=cc.colors[1], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	s = plt.ylim()
	cc.grid_and_ticks(y_min, s[1], ticks_interval, ticks_divisor, 0)
	cc.ticks_locator(cc.v_week_interval)
	cc.save_plot("totalvaccinationsbydose", f, "V")

def plot_doses_by_age(y_min, ticks_interval, ticks_divisor):
	print("-- Plotting total vaccinations by age...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_chart_texts("by_age")
	for i in range(len(age_groups)):
		age_dose[age_groups[i]][cc.v_start_date:cc.end_date].plot(kind='line', label=age_groups[i], color=cc.colors[i], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	s = plt.ylim()
	cc.grid_and_ticks(y_min, s[1], ticks_interval, ticks_divisor, 0)
	cc.ticks_locator(cc.v_week_interval)
	cc.save_plot("vaccinationsbyage", f, "V")

def plot_doses_by_age_avg(y_min, ticks_interval, ticks_divisor):
	print("-- Plotting total vaccinations by age...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_chart_texts("by_age_avg")
	for i in range(len(age_groups)):
		age_dose_avg[age_groups[i]][cc.v_start_date:cc.end_date].plot(kind='line', label=age_groups[i], color=cc.colors[i], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	s = plt.ylim()
	cc.grid_and_ticks(y_min, s[1], ticks_interval, ticks_divisor, 0)
	cc.ticks_locator(cc.v_week_interval)
	cc.save_plot("vaccinationsbyageavg", f, "V")

def plot_doses_by_vac_avg(y_min, ticks_interval, ticks_divisor):
	print("-- Plotting total vaccinations by vaccine...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_chart_texts("by_vac_avg")
	for i in range(len(vaccines)):
		vac_dose_avg[vaccines[i]][cc.v_start_date:cc.end_date].plot(kind='line', label=vaccines[i], color=cc.colors[i], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	s = plt.ylim()
	cc.grid_and_ticks(y_min, s[1], ticks_interval, ticks_divisor, 0)
	cc.ticks_locator(cc.v_week_interval)
	cc.save_plot("vaccinationsbyvac", f, "V")

def plot_reached_population_by_age(y_min, ticks_interval, ticks_divisor):
	print("-- Plotting reached population by age...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_chart_texts("reached_age")
	for i in range(len(reached_age_g)):
		reached_d[reached_age_g[i]][cc.v_start_date:cc.end_date].plot(kind='line', label=reached_age_g[i], color=cc.colors[i], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	s = plt.ylim()
	cc.grid_and_ticks(y_min, s[1], ticks_interval, ticks_divisor, 2)
	cc.ticks_locator(cc.v_week_interval)
	cc.save_plot("reachedbyage", f, "V")

def plot_reached_population_by_sex(ticks_interval, ticks_divisor):
	print("-- Plotting reached population by age...", end="\n")
	f = figure(num=None, figsize=(cc.w, cc.h), dpi=cc.image_resolution, facecolor=cc.background_figure, edgecolor='k')
	chart_texts = get_chart_texts("reached_sex")
	for i in range(len(reached_age_g)):
		data = reached_s[reached_age_g[i] + "F"][cc.v_start_date:cc.end_date] - reached_s[reached_age_g[i] + "M"][cc.v_start_date:cc.end_date]
		data[cc.v_start_date:cc.end_date].plot(kind='line', label=reached_age_g[i], color=cc.colors[i], linewidth=2.5)
	cc.build_texts(chart_texts[0], chart_texts[1], chart_texts[2])
	cc.build_legend()
	s = plt.ylim()
	min, max = cc.get_simetrical_limits(s[0] * 1.1, s[1])
	cc.grid_and_ticks(min, max, ticks_interval, ticks_divisor, 2)
	cc.ticks_locator(cc.v_week_interval)
	cc.save_plot("reachedbysex", f, "V")

texts_dict_en = {"total_by_sex": ["COVID-19 CABA: Vaccination champaign by sex", "Time in days", "Number of doses",
								"Male", "Female", "Total"],
				"total_by_dose": ["COVID-19 CABA: Vaccination champaign by dose", "Time in days", "Number of doses",
												"Firts dose", "Second dose"],
				"by_age": ["COVID-19 CABA: Vaccination champaign by age", "Time in days", "Number of doses"],
				"by_age_avg": ["COVID-19 CABA: Vaccination champaign by age (7 days)", "Time in days", "Number of doses"],
				"reached_age": ["COVID-19 CABA: Reached population by age", "Time in days", "Populations %"],
				"reached_sex": ["COVID-19 CABA: Reached population by sex (difference)", "Time in days", "Populations % (difference - F > M)"],
				"by_vac_avg": ["COVID-19 CABA: Vaccination champaign by age (7 days)", "Time in days", "Number of doses"]}

texts_dict_es = {"total_by_sex": ["COVID-19 CABA: Vacunación según género", "Tiempo en días", "Dosis administradas",
								"Masculinos", "Femeninos", "Total"],
				"total_by_dose": ["COVID-19 CABA: Vacunación según número de dosis", "Tiempo en días", "Dosis administradas",
								"Primera dosis", "Segunda dosis"],
				"by_age": ["COVID-19 CABA: Vacunación según edad", "Tiempo en días", "Dosis administradas"],
				"by_age_avg": ["COVID-19 CABA: Vacunación según edad (7 días)", "Tiempo en días", "Dosis administradas"],
				"reached_age": ["COVID-19 CABA: Población alcanzada por edad", "Tiempo en días", "% población alcanzada"],
				"reached_sex": ["COVID-19 CABA: Población alcanzada por sexo (diferencia)", "Tiempo en días", "% población alcanzada (diferencia - F > M)"],
				"by_vac_avg": ["COVID-19 CABA: Vacunación según vacuna (7 días)", "Tiempo en días", "Dosis administradas"]}

age_groups = ["<=30","31-40","41-50","51-60","61-70","71-80","81-90",">=91"]
reached_age_g = ["<=30","31-40","41-50","51-60","61-70","71-80",">=81"]
vaccines = ["Sputnik", "Sinopharm", "AstraZeneca", "Moderna", "Cansino", "Pfizer"]

def get_chart_texts(type):
	texts = []
	if cc.language == 0:
		return texts_dict_en[type]
	elif cc.language == 1:
		return texts_dict_es[type]
