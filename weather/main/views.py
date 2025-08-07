from django.shortcuts import render
from django.http import HttpResponse
import requests , json


def index(request):

    api_key = "e3c83b511869492240dfe8d76dbfb1ef"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    city_name = request.GET.get('city_id')

    complete_url = f"{base_url}?q={city_name}&appid={api_key}"
 
    response = requests.get(complete_url)
    
    x = response.json()
    context =  {}


    context['city'] = city_name

    if city_name :     
        if x["cod"] not in ['401' , '404']:
            y = x["main"]

            current_temperature = y["temp"] - 273.15 
            context['current_temperature'] = round(current_temperature , 3)
            context['current_pressure'] = y["pressure"]
            context['current_humidity'] = y["humidity"]
            z = x["weather"]
            context['weather_description'] = z[0]["description"]

        else : 
            print("city not found !!")
    

    print(f"the context is : {context}")
    return render(request , 'main/index.html' , context)

