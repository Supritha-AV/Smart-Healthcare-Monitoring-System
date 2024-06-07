import requests

# Replace YOUR_API_KEY with your Google Places API key
api_key = "YOUR_API_KEY"

# Replace YOUR_LATITUDE and YOUR_LONGITUDE with your current geo location
latitude = "YOUR_LATITUDE"
longitude = "YOUR_LONGITUDE"

# Set the search parameters
search_type = "hospital"
radius = 5000

# Define the Google Places API endpoint URL
url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={radius}&type={search_type}&key={api_key}"

# Send a GET request to the Google Places API endpoint
response = requests.get(url)

# Extract the JSON data from the response
data = response.json()
print(data)

# Generate a Google Maps link for each nearby hospital
for result in data["results"]:
    name = result['name']
    vicinity = result['vicinity']
    location = f"{result['geometry']['location']['lat']},{result['geometry']['location']['lng']}"
    maps_link = f"https://www.google.com/maps/search/?api=1&query={location}"
    print(f"{name} ({vicinity}): {maps_link}")
