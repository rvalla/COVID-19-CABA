import math
import time as tm
import datetime as dt
import util as ut
import pandas as pd

#Saving the moment in which this process start
start_time = None

#Output path:
output_path = "processed/"

filename = "casos_covid19.csv"
data_type = ["confirmed", "deaths", "dropped"]
data_zone = []
data_age = []
data_origin = []
age_errors = 0
zone_errors = 0
delay_errors = 0
origin_errors = 0
d_age_errors = 0
d_zone_errors = 0
d_delay_errors = 0
d_origin_errors = 0

#Setting time period
start_date = "2020-03-15"
end_date = "2021-04-30"
period = pd.date_range(start_date, end_date)
csv_lines = 2283283
lines_step = 10000
age_cuts = [11,21,31,41,51,61,71,81,91,1000]
age_keys = ["<=10", "11-20", "21-30","31-40","41-50","51-60","61-70","71-80","81-90",">=91"]
zone_keys = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
origin_keys = ["S", "C", "CE", "E", "I"]
csv_columns = ["numero_de_caso","fecha_apertura_snvs","fecha_toma_muestra","fecha_clasificacion","provincia","barrio",
				"comuna","genero","edad","clasificacion","fecha_fallecimiento","fallecido","fecha_alta","tipo_contagio"]
zone_c_s = ["1M","1F","1","2M","2F","2","3M","3F","3","4M","4F","4","5M","5F","5","6M","6F","6","7M","7F","7",
			"8M","8F","8","9M","9F","9","10M","10F","10","11M","11F","11","12M","12F","12","13M","13F","13",
			"14M","14F","14","15M","15F","15","TotalM","TotalF","Total"]
age_c_s = ["<=10M","<=10F","<=10","11-20M","11-20F","11-20","21-30M","21-30F","21-30","31-40M","31-40F","31-40",
		"41-50M","41-50F","41-50","51-60M","51-60F","51-60","61-70M","61-70F","61-70","71-80M","71-80F","71-80",
		"81-90M","81-90F","81-90",">=91M",">=91F",">=91","TotalM","TotalF","Total", "DelayCount", "CumDelay", "DelayAvg"]
origin_c = ["SM", "SF", "S", "CM", "CF", "C", "CEM", "CEF", "CE", "EM", "EF", "E", "IM", "IF", "I", "TotalM","TotalF","Total"]
for d in range(len(data_type)):
	data_zone.append(pd.DataFrame(0, index=period, columns=zone_c_s))
	data_age.append(pd.DataFrame(0, index=period, columns=age_c_s))
	data_zone[d].index.name = "FECHA"
	data_age[d].index.name = "FECHA"
	if d < 2:
		data_origin.append(pd.DataFrame(0, index=period, columns=origin_c))
		data_origin[d].index.name = "FECHA"

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
	try:
		add_case_by_origin(in_data, data_origin[0], date_s)
	except:
		global origin_errors
		origin_errors += 1

def add_death_case(in_data, date_s, date_c):
	delay = pd.Timedelta(date_c - date_s).days
	try:
		add_case_by_age(in_data, data_age[1], date_s, delay)
	except:
		global d_age_errors
		d_age_errors += 1
	try:
		add_case_by_zone(in_data, data_zone[1], date_s)
	except:
		global d_zone_errors
		d_zone_errors += 1
	try:
		add_case_by_origin(in_data, data_origin[1], date_s)
	except:
		global d_origin_errors
		d_origin_errors += 1

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
	elif in_data["genero"] == "masculino":
		out_df.loc[date_s][key + "M"] += 1
	if delay >= 0:
		out_df.loc[date_s]["DelayCount"] += 1
		out_df.loc[date_s]["CumDelay"] += delay
	else:
		global delay_errors
		delay_errors += 1

