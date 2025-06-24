# Write a function that accepts two parameters: a city name and a country name. 
# The function should return a single string of the form City, Country, such as 
# Santiago, Chile. Store the function in a file named city_functions.py. In the 
# same file, call the function at least three times using a City, Country values. 
# Excecute city_functions.py and take a screenshot of the result. Paste that 
# screenshot into your Word document.
print("//////3 Cities and their Countries !\\\\")
def city_country(city, country):
    return f"{city.title()}, {country.title()}"

# Call the function at least 3 times
print(city_country("santiago", "chile"))
print(city_country("denver", "united states"))
print(city_country("fontana", "united states"))

#updated 
#Now modify your city_country function in city_functions.py so that the language argument is #optional.
def city_country(city, country, population=None, language=None):
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result

# Test all 3 versions
print(city_country("santiago", "chile"))
print(city_country("denver", "united states", 700000))
print(city_country("fontana", "united states", 13960000, "english/spanish"))