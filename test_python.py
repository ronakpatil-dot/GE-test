import requests

def get_quick_weather(city="Bangalore"):
    # Format '3' returns a short, simple string (e.g., "Bangalore: ⛅️ +28°C")
    url = f"https://wttr.in/{city}?format=3"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Current Weather:")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    get_quick_weather()
