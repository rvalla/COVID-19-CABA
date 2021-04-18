import time as tm
import util as ut
import pandas as pd

#Saving the moment in which this process start
start_time = None

#Output path:
output_path = "processed/"

#Importing data from llamados_107_covid.csv
calls_data = pd.read_csv("datasets/llamados_107_covid.csv")
calls_data["FECHA"] = pd.to_datetime(calls_data["FECHA"], format="%d%b%Y:%H:%M:%S")
calls_data.set_index("FECHA", inplace=True)
calls_data.sort_values(by=["FECHA"], inplace=True)

#Calculating some averages
def add_averages():
	in_columns = ["COVID_LLAMADOS", "CASOS_SOSPECHOSOS", "CASOS_DESCARTADOS_COVID", "CASOS_TRASLADADOS", "CASOS_DERIVADOS"]
	out_columns = ["LLAMADOSAVG", "SOSPECHOSOSAVG", "DESCARTADOSAVG", "TRASLADADOSAVG", "DERIVADOSAVG"]
	ut.add_averages(calls_data, 7, in_columns, out_columns)

#Adding some useful ratios
def add_ratios():
	in_columns = ["CASOS_SOSPECHOSOS", "CASOS_DESCARTADOS_COVID", "CASOS_TRASLADADOS", "CASOS_DERIVADOS",
				"SOSPECHOSOSAVG", "DESCARTADOSAVG", "TRASLADADOSAVG", "DERIVADOSAVG"]
	t_columns = ["COVID_LLAMADOS", "COVID_LLAMADOS", "COVID_LLAMADOS", "COVID_LLAMADOS",
				"LLAMADOSAVG", "LLAMADOSAVG", "LLAMADOSAVG", "LLAMADOSAVG"]
	out_columns = ["%SOSPECHOSOS", "%DESCARTADOS", "%TRASLADADOS", "%DERIVADOS", "%SOSPECHOSOSAVG",
				"%DESCARTADOSAVG", "%TRASLADADOSAVG", "%DERIVADOSAVG"]
	ut.add_ratios(calls_data, in_columns, t_columns, out_columns)

#Saving a new csv file
def save():
	calls_data.to_csv(output_path + "emergencycalls.csv")
	print("-- Processed csv file saved!                 ", end="\n")
	print("-- This took " + str(get_time(start_time, tm.time())))

def run():
	global start_time
	start_time = tm.time()
	print("-- Processing emergency calls data...", end="\n")
	add_averages()
	add_ratios()
	save()

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
