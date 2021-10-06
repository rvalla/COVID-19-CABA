import p_emergencycalls as ecalls
import p_vaccinations as vac
import p_cases as cases
import p_analysis as sis

print("#############################################", end="\n")
print("   COVID-19: Buenos Aires city open data     ", end="\n")
print("---___________ Last 90 days -----------------", end="\n")
print("https://gitlab.com/rodrigovalla/covid-19-caba", end="\n")
print("---------------------------------------------", end="\n")

#Building emergency calls charts
ecalls.plot_calls_ratios_avg(0, 0.025,1)
ecalls.plot_total_calls_avg()

#Building vaccination champaign charts
vac.plot_doses_by_age_avg(0, 3000, 1000)
vac.plot_doses_by_vac_avg(0, 5000, 1000)

#Building cases charts
cases.plot_total_avg(0, 0, 250, 1, 3, 1)
cases.plot_cases_by_age_avg(0, 0, 50, 1, 2, 1)
cases.plot_cases_by_zone_avg(0, 0, 25, 2, 0.5, 1)

#Building analysis charts
sis.plot_age_ratios(0, 0, 0.3, 0.5, 0.1, 0.25)
