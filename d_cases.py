import math
import time as tm
import util as ut
import pandas as pd

#Saving the moment in which this process start
start_time = tm.time()

#Importing demographics data...
#demographics = pd.read_csv("demographics_c.csv")

filename = "casos_covid19.csv"
data_type = ["confirmed", "deaths", "dropped"]
data_zone = []
data_age = []
age_errors = 0
zone_errors = 0

#Setting time period
start_date = "2020-03-15"
end_date = "2021-04-06"
period = pd.date_range(start_date, end_date)
csv_lines = 2027340
lines_step = 5000
age_cuts = [31,41,51,61,71,81,91,1000]
age_keys = ["<=30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90", ">=91"]
csv_columns = ["numero_de_caso","fecha_apertura_snvs","fecha_toma_muestra","fecha_clasificacion","provincia","barrio",
				"comuna","genero","edad","clasificacion","fecha_fallecimiento","fallecido","fecha_alta","tipo_contagio"]
zone_c_s = ["1M","1F","1","2M","2F","2","3M","3F","3","4M","4F","4","5M","5F","5","6M","6F","6","7M","7F","7",
			"8M","8F","8","9M","9F","9","10M","10F","10","11M","11F","11","12M","12F","12","13M","13F","13",
			"14M","14F","14","15M","15F","15","TotalM","TotalF","Total"]
age_c_s = ["<=30M","<=30F","<=30","31-40M","31-40F","31-40","41-50M","41-50F","41-50","51-60M","51-60F","51-60",
		"61-70M","61-70F","61-70","71-80M","71-80F","71-80","81-90M","81-90F","81-90",">=91M",">=91F",">=91",
		"TotalM","TotalF","Total", "DelayCount", "CumDelay", "DelayAvg"]
for d in range(len(data_type)):
	data_zone.append(pd.DataFrame(0, index=period, columns=zone_c_s))
	data_age.append(pd.DataFrame(0, index=period, columns=age_c_s))
	data_zone[d].index.name = "FECHA"
	data_age[d].index.name = "FECHA"

#Functions to process the dataset...
def add_confirmed_case(in_data, date_s, date_c):
	delay = pd.Timedelta(date_c - date_s).days
	try:
		add_case_by_age(in_data, data_age[0], date_s, delay)
	except:
		global age_errors
		age_errors += 1
	try:
		add_case_by_zone(in_data, data_zone[0], date_s)
	except:
		global zone_errors
		zone_errors += 1

def add_death_case(in_data, date_s, date_c):
	delay = pd.Timedelta(date_c - date_s).days
	try:
		add_case_by_age(in_data, data_age[1], date_s, delay)
	except:
		global age_errors
		age_errors += 1
	try:
		add_case_by_zone(in_data, data_zone[1], date_s)
	except:
		global zone_errors
		zone_errors += 1

def add_dropped_case(in_data, date_s, date_c):
	delay = pd.Timedelta(date_c - date_s).days
	try:
		add_case_by_age(in_data, data_age[2], date_s, delay)
	except:
		global age_errors
		age_errors += 1
	try:
		add_case_by_zone(in_data, data_zone[2], date_s)
	except:
		global zone_errors
		zone_errors += 1

def add_case_by_age(in_data, out_df, date_s, delay):
	key = get_age_key(in_data["edad"])
	if in_data["genero"] == "femenino":
		out_df.loc[date_s][key + "F"] += 1
		out_df.loc[date_s]["TotalF"] += 1
	elif in_data["genero"] == "masculino":
		out_df.loc[date_s][key + "M"] += 1
		out_df.loc[date_s]["TotalM"] += 1
	out_df.loc[date_s][key] += 1
	out_df.loc[date_s]["Total"] += 1
	if delay > 0:
		out_df.loc[date_s]["DelayCount"] += 1
		out_df.loc[date_s]["CumDelay"] += delay

