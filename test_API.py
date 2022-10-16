import requests

api_key = 'ab75a9292b4e4de9b55d1463f793b572'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

print(weather_data.json())