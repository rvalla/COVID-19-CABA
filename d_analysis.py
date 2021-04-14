import math
import time as tm
import util as ut
import pandas as pd

#Saving the moment in which this process start
start_time = tm.time()

#Output path:
output_path = "processed/"

#Some estimation variables
real_mortality = 0.005 #Real mortality to estimate infected count from deaths
death_offset = 14 #Number of days needed to reach a death since symptoms onset on average

data_types = ["Confirmed", "Deaths", "Dropped"]
input_path = "processed/"
d_byage_avg = []
d_byage_cum = []
d_byage_avg.append(pd.read_csv(input_path + "cases_confirmed_byage_avg.csv"))
d_byage_avg.append(pd.read_csv(input_path + "cases_deaths_byage_avg.csv"))
d_byage_cum.append(pd.read_csv(input_path + "cases_confirmed_byage_cum.csv"))
d_byage_cum.append(pd.read_csv(input_path + "cases_deaths_byage_cum.csv"))
for i in range(2):
	d_byage_avg[i].set_index("FECHA", inplace=True)
	d_byage_cum[i].set_index("FECHA", inplace=True)

columns = d_byage_cum[0].columns
rows = d_byage_cum[0].index

estimation_cum = pd.DataFrame(index=rows, columns=["confirmed", "deaths", "estimation", "knownratio"])
estimation_avg = pd.DataFrame(index=rows, columns=["confirmed", "deaths", "estimation", "knownratio"])
deathrate = pd.DataFrame(index = rows, columns=columns)
estimation_cum.index.name = "FECHA"
estimation_avg.index.name = "FECHA"
deathrate.index.name = "FECHA"

def build_death_rate(c_df, d_df, out_df):
	for c in columns:
		out_df[c] = d_df[c] / c_df[c]

def build_estimation(c_df, d_df, out_df):
	out_df["confirmed"] = c_df["Total"]
	out_df["deaths"] = d_df["Total"]
	for i in range(out_df.shape[0] - death_offset):
		e = out_df.loc[out_df.index[i + death_offset], "deaths"] / real_mortality
		out_df.loc[out_df.index[i], "estimation"] = e
	out_df["knownratio"] = out_df["confirmed"] / out_df["estimation"]

def run():
	print("-- Analysing cases data...", end="\n")
	build_death_rate(d_byage_cum[0], d_byage_cum[1], deathrate)
	build_estimation(d_byage_cum[0], d_byage_cum[1], estimation_cum)
	build_estimation(d_byage_avg[0], d_byage_avg[1], estimation_avg)
	save_processed_data()

def save_processed_data():
	print("-- Preparing csv files...", end="\r")
	name = "analysis_"
	deathrate.to_csv(output_path + name + "deathrate.csv")
	estimation_cum.to_csv(output_path + name + "estimation_cum.csv")
	estimation_avg.to_csv(output_path + name + "estimation_avg.csv")
	print("-- Processed csv files saved!                 ", end="\n")
	print("-- This took " + str(get_time(start_time, tm.time())))

#Calculating time needed to processed the data..
def get_time(start_time, end_time):
	time = end_time - start_time
	formated_time = format_time(time)
	return formated_time

def format_time(time):
	ms = ""
	minutes = time // 60
	seconds = time - minutes * 60
	seconds = round(seconds, 2)
	ms = "{:02d}".format(int(minutes))
	ms += ":"
	ms += "{:05.2f}".format(seconds)
	return ms