def add_case_by_zone(in_data, out_df, date_s):
	key = str(round(in_data["comuna"]))
	if in_data["genero"] == "femenino":
		out_df.loc[date_s][key + "F"] += 1
		out_df.loc[date_s]["TotalF"] += 1
	elif in_data["genero"] == "masculino":
		out_df.loc[date_s][key + "M"] += 1
		out_df.loc[date_s]["TotalM"] += 1
	out_df.loc[date_s][key] += 1
	out_df.loc[date_s]["Total"] += 1

#Deciding age group...
def get_age_key(in_key):
	p = 0
	while in_key > age_cuts[p]:
		p += 1
	return age_keys[p]

def run():
	print("-- Processing cases dataset...", end="\n")
	print("-- Which is huge. Be patient...", end="\n")
	#Variables to control sub_datasets
	step = 0
	steps = math.ceil(csv_lines/lines_step)
	done_lines = 1
	while step * lines_step < csv_lines:
		print("-- Step " + str(step + 1) + " of " + str(steps) + " completed...", end="\r")
		if done_lines + lines_step >= csv_lines - 1:
			lines = csv_lines - done_lines - 1
		else:
			lines = lines_step
		#Importing data from dataset_total_vacunas.csv
		c_data = pd.read_csv("datasets/" + filename, nrows=lines, skiprows=done_lines, names=csv_columns)
		c_data = c_data[c_data["provincia"] == "CABA"]
		c_data["fecha_toma_muestra"] = pd.to_datetime(c_data["fecha_toma_muestra"], format="%d%b%Y:%H:%M:%S.%f")
		c_data["fecha_clasificacion"] = pd.to_datetime(c_data["fecha_clasificacion"], format="%d%b%Y:%H:%M:%S.%f")
		process_data(c_data)
		done_lines += lines
		step += 1
	print("-- A total of " + str(done_lines) + " lines where processed.", end="\n")
	print("-- !!! Errors while processing by age: " + str(age_errors))
	print("-- !!! Errors while processing by zone: " + str(zone_errors))
	save_processed_data()

def process_data(c_data):
	c_data_c = c_data[c_data["clasificacion"] == "confirmado"]
	c_data_d = c_data[c_data["clasificacion"] == "descartado"]
	for i in range(c_data_c.shape[0]):
		row = c_data_c.loc[c_data_c.index[i]]
		add_confirmed_case(row, row["fecha_toma_muestra"], row["fecha_clasificacion"])
		if row["fallecido"] == "si":
			d_date = pd.to_datetime(row["fecha_fallecimiento"], format="%d%b%Y:%H:%M:%S.%f")
			add_death_case(row, row["fecha_toma_muestra"], d_date)
	for i in range(c_data_d.shape[0]):
		row = c_data_d.loc[c_data_d.index[i]]
		add_dropped_case(row, row["fecha_toma_muestra"], row["fecha_clasificacion"])

def get_delay_avg(in_df):
	in_df["DelayAvg"] = in_df["CumDelay"] / in_df["DelayCount"]

def save_processed_data():
	print("-- Preparing csv files...", end="\r")
	for t in range(len(data_type)):
		name = "cases_" + data_type[t]
		get_delay_avg(data_age[t])
		data_zone[t].to_csv("processed/" + name + "_byzone.csv")
		data_age[t].to_csv("processed/" + name + "_byage.csv")
		save_cum_sum(data_zone[t], name + "_byzone_cum.csv")
		save_averages(data_zone[t], name + "_byage_avg.csv")
		save_averages(data_age[t], name + "_byage_avg.csv")
		del data_age[t]["DelayAvg"]
		del data_age[t]["CumDelay"]
		del data_age[t]["DelayCount"]
		save_cum_sum(data_age[t], name + "_byage_cum.csv")
	print("-- Processed csv files saved!                 ", end="\n")
	print("-- This took " + str(get_time(start_time, tm.time())))

def save_cum_sum(in_df, f_name):
	cumsum = in_df.cumsum()
	cumsum.to_csv("processed/" + f_name)

def save_averages(in_df, f_name):
	avg = ut.build_averages(in_df, 7)
	avg.to_csv("processed/" + f_name)

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
