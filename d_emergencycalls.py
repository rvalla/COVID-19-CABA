import util as ut
import pandas as pd

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
	calls_data.to_csv("processed/emergencycalls.csv")
	print("-- Processed csv file saved!                 ", end="\n")

def run():
	print("-- Processing emergency calls data...", end="\n")
	add_averages()
	add_ratios()
	save()
