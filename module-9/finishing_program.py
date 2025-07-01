import requests
import json

print("This program tests an API connection and retrieves data from") 
print("the Open Notify API. It shows both the raw and formatted responses,")
print("listing all astronauts currently in space.")

# Step 1: Test connection to Google
print("Testing connection to Google...")
google_response = requests.get('http://www.google.com')
print("Google Status Code:", google_response.status_code)
print()

# Step 2: Test connection to astronauts API
print("Testing connection to astronauts API...")
astro_response = requests.get('http://api.open-notify.org/astros.json')
print("Astronauts API Status Code:", astro_response.status_code)
print()

# Step 3: Print unformatted JSON response
print("Unformatted JSON response from API:")
print(astro_response.text)
print()

# Step 4: Format and print the astronaut data
print("Formatted Output:")
data = astro_response.json()
print(f"There are {data['number']} astronauts currently in space:\n")

for person in data['people']:
    print(f"- {person['name']} on the {person['craft']}")