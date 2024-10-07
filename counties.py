import requests
from bs4 import BeautifulSoup
import csv

# List of URLs to check
urls = [
    "https://www.pacertboard.org/class/recovery-specialist-241",
    "https://www.pacertboard.org/class/recovery-specialist-242",
    # Add the rest of the URLs here...
    "https://www.pacertboard.org/class/recovery-specialist-340"
]

# Function to find and return the location from the specified HTML structure
def find_location(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    location_div = soup.find('div', class_='block-field-blocknodeclassfield-class-location')
    if location_div:
        location = location_div.find('div', class_='field__item')
        if location:
            return location.get_text(strip=True)
    return "Location not found"

# Open a CSV file to write the results
with open("classes_in_counties.csv", "w", newline='') as csvfile:
    fieldnames = ['URL', 'Location']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for url in urls:
        location = find_location(url)
        writer.writerow({'URL': url, 'Location': location})

print("Results have been saved to classes_in_counties.csv")

from google.colab import files
files.download('classes_in_counties.csv')
