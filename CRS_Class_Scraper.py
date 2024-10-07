import csv
import requests
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = [f"https://www.pacertboard.org/class/recovery-specialist-{i}" for i in range(201, 321)]

# Function to scrape data from a single URL
def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the class number from the URL
    class_number = url.split('-')[-1]
    
    # Extract the location
    location_div = soup.find('div', class_='block-field-blocknodeclassfield-class-location')
    location = location_div.find('div', class_='field__item').text.strip() if location_div else 'N/A'
    
    # Extract the organization
    organization_div = soup.find('div', class_='block-field-blocknodeclassfield-sponsoring-organization')
    organization = organization_div.find('div', class_='field__item').text.strip() if organization_div else 'N/A'
    
    # Extract the instructor
    instructor_div = soup.find('div', class_='block-views-block-views-blockclass-instructor-block-1')
    instructor = instructor_div.find('div', class_='field__item').text.strip() if instructor_div else 'N/A'
    
    # Extract the dates
    dates_div = soup.find('div', class_='block-field-blocknodeclassfield-class-dates')
    dates = dates_div.find('div', class_='field__item').text.strip() if dates_div else 'N/A'
    
    return {
        'Class Number': class_number,
        'Location': location,
        'Organization': organization,
        'Instructor': instructor,
        'Dates': dates
    }

# List to store the scraped data
data_list = []

# Scrape data from each URL and add it to the list
for url in urls:
    data_list.append(scrape_data(url))

# Write the data to a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Class Number', 'Location', 'Organization', 'Instructor', 'Dates']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for data in data_list:
        writer.writerow(data)

print("Data has been scraped and saved to scraped_data.csv")
