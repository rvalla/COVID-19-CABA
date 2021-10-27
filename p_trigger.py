import p_emergencycalls as ecalls
import p_vaccinations as vac
import p_cases as cases
import p_analysis as sis
import chart_config as cc

print("#############################################", end="\n")
print("   COVID-19: Buenos Aires city open data     ", end="\n")
print("---------------------------------------------", end="\n")
print("https://gitlab.com/rodrigovalla/covid-19-caba", end="\n")
print("---------------------------------------------", end="\n")

#Date configuration for general charts...
cc.chart_path = "charts/"
cc.start_date = "2020-03-15"
cc.week_interval = 6
cc.v_start_date = "2021-01-01"
cc.v_week_interval = 3
cc.e_start_date = "2020-03-15"
cc.e_week_interval = 6

#Building emergency calls charts
ecalls.plot_calls_ratios_avg(0, 0.2, 1, cc)
ecalls.plot_total_calls_avg(cc)

#Building vaccination champaign charts
vac.plot_total_vac_by_sex(0, 400000, 1000, cc)
vac.plot_total_vac_by_dose(0, 400000, 1000, cc)
vac.plot_doses_by_age_avg(0, 3000, 1000, cc)
vac.plot_doses_by_vac_avg(0, 5000, 1000, cc)
vac.plot_reached_population_by_age(0, 0.25, 1, cc)
vac.plot_reached_population_by_sex(0.1, 1, cc)

#Building cases charts
cases.plot_delay_evol(0, 0, 5, 5, 1, 1, cc)
cases.plot_total_avg(0, 0, 1000, 1000, 15, 1, cc)
cases.plot_total_cases(0, 0, 150000, 1000, 2500, 1000, cc)
cases.plot_cases_by_age_avg(0, 0, 250, 1, 5, 1, cc)
cases.plot_cases_by_zone_avg(0, 0, 75, 2, 1, 1, cc)

#Building analysis charts
sis.plot_age_ratios(0, 0, 0.5, 1.0, 0.1, 0.25, cc)
sis.plot_origin_ratios(0, 0, 1, 1, 0.25, 0.25, cc)
sis.plot_sex_ratios(0.5, 0.5, 1, 1, 0.2, 0.2, cc)
sis.plot_deathrate_by_age(0, 1, cc)
sis.plot_deathrate_by_sex_and_age(0.2, 1, 0.05, 0.25, cc)
sis.plot_estimation_avg(0, 0, 2000, 1000, 3, 1, cc)
sis.plot_estimation(0, 0, 500000, 1000000, 0.1, 1, cc)

#Last 180 days...
#Date configuration for general charts...
cc.chart_path = "charts/last_180/"
cc.start_date = "2021-02-26"
cc.week_interval = 3
cc.v_start_date = "2021-02-26"
cc.v_week_interval = 3
cc.e_start_date = "2021-02-26"
cc.e_week_interval = 3

#Building emergency calls charts
ecalls.plot_calls_ratios_avg(0, 0.025,1, cc)
ecalls.plot_total_calls_avg(cc)

#Building vaccination champaign charts
vac.plot_doses_by_age_avg(0, 3000, 1000, cc)
vac.plot_doses_by_vac_avg(0, 5000, 1000, cc)

#Building cases charts
cases.plot_total_avg(0, 0, 500, 1, 10, 1, cc)
cases.plot_cases_by_age_avg(0, 0, 150, 1, 5, 1, cc)
cases.plot_cases_by_zone_avg(0, 0, 25, 1, 5, 1, cc)

#Building analysis charts
sis.plot_age_ratios(0, 0, 0.3, 1, 0.1, 0.25, cc)

#Last 90 days...
#Date configuration for general charts...
cc.chart_path = "charts/last_90/"
cc.start_date = "2021-07-26"
cc.week_interval = 2
cc.v_start_date = "2021-07-26"
cc.v_week_interval = 2
cc.e_start_date = "2021-07-26"
cc.e_week_interval = 2

#Building emergency calls charts
ecalls.plot_calls_ratios_avg(0, 0.025,1, cc)
ecalls.plot_total_calls_avg(cc)

#Building vaccination champaign charts
vac.plot_doses_by_age_avg(0, 3000, 1000, cc)
vac.plot_doses_by_vac_avg(0, 5000, 1000, cc)

#Building cases charts
cases.plot_total_avg(0, 0, 125, 1, 3, 1, cc)
cases.plot_cases_by_age_avg(0, 0, 50, 1, 1, 1, cc)
cases.plot_cases_by_zone_avg(0, 0, 25, 1, 1, 1, cc)

#Building analysis charts
sis.plot_age_ratios(0, 0, 0.3, 1, 0.1, 0.25, cc)

#Last 30 days...
#Date configuration for general charts...
cc.chart_path = "charts/last_30/"
cc.start_date = "2021-09-26"
cc.week_interval = 1
cc.v_start_date = "2021-09-26"
cc.v_week_interval = 1
cc.e_start_date = "2021-09-26"
cc.e_week_interval = 1

#Building emergency calls charts
ecalls.plot_calls_ratios_avg(0, 0.025,1, cc)
ecalls.plot_total_calls_avg(cc)

#Building vaccination champaign charts
vac.plot_doses_by_age_avg(0, 3000, 1000, cc)
vac.plot_doses_by_vac_avg(0, 5000, 1000, cc)

#Building cases charts
cases.plot_total_avg(0, 0, 50, 1, 1, 1, cc)
cases.plot_cases_by_age_avg(0, 0, 10, 1, 1, 1, cc)
cases.plot_cases_by_zone_avg(0, 0, 5, 1, 1, 1, cc)

#Building analysis charts
sis.plot_age_ratios(0, 0, 0.3, 1, 0.1, 0.25, cc)
