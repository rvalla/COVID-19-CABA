import d_emergencycalls as ecalls
import d_vaccinations as vac
import d_cases as cases
import d_analysis as analysis

print("#############################################", end="\n")
print("   COVID-19: Buenos Aires city open data     ", end="\n")
print("---------------------------------------------", end="\n")
print("https://gitlab.com/rodrigovalla/covid-19-caba", end="\n")
print("---------------------------------------------", end="\n")

#Building data from cases dataset
cases.run()

#Building data from emergency calls
ecalls.run()

#Building data from vaccination champaing dataset
#vac.run()

#Building some estimations and ratios
analysis.run()
