""""def years_days(minutes):
    days_in_a_year = 365
    minutes_in_a_day = 60 * 24
    minutes_per_year = days_in_a_year * minutes_in_a_day
    years = minutes // minutes_per_year
    remaining_minutes = minutes % minutes_per_year
    days = remaining_minutes // minutes_in_a_day
    return f"{minutes} minutes is approximately {years}  years and {days}  days"


minutes = int(input("Enter the number of minutes: "))
print(years_days(minutes))"""

def years_days1(minutes):
    days_in_a_year = 365
    minutes_in_a_day = 24 * 60
    minutes_in_a_year = days_in_a_year * minutes_in_a_day

    years = minutes // minutes_in_a_year
    remaining_minutes = minutes % minutes_in_a_year
    days = remaining_minutes // minutes_in_a_day

    return f"{minutes} minutes is approximately {years} years and {days} days"

minutes = eval(input("Enter the number of minutes: "))
print(years_days1(minutes))