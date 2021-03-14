import pandas as pd

#Importing data from llamados_107_covid.csv
calls_data = pd.read_csv("datasets/llamados_107_covid.csv")
calls_data["FECHA"] = pd.to_datetime(calls_data["FECHA"], format="%d%b%Y:%H:%M:%S")
calls_data.set_index("FECHA", inplace=True)
calls_data.sort_values(by=["FECHA"], inplace=True)

def add_averages():
	in_columns = ["COVID_LLAMADOS", "CASOS_SOSPECHOSOS", "CASOS_DESCARTADOS_COVID", "CASOS_TRASLADADOS", "CASOS_DERIVADOS"]
	out_columns = ["LLAMADOSAVG", "SOSPECHOSOSAVG", "DESCARTADOSAVG", "TRASLADADOSAVG", "DERIVADOSAVG"]
	for c in range(len(in_columns)):
		for d in range(calls_data.shape[0] - 6):
			d0 = calls_data.loc[calls_data.index[d], in_columns[c]]
			d1 = calls_data.loc[calls_data.index[d+1], in_columns[c]]
			d2 = calls_data.loc[calls_data.index[d+2], in_columns[c]]
			d3 = calls_data.loc[calls_data.index[d+3], in_columns[c]]
			d4 = calls_data.loc[calls_data.index[d+4], in_columns[c]]
			d5 = calls_data.loc[calls_data.index[d+5], in_columns[c]]
			d6 = calls_data.loc[calls_data.index[d+6], in_columns[c]]
			calls_data.loc[calls_data.index[d+3], out_columns[c]] = (d0 + d1+ d2 + d3 + d4 + d5 + d6) / 7

#Adding some useful ratios
def add_ratios():
	print("-- Adding useful ratios...         ", end="\r")
	calls_data["%SOSPECHOSOS"] = calls_data["CASOS_SOSPECHOSOS"].div(calls_data["COVID_LLAMADOS"])
	calls_data["%DESCARTADOS"] = calls_data["CASOS_DESCARTADOS_COVID"].div(calls_data["COVID_LLAMADOS"])
	calls_data["%TRASLADADOS"] = calls_data["CASOS_TRASLADADOS"].div(calls_data["COVID_LLAMADOS"])
	calls_data["%DERIVADOS"] = calls_data["CASOS_DERIVADOS"].div(calls_data["COVID_LLAMADOS"])
	calls_data["%SOSPECHOSOSAVG"] = calls_data["SOSPECHOSOSAVG"].div(calls_data["LLAMADOSAVG"])
	calls_data["%DESCARTADOSAVG"] = calls_data["DESCARTADOSAVG"].div(calls_data["LLAMADOSAVG"])
	calls_data["%TRASLADADOSAVG"] = calls_data["TRASLADADOSAVG"].div(calls_data["LLAMADOSAVG"])
	calls_data["%DERIVADOSAVG"] = calls_data["DERIVADOSAVG"].div(calls_data["LLAMADOSAVG"])

#Saving a new csv file
def save():
	calls_data.to_csv("processed/emergencycalls.csv")
	print("-- Processed csv file saved!                 ", end="\n")

def run():
	add_averages()
	add_ratios()
	save()
