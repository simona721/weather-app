import requests
import tkinter as tk

def getWeather(window):

    city = textfield.get()
    api = "yourapikeyhere"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&exclude=current,hourly,minutely,alerts&units=metric&appid={api}"



    response = requests.get(url).json()

    weather = response["weather"][0]["main"] 
    temperature = int(response["main"]["temp"]) 
    feelsLike = int(response["main"]["feels_like"])
    wind = response["wind"]["speed"]


    #print(f"The weather in {city} is {weather}, the temperature is {temperature}°C and it feels like {feelsLike}°C the wind is {wind} km/h. ")
    temp = f"{temperature}°C"
    weatherConditions = f"The weather today is: {weather} \n It feels like: {feelsLike} \n The wind is: {wind} m/h"
    label1.config(text=temp)
    label2.config(text=weatherConditions)


window = tk.Tk()

window.geometry("600x500")

window.title("Weather App")

textfield = tk.Entry(window, justify="center")
textfield.pack(pady=20)
textfield.focus()
textfield.bind("<Return>", getWeather)

label1 = tk.Label(window, font="poppins 20 bold", justify="center")
label1.pack()

label2 = tk.Label(window, font=" Areal 15", justify="center")
label2.pack()



window.mainloop()