import requests
import pandas as pd
import matplotlib.pyplot as plt

# Configuration
API_KEY = "db0e404ee01ab76957be6cff5fecf8bf"  # Replace with your OpenWeatherMap API Key
cities = ["London", "New York", "Tokyo", "Mumbai", "Sydney"]
data = []

# Fetch data from API
for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        data.append({
            "City": city,
            "Temperature": json_data["main"]["temp"],
            "Humidity": json_data["main"]["humidity"],
            "Pressure": json_data["main"]["pressure"]
        })
    else:
        print(f"Failed to fetch data for {city}")

# Create DataFrame
df = pd.DataFrame(data)

# Plot using Matplotlib
plt.figure(figsize=(10, 5))
plt.bar(df['City'], df['Temperature'], color='orange')
plt.title('Temperature by City')
plt.xlabel('City')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()