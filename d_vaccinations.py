import math
import time as tm
import util as ut
import pandas as pd

#Saving the moment in which this process start
start_time = None

#Output path:
output_path = "processed/"

#Importing demographics data...
demographics = pd.read_csv("demographics_v.csv")
demographics.set_index("Age", inplace=True)

#Setting time period
start_date = "2020-12-29"
end_date = "2021-04-23"
period = pd.date_range(start_date, end_date)
csv_lines = 5098
lines_step = 2000
csv_columns = ["FECHA_ADMINISTRACION","GRUPO_ETARIO","GENERO","VACUNA","TIPO_EFECTOR","DOSIS_1","DOSIS_2","ID_CARGA"]

#Building blank dataframe for organizing data by age
ages = ["<=30","31-40","41-50","51-60","61-70","71-80","81-90",">=91"]
age_in = ["30 o menos","31 a 40","41 a 50","51 a 60","61 a 70","71 a 80","81 a 90","91 o mas"]
age_k = {"30 o menos":"<=30","31 a 40":"31-40","41 a 50":"41-50","51 a 60":"51-60",
			"61 a 70":"61-70","71 a 80":"71-80","81 a 90":"81-90","91 o mas":">=91"}
age_c_d = ["TotalA","TotalB","Total","<=30A","<=30B","<=30","31-40A","31-40B","31-40","41-50A","41-50B","41-50",
		"51-60A","51-60B","51-60","61-70A","61-70B","61-70","71-80A","71-80B","71-80","81-90A","81-90B","81-90",
		">=91A",">=91B",">=91"]
age_c_s = ["TotalM","TotalF","Total","<=30M","<=30F","<=30","31-40M","31-40F","31-40","41-50M","41-50F","41-50",
		"51-60M","51-60F","51-60","61-70M","61-70F","61-70","71-80M","71-80F","71-80","81-90M","81-90F","81-90",
		">=91M",">=91F",">=91"]
d_age_dose = pd.DataFrame(0, index=period, columns=age_c_d)
d_age_sex = pd.DataFrame(0, index=period, columns=age_c_s)
d_age_dose.index.name = "FECHA"
d_age_sex.index.name = "FECHA"

#Processing data in dataframe by age
def by_age_and_dose(in_data, out_df, date):
	key = get_age_key(in_data["GRUPO_ETARIO"])
	d1 = in_data["DOSIS_1"]
	d2 = in_data["DOSIS_2"]
	out_df.loc[date,key + "A"] += d1
	out_df.loc[date,key + "B"] += d2

def by_age_and_sex(in_data, out_df, date):
	key = get_age_key(in_data["GRUPO_ETARIO"])
	d1 = in_data["DOSIS_1"]
	d2 = in_data["DOSIS_2"]
	t = d1 + d2
	if in_data["GENERO"] == "M":
		out_df.loc[date,key + "M"] += t
	elif in_data["GENERO"] == "F":
		out_df.loc[date,key + "F"] += t

def get_age_key(in_key):
	return age_k[in_key]

#Building blank dataframe for organizing data by vaccine
vaccines = ["Sputnik", "Covishield", "Sinopharm", "AstraZeneca"]
vac_in = {"Sputnik": "Sputnik", "Covishield": "Covishield", "Sinopharm": "Sinopharm",
			"AstraZeneca": "AstraZeneca"}
vac_c = ["SputnikA", "SputnikB", "Sputnik", "CovishieldA", "CovishieldB", "Covishield",
			"SinopharmA", "SinopharmB", "Sinopharm", "AstraZenecaA", "AstraZenecaB", "AstraZeneca",
			"TotalA", "TotalB", "Total"]
d_vac = pd.DataFrame(0, index=period, columns=vac_c)
d_vac.index.name = "FECHA"

def by_vaccine(in_data, out_df, date):
	#key = get_vac_key(in_data.loc["VACUNA"])
	key = in_data.loc["VACUNA"]
	d1 = in_data["DOSIS_1"]
	d2 = in_data["DOSIS_2"]
	out_df.loc[date,key + "A"] += d1
	out_df.loc[date,key + "B"] += d2

def get_vac_key(vac_field):
	return vac_in[vac_field]

def run():
	global start_time
	start_time = tm.time()
	print("-- Processing vaccination campaign data...", end="\n")
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
		vac_data = pd.read_csv("datasets/dataset_total_vacunas.csv", nrows=lines, skiprows=done_lines, names=csv_columns)
		vac_data["FECHA_ADMINISTRACION"] = pd.to_datetime(vac_data["FECHA_ADMINISTRACION"], format="%d%b%Y:%H:%M:%S")
		process_data(vac_data)
		done_lines += lines
		step += 1
	print("-- A total of " + str(done_lines) + " lines where processed.", end="\n")
	complete_data_sums()
	save_processed_data()

