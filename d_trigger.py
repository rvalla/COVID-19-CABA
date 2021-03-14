import d_emergencycalls as ecalls

print("#############################################", end="\n")
print("   COVID-19: Buenos Aires city open data     ", end="\n")
print("---------------------------------------------", end="\n")
print("https://gitlab.com/rodrigovalla/covid-19-caba", end="\n")
print("---------------------------------------------", end="\n")

#Building data from emergency calls
print("-- Processing emergency calls data...", end="\n")
ecalls.run()
