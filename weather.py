import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def get_weather(city):
    try:
        # Encode the city name for use in a URL
        query = quote(f"{city} weather")
        url = f"https://www.google.com/search?q={query}"
        
        # Set the headers to mimic a browser request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        
        # Perform the request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        
        # Parse the response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Attempt to extract weather data using various common patterns
        temperature = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
        condition = soup.find("div", class_="BNeawe tAd8D AP7Wnd").text
        
        # Further parse to remove unwanted text
        condition = condition.split('\n')[1] if '\n' in condition else condition
        
        return f"The current weather in {city.capitalize()} is {temperature} with {condition}."
    
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"

def main():
    city = input("Enter the name of the city: ").strip()
    weather_info = get_weather(city)
    
    print(weather_info)

if __name__ == "__main__":
    main()
