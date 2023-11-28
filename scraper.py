import requests
from bs4 import BeautifulSoup
import csv

# The URL of the website you want to scrape
url = "https://www.eazydiner.com/chennai/restaurants"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Success!")
else:
    print(f"Error: {response.status_code}")
    exit()

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Look for the specific XPath locators that contain the restaurant names and ratings
restaurant_names= soup.findAll('h3', class_='grey res_name font-20 bold inline-block')
restaurant_ratings = soup.findAll('span', class_='critic')

# Create or open the CSV file with write permissions
with open('restaurants.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)  # Create a csv writer object
    writer.writerow(["Name", "Rating"])  # Write the header row

    # Loop through the list of restaurant names and ratings
    for name_element, rating_element in zip(restaurant_names, restaurant_ratings):
        # Extract the name and rating
        name = name_element.text.strip()
        rating = rating_element.text.strip()

        # Write a row with the name and rating
        writer.writerow([name, rating])

        # Debug print
        print(f"Name: {name}, Rating: {rating}")

print("Data has been scraped and saved to restaurants.csv.")
