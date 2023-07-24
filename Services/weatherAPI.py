import http.client
import json

conn = http.client.HTTPSConnection("weatherapi-com.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "7e5ccd8f73msh0de7c965c7f0099p1c2d8ejsnae8e7d33865d",
    'X-RapidAPI-Host': "weatherapi-com.p.rapidapi.com"
}


# gets current temperature (f) in a given zipcode area
# Done Add code to get current temp of zipcode
def get_current_temp(zipcode):
    request = f"/current.json?q={str(zipcode)}"
    conn.request("GET", request, headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")

    weather_data = json.loads(data)
    current_temp = weather_data['current']['temp_f']
    return current_temp


# gets current wind speed (mph) in a given zipcode area
# Done Add code to get current wind speed with zipcde
def get_current_wind(zipcode):
    request = f"/current.json?q={str(zipcode)}"
    conn.request("GET", request, headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")

    weather_data = json.loads(data)
    wind_speed = weather_data['current']['wind_mph']
    return wind_speed


# gets current humidity (%) in a given zipcode area
# Done Add code to get current humidity with zipcode
def get_current_humidity(zipcode):
    request = f"/current.json?q={str(zipcode)}"
    conn.request("GET", request, headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    weather_data = json.loads(data)
    humidity = weather_data['current']['humidity']
    return humidity


# gets current uv index in a given zipcode area
# Done Add code to get current uv index with zipcode
def get_current_uv_index(zipcode):
    request = f"/current.json?q={str(zipcode)}"
    conn.request("GET", request, headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    weather_data = json.loads(data)
    uv_index = weather_data['current']['uv']
    return uv_index


# gets temp forecast for next 3 days and returns as a list
# Done Add code to get 3 day forecast in a list with zipcode
def get_forecast(zipcode):
    forecast_list = []
    request = f"/forecast.json?q={str(zipcode)}&days=3"
    conn.request("GET", request, headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    weather_data = json.loads(data)

    for day in range(3):
        temp = weather_data['forecast']['forecastday'][day]['day']["avgtemp_f"]
        forecast_list.append(temp)

    return forecast_list


def main():
    pass


if __name__ == '__main__':
    main()
