import json
import time
import urllib.request

API = "uGtAKOhA4GNT1D1ABucHbnai8xkoZHG9"
countryCode = "Ke"
city = input("City name:")
key = ""


def getLocation(CountryCode, city):
    search_address = "http://dataservice.accuweather.com/locations/v1/cities/" + CountryCode + "/search?apikey=%09uGtAKOhA4GNT1D1ABucHbnai8xkoZHG9&q=" + city + "&details=true&offset=0&alias=Kenya"
    # print(search_address)
    with urllib.request.urlopen(search_address)as search_address:
        data = json.loads(search_address.read().decode())
    # print(data)
    location_key = data[0]["Key"]
    return location_key


def getLocationForecast(location_key):
    dailyForecastUrl = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" + location_key + "?apikey=uGtAKOhA4GNT1D1ABucHbnai8xkoZHG9&details=true&metric=true"
    with urllib.request.urlopen(dailyForecastUrl)as dataForecastUrl:
        data = json.loads(dataForecastUrl.read().decode())
    for x in data['DailyForecasts']:
        print("weather forecast for"+x["Date"])
        print("Minimum temperature in(C) :"+str(x["Temperature"]["Minimum"]["Value"]))
        print("Maximum temperature in(C) :"+str(x["Temperature"]["Maximum"]["Value"]))
        print("Probability of rain : "+str(x["Day"]["PrecipitationProbability"]))
        print("**********************************")


key = getLocation(countryCode, city)
getLocationForecast(key)
