
import requests


def get_weather():
    print("=" * 40)
    print("     OASIS INFOBYTE - WEATHER APP")
    print("=" * 40)

    city = input("Enter city name: ").strip()

    if not city:
        print("Error: City name cannot be empty.")
        return

    api_key = input("Enter your OpenWeatherMap API key: ").strip()

    if not api_key:
        print("Error: API key cannot be empty.")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()

            print("\n----- WEATHER REPORT -----")
            print(f"City: {data['name']}")
            print(f"Temperature: {data['main']['temp']} °C")
            print(f"Feels like: {data['main']['feels_like']} °C")
            print(f"Humidity: {data['main']['humidity']}%")
            print(
                "Weather: "
                + data['weather'][0]['description'].title()
            )
            print("--------------------------")

        elif response.status_code == 404:
            print("Error: City not found. Check the city name.")

        elif response.status_code == 401:
            print("Error: Invalid API key or key not activated.")

        else:
            print(f"Weather service error: {response.status_code}")

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.RequestException:
        print("Error: Could not connect to the weather service.")


if __name__ == "__main__":
    get_weather()
