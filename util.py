import pandas as pd

#Addign averages...
def add_averages(dataframe, width, in_columns, out_columns):
	for c in range(len(in_columns)):
		for d in range(dataframe.shape[0] - width + 1):
			t = 0
			for i in range(width):
				t += dataframe.loc[dataframe.index[d + i], in_columns[c]]
			dataframe.loc[dataframe.index[d+width//2], out_columns[c]] = t / width

#Addign averages...
def build_averages(dataframe, width):
	columns = dataframe.columns
	new_data = pd.DataFrame(index=dataframe.index, columns=columns)
	for c in range(len(columns)):
		for d in range(dataframe.shape[0] - width + 1):
			t = 0
			for i in range(width):
				t += dataframe.loc[dataframe.index[d + i], columns[c]]
			new_data.loc[new_data.index[d+width//2], columns[c]] = t / width
	return new_data

#Adding ratios
def add_ratios(dataframe, in_columns, t_columns, out_columns):
	for i in range(len(in_columns)):
		dataframe[out_columns[i]] = dataframe[in_columns[i]].div(dataframe[t_columns[i]])
