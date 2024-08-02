def main():

    current_population =  312032486

    birth_per_seconds = 7
    death_per_seconds = 13
    immigrants_per_seconds = 45

    seconds_per_year = 365 * 24 * 60 * 60

    birth_per_year = seconds_per_year // birth_per_seconds
    death_per_year = seconds_per_year // death_per_seconds
    immigrants_per_year = seconds_per_year // immigrants_per_seconds

    net_population_change_per_year = birth_per_year + immigrants_per_year - death_per_year

    number_of_years = eval(input("Enter number of years:"))

    for year in range(1 , number_of_years + 1):
        current_population += net_population_change_per_year 
        print(f"Year {year}: {current_population}")

main()