import util as ut
import pandas as pd

#Importing demographics data...
demographics = pd.read_csv("demographics_c.csv")

#Setting time period
start_date = "2020-12-29"
end_date = "2021-03-25"
period = pd.date_range(start_date, end_date)
csv_lines = 3256
lines_step = 1500
csv_columns = ["FECHA_ADMINISTRACION","GRUPO_ETARIO","GENERO","VACUNA","TIPO_EFECTOR","DOSIS_1","DOSIS_2","ID_CARGA"]

#Building blank dataframe for organizing data by age
age_in = ["30 o menos","31 a 40","41 a 50","51 a 60","61 a 70","71 a 80","81 a 90","91 o mas"]
age_k = {"30 o menos":"<=30","31 a 40":"31-40","41 a 50":"41-50","51 a 60":"51-60",
			"61 a 70":"61-70","71 a 80":"71-80","81 a 90":"81-90","91 o mas":">=91"}
age_c_d = ["<=30A","<=30B","<=30","31-40A","31-40B","31-40","41-50A","41-50B","41-50","51-60A","51-60B","51-60",
		"61-70A","61-70B","61-70","71-80A","71-80B","71-80","81-90A","81-90B","81-90",">=91A",">=91B",">=91",
		"TotalA","TotalB","Total"]
age_c_s = ["<=30M","<=30F","<=30","31-40M","31-40F","31-40","41-50M","41-50F","41-50","51-60M","51-60F","51-60",
		"61-70M","61-70F","61-70","71-80M","71-80F","71-80","81-90M","81-90F","81-90",">=91M",">=91F",">=91",
		"TotalM","TotalF","Total"]
d_age_dose = pd.DataFrame(0, index=period, columns=age_c_d)
d_age_sex = pd.DataFrame(0, index=period, columns=age_c_s)
d_age_dose.index.name = "FECHA"
d_age_sex.index.name = "FECHA"

#Processing data in dataframe by age
def by_age_and_dose(in_data, out_df, date):
	key = get_age_key(in_data["GRUPO_ETARIO"])
	d1 = in_data["DOSIS_1"]
	d2 = in_data["DOSIS_2"]
	t = d1 + d2
	out_df.loc[date,key + "A"] += d1
	out_df.loc[date,"Total" + "A"] += d1
	out_df.loc[date,key + "B"] += d2
	out_df.loc[date,"Total" + "B"] += d2
	out_df.loc[date,key] += t
	out_df.loc[date,"Total"] += t

def by_age_and_sex(in_data, out_df, date):
	key = get_age_key(in_data["GRUPO_ETARIO"])
	d1 = in_data["DOSIS_1"]
	d2 = in_data["DOSIS_2"]
	t = d1 + d2
	if in_data["GENERO"] == "M":
		out_df.loc[date,key + "M"] += t
		out_df.loc[date,"Total" + "M"] += t
	elif in_data["GENERO"] == "F":
		out_df.loc[date,key + "F"] += t
		out_df.loc[date,"Total" + "F"] += t
	out_df.loc[date,key] += t
	out_df.loc[date,"Total"] += t

def get_age_key(in_key):
	return age_k[in_key]

#Building blank dataframe for organizing data by vaccine
vac_c = ["SputnikA", "SputnikB", "Sputnik", "CovishieldA", "CovishieldB", "Covishield",
			"SinopharmA", "SinopharmB", "Sinopharm", "TotalA", "TotalB", "Total"]
d_vac = pd.DataFrame(0, index=period, columns=vac_c)
d_vac.index.name = "FECHA"

def by_vaccine(in_data, out_df, date):
	key = in_data.loc["VACUNA"]
	d1 = in_data["DOSIS_1"]
	d2 = in_data["DOSIS_2"]
	t = d1 + d2
	out_df.loc[date,key + "A"] += d1
	out_df.loc[date,"Total" + "A"] += d1
	out_df.loc[date,key + "B"] += d2
	out_df.loc[date,"Total" + "B"] += d2
	out_df.loc[date,key] += t
	out_df.loc[date,"Total"] += t

def run():
	print("-- Processing vaccination campaign data...", end="\n")
	#Variables to control sub_datasets
	step = 0
	done_lines = 1
	while step * lines_step < csv_lines:
		print("-- Step " + str(step) + " completed...", end="\r")
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
	save_processed_data()

def process_data(vac_data):
	for i in range(vac_data.shape[0]):
		row = vac_data.loc[vac_data.index[i]]
		date = vac_data.loc[vac_data.index[i], "FECHA_ADMINISTRACION"]
		by_age_and_dose(row, d_age_dose, date)
		by_age_and_sex(row, d_age_sex, date)
		by_vaccine(row, d_vac, date)

def save_processed_data():
	print("-- Saving csv files...", end="\r")
	d_age_dose.to_csv("processed/vaccinationbyageanddose.csv")
	d_age_sex.to_csv("processed/vaccinationbyageandsex.csv")
	d_vac.to_csv("processed/vaccinationbyvaccine.csv")
	build_cum_sums()
	build_averages()
	print("-- Processed csv files saved!                 ", end="\n")

def build_cum_sums():
	cum_age_dose = d_age_dose.cumsum()
	cum_age_sex = d_age_sex.cumsum()
	cum_vac = d_vac.cumsum()
	cum_age_dose.to_csv("processed/cum_vaccinationbyageanddose.csv")
	cum_age_sex.to_csv("processed/cum_vaccinationbyageandsex.csv")
	cum_vac.to_csv("processed/cum_vaccinationbyvaccine.csv")

def build_averages():
	d_age_dose_avg = ut.build_averages(d_age_dose, 7)
	d_vac_avg = ut.build_averages(d_vac, 7)
	d_age_dose_avg.to_csv("processed/vaccinationbyageanddoseavg.csv")
	d_vac_avg.to_csv("processed/vaccinationbyvaccineavg.csv")
