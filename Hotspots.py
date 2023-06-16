import pandas as pd
import folium

# Read the dataset into a pandas DataFrame
data = pd.read_csv('crime4.csv')

# Group the data by latitude and longitude and count the number of crimes in each location
crime_counts = data.groupby(['latitude', 'longitude']).size().reset_index(name='Count')

# Filter out locations with fewer than a certain threshold of crimes (adjust the threshold as needed)
threshold = 5
hotspots = crime_counts[crime_counts['Count'] >= threshold]

# Create a map centered around the mean latitude and longitude of the hotspots
map_center = [hotspots['latitude'].mean(), hotspots['longitude'].mean()]
crime_map = folium.Map(location=map_center, zoom_start=12)

# Add markers for each hotspot to the map
for _, hotspot in hotspots.iterrows():
    count = hotspot['Count']
    lat, lon = hotspot['latitude'], hotspot['longitude']
    folium.Marker([lat, lon], popup=f'Crime Count: {count}').add_to(crime_map)

# Save the map to an HTML file
crime_map.save('crime_hotspots_map.html')