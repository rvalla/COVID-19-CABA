import util as ut
import pandas as pd

#Importing demographics data...
demographics = pd.read_csv("demographics_c.csv")

#Setting time period
start_date = "2020-12-29"
end_date = "2021-03-24"
period = pd.date_range(start_date, end_date)
csv_lines = 3181
lines_step = 1000
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
def by_age_and_dose(in_df, out_df):
	for i in range(in_df.shape[0]):
		date = in_df.loc[in_df.index[i], "FECHA_ADMINISTRACION"]
		key = get_age_key(in_df["GRUPO_ETARIO"].values[i])
		d1 = in_df["DOSIS_1"].values[i]
		d2 = in_df["DOSIS_2"].values[i]
		t = d1 + d2
		out_df.loc[date,key + "A"] += d1
		out_df.loc[date,"Total" + "A"] += d1
		out_df.loc[date,key + "B"] += d2
		out_df.loc[date,"Total" + "B"] += d2
		out_df.loc[date,key] += t
		out_df.loc[date,"Total"] += t

def by_age_and_sex(in_df, out_df):
	for i in range(in_df.shape[0]):
		date = in_df.loc[in_df.index[i], "FECHA_ADMINISTRACION"]
		key = get_age_key(in_df["GRUPO_ETARIO"].values[i])
		d1 = in_df["DOSIS_1"].values[i]
		d2 = in_df["DOSIS_2"].values[i]
		t = d1 + d2
		if in_df["GENERO"].values[i] == "M":
			out_df.loc[date,key + "M"] += t
			out_df.loc[date,"Total" + "M"] += t
		elif in_df["GENERO"].values[i] == "F":
			out_df.loc[date,key + "F"] += t
			out_df.loc[date,"Total" + "F"] += t
		out_df.loc[date,key] += t
		out_df.loc[date,"Total"] += t

def get_age_key(in_key):
	return age_k[in_key]

#def by_vaccine_dataset():

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
		by_age_and_dose(vac_data, d_age_dose)
		by_age_and_sex(vac_data, d_age_sex)
		done_lines += lines
		step += 1
	print("-- A total of " + str(done_lines) + " lines where processed.", end="\n")
	print("-- Saving csv files...", end="\r")
	d_age_dose.to_csv("processed/vaccinationbyageanddose.csv")
	d_age_sex.to_csv("processed/vaccinationbyageandsex.csv")
	cum_age_dose = d_age_dose.cumsum()
	cum_age_sex = d_age_sex.cumsum()
	cum_age_dose.to_csv("processed/cum_vaccinationbyageanddose.csv")
	cum_age_sex.to_csv("processed/cum_vaccinationbyageandsex.csv")
	print("-- Processed csv files saved!                 ", end="\n")
