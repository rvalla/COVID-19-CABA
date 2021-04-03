import p_emergencycalls as ecalls
import p_vaccinations as vac

print("#############################################", end="\n")
print("   COVID-19: Buenos Aires city open data     ", end="\n")
print("---------------------------------------------", end="\n")
print("https://gitlab.com/rodrigovalla/covid-19-caba", end="\n")
print("---------------------------------------------", end="\n")

#Building emergency calls charts
ecalls.plot_calls_ratios()
ecalls.plot_calls_ratios_avg()
ecalls.plot_total_calls()
ecalls.plot_total_calls_avg()

#Building vaccination champaign charts
vac.plot_total_vac_by_sex()
vac.plot_total_vac_by_dose()
vac.plot_doses_by_age()
vac.plot_doses_by_age_avg()
vac.plot_doses_by_vac_avg()
vac.plot_reached_population_by_age()
vac.plot_reached_population_by_sex()
