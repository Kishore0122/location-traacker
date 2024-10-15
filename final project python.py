n = input("Enter a phone number: ")
phone_number1 = "+" + n  # Convert to international format

import phonenumbers
from phonenumbers import carrier, geocoder
import requests

def get_location(phone_number):
    # Parse the phone number
    phone_info = phonenumbers.parse(phone_number, None)

    # Get carrier information directly from the parsed phone number
    carrier_name = carrier.name_for_number(phone_info, 'en')

    # Get the location using geocoder
    location = geocoder.description_for_number(phone_info, "en")

    return carrier_name, location

# Example usage
carrier_name, location = get_location(phone_number1)
print("\nPhone number location:")
print("Carrier Name:", carrier_name)
print("Location:", location)

# Alternative method using OpenStreetMap Nominatim (not recommended for accurate location)
def get_location_with_nominatim(phone_number):
    phone_info = phonenumbers.parse(phone_number, None)
    carrier_name = carrier.name_for_number(phone_info, 'en')
    search_url = f"https://nominatim.openstreetmap.org/search?format=json&q={carrier_name}&polygon_geojson=1"
    response = requests.get(search_url)
    data = response.json()
    if data:
        return data[0]['display_name']
    else:
        return None

# Example usage
print("\nPhone number location using Nominatim:")
print(get_location_with_nominatim(phone_number1))
