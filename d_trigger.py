import d_emergencycalls as ecalls
import d_vaccinations as vac

print("#############################################", end="\n")
print("   COVID-19: Buenos Aires city open data     ", end="\n")
print("---------------------------------------------", end="\n")
print("https://gitlab.com/rodrigovalla/covid-19-caba", end="\n")
print("---------------------------------------------", end="\n")

#Building data from emergency calls
ecalls.run()

#print("-- Processing vaccination campaign data...", end="\n")
vac.run()
