import pandas as pd
from geopy.geocoders import Nominatim
from collections import Counter
import time

coordinates = [
  your data
]

# Initialize the geocoder
geolocator = Nominatim(user_agent="coordinate_analysis")


def get_country_from_coords(lat, lon):
  try:
    location = geolocator.reverse((lat, lon), language='en', exactly_one=True)
    if location and location.raw.get('address'):
      return location.raw['address'].get('country', 'Unknown')
    return 'Unknown'
  except Exception as e:
    print(f"Error getting country for ({lat}, {lon}): {e}")
    return 'Error'


# Analyze the countries of all coordinates
all_countries = []
print(f"Start analyzing {len(coordinates)} coordinate points...")

for i, (lat, lon) in enumerate(coordinates):
  country = get_country_from_coords(lat, lon)
  all_countries.append(country)
  print(f"Progress: {i + 1}/{len(coordinates)} - ({lat}, {lon}) -> {country}")

  # Follow API limits, max 1 request per second
  time.sleep(1)

# Calculate country counts
country_counts = Counter(all_countries)
total_coordinates = len(coordinates)

# Get the top four countries
top_8 = country_counts.most_common(8)

print("\nTop 8 countries and their percentages:")
print("-" * 40)
for country, count in top_8:
  percentage = (count / total_coordinates) * 100
  print(f"{country}: {percentage:.2f}% ({count} coordinate points)")

# Calculate the total proportion of the top 8
top_8_total = sum(count for country, count in top_8)
top_8_percentage = (top_8_total / total_coordinates) * 100
print(f"\nTotal of top four countries: {top_8_percentage:.2f}%")
print(f"All other countries: {100 - top_8_percentage:.2f}%")