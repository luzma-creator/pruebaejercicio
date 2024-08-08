import requests


def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def suggest_clothing(weather):
    temperature = weather['main']['temp']
    weather_condition = weather['weather'][0]['main']

    if temperature > 25:
        clothing = "Ropa ligera, como una camiseta y shorts."
    elif 15 < temperature <= 25:
        clothing = "Ropa cómoda, como una camiseta de manga larga o una sudadera ligera."
    elif 5 < temperature <= 15:
        clothing = "Ropa más abrigada, como una chaqueta o un suéter."
    else:
        clothing = "Ropa muy abrigada, como un abrigo, bufanda y guantes."

    if weather_condition in ["Rain", "Drizzle"]:
        clothing += " No olvides llevar un paraguas o una chaqueta impermeable."
    elif weather_condition in ["Snow"]:
        clothing += " No olvides llevar una chaqueta de invierno y botas."

    return clothing


def main():
    api_key = "TU_API_KEY"
    city = "Ciudad"
    weather = get_weather(api_key, city)

    if weather:
        clothing_suggestion = suggest_clothing(weather)
        print(
            f"El clima en {city} es {weather['weather'][0]['description']} con una temperatura de {weather['main']['temp']}°C.")
        print(f"Sugerencia de ropa: {clothing_suggestion}")
    else:
        print("No se pudo obtener el clima. Por favor, verifica la ciudad y tu API Key.")


if __name__ == "__main__":
    main()