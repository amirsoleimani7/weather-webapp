from django.shortcuts import render
from django.http import HttpResponse
import requests , json


def index(request , user_city_name):

    api_key = "e3c83b511869492240dfe8d76dbfb1ef"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    city_name = "tehran"

    complete_url = base_url + "appid=" + api_key + "&=" + city_name

    response = requests.get(complete_url)
    
    x = response.json() 

    print(f"city is : {city_name}")
    print(f"response is ; {x}")


    
    # if x["cod"] not in [401 , 404]:
    #     # store the value of "main"
    #     # key in variable y
    #     y = x["main"]

    #     # store the value corresponding
    #     # to the "temp" key of y
    #     current_temperature = y["temp"]

    #     # store the value corresponding
    #     # to the "pressure" key of y
    #     current_pressure = y["pressure"]

    #     # store the value corresponding
    #     # to the "humidity" key of y
    #     current_humidity = y["humidity"]

    #     # store the value of "weather"
    #     # key in variable z
    #     z = x["weather"]

    #     # store the value corresponding 
    #     # to the "description" key at 
    #     # the 0th index of z
    #     weather_description = z[0]["description"]

    #     print(" Temperature (in kelvin unit) = " +
    #                     str(current_temperature) + 
    #         "\n atmospheric pressure (in hPa unit) = " +
    #                     str(current_pressure) +
    #         "\n humidity (in percentage) = " +
    #                     str(current_humidity) +
    #         "\n description = " +
    #                     str(weather_description))

    # else : 
    #     print("city not found !!")
    


    context = {

    }

    return render(request , 'main/index.html' , context)

