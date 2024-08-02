def wind_chill_index(temperature_in_fahreheit , wind_speed_miles_per_hour):
    ta = temperature_in_fahreheit
    v = wind_speed_miles_per_hour
    twc = 35.74 + (0.6215 * ta) - (35.75 * (v)**0.16) + 0.4275 * ta * (v)**0.16
    return f"The wind chill index is {twc:.5f}"
    

temperature_in_fahreheit = eval(input("Enter the temperature in fahreheit between -58 and 41: "))
wind_speed_miles_per_hour = eval(input("Enter the wind speed in miles per hour: "))
print(wind_chill_index(temperature_in_fahreheit , wind_speed_miles_per_hour))