def process_data(vac_data):
	for i in range(vac_data.shape[0]):
		row = vac_data.loc[vac_data.index[i]]
		date = vac_data.loc[vac_data.index[i], "FECHA_ADMINISTRACION"]
		by_age_and_dose(row, d_age_dose, date)
		by_age_and_sex(row, d_age_sex, date)
		by_vaccine(row, d_vac, date)

def complete_data_sums():
	data_sums(d_age_dose, ages, ["A","B"])
	data_sums(d_age_sex, ages, ["M","F"])
	data_sums(d_vac, vaccines, ["A","B"])

def data_sums(in_df, in_c, in_l):
	for c in in_c:
		a = in_df[c + in_l[0]]
		b = in_df[c + in_l[1]]
		in_df[c] = a + b
		in_df["Total" + in_l[0]] += a
		in_df["Total" + in_l[1]] += b
	in_df["Total"] = in_df["Total" + in_l[0]] + in_df["Total" + in_l[1]]

def save_processed_data():
	print("-- Saving csv files...", end="\r")
	d_age_dose.to_csv(output_path + "vaccinationbyageanddose.csv")
	d_age_sex.to_csv(output_path + "vaccinationbyageandsex.csv")
	d_vac.to_csv(output_path + "vaccinationbyvaccine.csv")
	cum_age_dose = d_age_dose.cumsum()
	cum_age_dose.to_csv(output_path + "vaccinationbyageanddose_cum.csv")
	cum_age_sex = d_age_sex.cumsum()
	cum_age_sex.to_csv(output_path + "vaccinationbyageandsex_cum.csv")
	cum_vac = d_vac.cumsum()
	cum_vac.to_csv(output_path + "vaccinationbyvaccine_cum.csv")
	d_age_dose_avg = ut.build_averages(d_age_dose, 7)
	d_age_dose_avg.to_csv(output_path + "vaccinationbyageanddoseavg.csv")
	d_vac_avg = ut.build_averages(d_vac, 7)
	d_vac_avg.to_csv(output_path + "vaccinationbyvaccineavg.csv")
	build_reached_population_by_sex(cum_age_sex)
	build_reached_population_by_dose(cum_age_dose)
	print("-- Processed csv files saved!                 ", end="\n")
	print("-- This took " + str(get_time(start_time, tm.time())))

#This process the data in place so is necessary to save the .csv file before.
def build_reached_population_by_sex(cum_data):
	cum_data[">=81M"] = cum_data["81-90M"] + cum_data[">=91M"]
	cum_data[">=81F"] = cum_data["81-90F"] + cum_data[">=91F"]
	cum_data[">=81"] = cum_data["81-90"] + cum_data[">=91"]
	del cum_data["81-90M"]
	del cum_data["81-90F"]
	del cum_data["81-90"]
	del cum_data[">=91M"]
	del cum_data[">=91F"]
	del cum_data[">=91"]
	ages_r = ["<=30","31-40","41-50","51-60","61-70","71-80",">=81","Total"]
	for c in ages_r:
		cum_data[c + "M"] = cum_data[c + "M"] / demographics.loc[c, "Men"]
		cum_data[c + "F"] = cum_data[c + "F"] / demographics.loc[c, "Women"]
		cum_data[c] = cum_data[c] / demographics.loc[c, "Both"]
	cum_data.to_csv(output_path + "vaccinationbyageandsex_reached.csv")

def build_reached_population_by_dose(cum_data):
	cum_data[">=81A"] = cum_data["81-90A"] + cum_data[">=91A"]
	cum_data[">=81B"] = cum_data["81-90B"] + cum_data[">=91B"]
	cum_data[">=81"] = cum_data["81-90"] + cum_data[">=91"]
	del cum_data["81-90A"]
	del cum_data["81-90B"]
	del cum_data["81-90"]
	del cum_data[">=91A"]
	del cum_data[">=91B"]
	del cum_data[">=91"]
	ages = ["<=30","31-40","41-50","51-60","61-70","71-80",">=81","Total"]
	for c in ages:
		cum_data[c + "A"] = cum_data[c + "A"] / demographics.loc[c, "Both"]
		cum_data[c + "B"] = cum_data[c + "B"] / demographics.loc[c, "Both"]
		cum_data[c] = cum_data[c] / demographics.loc[c, "Both"]
	cum_data.to_csv(output_path + "vaccinationbyageanddose_reached.csv")

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
