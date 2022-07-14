import json

from countryinfo import CountryInfo
country_title = input("Enter the name of the country (in English):")
country = CountryInfo(country_title)

with open("country_data", "w") as file:
    geo = country.geo_json()
    print(json.dump(geo, file, indent=4))


def country_info():
    return country.languages, country.currencies


print("In Uzbekistan people speak:", country.languages())
print("Local currency in Uzbekistan is:", country.currencies())


