import pandas as pd
import numpy as np

# Constants
current_age = 31
retirement_age = 65
years_of_service = retirement_age - current_age

initial_basic_pay = 75000
annual_increment = 2000
hra_percentage = 0.20
initial_ta = 7200
da_increment_rate = 0.03  # every six months, so 6% yearly
service_tax_monthly = 200
nps_contribution_rate = 0.10  # of basic + DA
xirr_rate = 0.12  # assumed XIRR for NPS corpus

# Salary hike years
hike_years = [4, 8, 12, 20]
hike_percentage = 0.30

# Pay commission years (assuming same cycle as past)
pay_commission_years = [2006, 2016, 2026, 2036, 2046]
start_year = 2025

# Initialize DataFrame
data = []

basic_pay = initial_basic_pay
ta = initial_ta
da_percentage = 0.0

for year in range(start_year, start_year + years_of_service):
    year_index = year - start_year

    # Apply annual increment
    if year_index > 0:
        basic_pay += annual_increment

    # Apply pay commission doubling
    if year in pay_commission_years:
        basic_pay *= 2
        ta *= 2
        da_percentage = 0.0  # reset DA

    # Apply service-based hike
    if year_index in hike_years:
        basic_pay *= 1 + hike_percentage

    # Increase DA annually by 6% (3% every six months)
    da_percentage += da_increment_rate * 2
    da = basic_pay * da_percentage

    hra = basic_pay * hra_percentage
    total_ta = ta + da
    gross_salary = basic_pay + da + hra + total_ta

    # Monthly deductions
    service_tax = service_tax_monthly * 12
    nps_contribution = (basic_pay + da) * nps_contribution_rate * 12
    net_income = gross_salary * 12 - service_tax - nps_contribution

    data.append({
        "Year": year,
        "Basic Pay": basic_pay,
        "DA %": da_percentage,
        "DA": da,
        "HRA": hra,
        "TA": total_ta,
        "Gross Income": gross_salary * 12,
        "NPS Contribution": nps_contribution,
        "Service Tax": service_tax,
        "Net Income": net_income
    })

# Create DataFrame
df = pd.DataFrame(data)

# NPS Corpus Calculation using XIRR approximation
cash_flows = [-row["NPS Contribution"] for row in data]
dates = [pd.Timestamp(f"{row['Year']}-07-01") for row in data]
final_value_year = df["Year"].iloc[-1]
final_date = pd.Timestamp(f"{final_value_year}-07-01")

# Estimate future value of NPS corpus
nps_corpus = 0
for i, cf in enumerate(cash_flows):
    years_to_retirement = (final_date - dates[i]).days / 365.25
    nps_corpus += cf * ((1 + xirr_rate) ** years_to_retirement)

# Display first few years and final corpus
print(df)
print(f"\nEstimated NPS Corpus at Retirement (with 12% XIRR): Rs. {nps_corpus:,.2f}")
df.to_csv('Salary.csv', index=False)