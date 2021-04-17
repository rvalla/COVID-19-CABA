import p_emergencycalls as ecalls
import p_vaccinations as vac
import p_cases as cases
import p_analysis as sis

print("#############################################", end="\n")
print("   COVID-19: Buenos Aires city open data     ", end="\n")
print("---------------------------------------------", end="\n")
print("https://gitlab.com/rodrigovalla/covid-19-caba", end="\n")
print("---------------------------------------------", end="\n")

#Building emergency calls charts
ecalls.plot_calls_ratios_avg(0, 0.05,1)
ecalls.plot_total_calls_avg()

#Building vaccination champaign charts
vac.plot_total_vac_by_sex(0, 100000, 1000)
vac.plot_total_vac_by_dose(0, 100000, 1000)
vac.plot_doses_by_age(0, 3000, 1000)
vac.plot_doses_by_age_avg(0, 3000, 1000)
vac.plot_doses_by_vac_avg(0, 2000, 1000)
vac.plot_reached_population_by_age(0, 0.25, 1)
vac.plot_reached_population_by_sex(0.05, 1)

#Building cases charts
cases.plot_total_cases(0, 0, 50000, 1000, 1500, 1000)
cases.plot_total_avg(0, 0, 500, 1, 15, 1)
cases.plot_delay_evol(0, 0, 1, 1, 5, 1)
cases.plot_cases_by_age_avg(0, 0, 250, 1, 5, 1)

#Building analysis charts
sis.plot_estimation_avg(0, 0, 3000, 1000, 0.25, 1)
sis.plot_estimation(0, 0, 500000, 1000000, 0.05, 1)
sis.plot_deathrate_by_sex_and_age(0,0,0.05,0.25)
sis.plot_deathrate_by_age(0, 0.05)
sis.plot_age_ratios(0, 0, 0.3, 0.5, 0.1, 0.25)
sis.plot_sex_ratios(0.45, 0.2, 0.50, 0.6, 0.05, 0.2)