def add_case_by_zone(in_data, out_df, date_s):
	key = str(round(in_data["comuna"]))
	if in_data["genero"] == "femenino":
		out_df.loc[date_s][key + "F"] += 1
	elif in_data["genero"] == "masculino":
		out_df.loc[date_s][key + "M"] += 1

def add_case_by_origin(in_data, out_df, date_s):
	key = get_origin_key(in_data["tipo_contagio"])
	if in_data["genero"] == "femenino":
		out_df.loc[date_s][key + "F"] += 1
	elif in_data["genero"] == "masculino":
		out_df.loc[date_s][key + "M"] += 1

#Deciding age group...
def get_age_key(in_key):
	p = 0
	while in_key > age_cuts[p]:
		p += 1
	return age_keys[p]

#Deciding origin key...
origins = {"Trabajador de la Salud": "S", "Comunitario": "C", "Contacto": "CE", "En Investigación": "E", "Importado": "I"}
def get_origin_key(in_key):
	return origins[in_key]

def run():
	global start_time
	start_time = tm.time()
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
	write_log()
	complete_data_sums()
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

def complete_data_sums():
	for t in range(len(data_type)):
		data_sums(data_age[t], age_keys, ["M","F"])
		data_sums(data_zone[t], zone_keys, ["M","F"])
		if t < 2:
			data_sums(data_origin[t], origin_keys, ["M","F"])

def data_sums(in_df, in_c, in_l):
	for c in in_c:
		a = in_df[c + in_l[0]]
		b = in_df[c + in_l[1]]
		in_df[c] = a + b
		in_df["Total" + in_l[0]] += a
		in_df["Total" + in_l[1]] += b
	in_df["Total"] = in_df["Total" + in_l[0]] + in_df["Total" + in_l[1]]

def save_processed_data():
	print("-- Preparing csv files...", end="\r")
	for t in range(len(data_type)):
		name = "cases_" + data_type[t]
		get_delay_avg(data_age[t])
		data_zone[t].to_csv(output_path + "" + name + "_byzone.csv")
		data_age[t].to_csv(output_path + "" + name + "_byage.csv")
		if t < 2:
			data_origin[t].to_csv(output_path + "" + name + "_byorigin.csv")
			save_averages(data_origin[t], name + "_byorigin_avg.csv")
		save_cum_sum(data_zone[t], name + "_byzone_cum.csv")
		save_averages(data_zone[t], name + "_byzone_avg.csv")
		save_averages(data_age[t], name + "_byage_avg.csv")
		del data_age[t]["DelayAvg"]
		del data_age[t]["CumDelay"]
		del data_age[t]["DelayCount"]
		save_cum_sum(data_age[t], name + "_byage_cum.csv")
	print("-- Processed csv files saved!                 ", end="\n")
	print("-- This took " + str(get_time(start_time, tm.time())))

def save_cum_sum(in_df, f_name):
	cumsum = in_df.cumsum()
	cumsum.to_csv(output_path + "" + f_name)

def save_averages(in_df, f_name):
	avg = ut.build_averages(in_df, 7)
	avg.to_csv(output_path + f_name)

def write_log():
	log = open(output_path + "log.md", "a")
	m = "-- !!! Errors while processing by age: " + str(age_errors) + " (" + str(round((age_errors/csv_lines)*100,2)) + "%)" + "\n"
	m += "-- !!! Errors while processing by zone: " + str(zone_errors) + " (" + str(round((zone_errors/csv_lines)*100,2)) + "%)" + "\n"
	m += "-- !!! Errors while processing by origin: " + str(origin_errors) + " (" + str(round((origin_errors/csv_lines)*100,2)) + "%)" + "\n"
	m += "-- !!! Errors while processing delays: " + str(delay_errors) + " (" + str(round((delay_errors/csv_lines)*100,2)) + "%)"
	today = dt.date.today()
	log.write("\n")
	log.write("### %s"%today)
	log.write(":" + "\n")
	log.write(m)
	log.write("\n")
	log.close()
	print(m)

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
