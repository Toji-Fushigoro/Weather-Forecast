import requests

api_key = '4dc4ad39e214e278db131d99873b7dd1'
user_input = input("What is the name of your city? ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

print(weather_data.status_code)

weather = weather_data.json()['weather'][0]['main']
description = weather_data.json()['weather'][0]['description']
temperature = weather_data.json()['main']['temp']
temp_cel = (temperature-32)/1.8

if weather_data.status_code == 200:
    print("The weather today in",user_input,"is",weather)
    print("The weather today feels",description)
    print("In which format do you want the temperature?(C/F)")
    n = input(":/> ")
    if n == 'C' or n == 'c':
        print("The temperatuer in",user_input,"in celsius is", temp_cel)
    elif n == "F" or n == "f":
        primt("The temperature in",user_input,"in farenheight is", temperature)

else:
    print("Error!!")

