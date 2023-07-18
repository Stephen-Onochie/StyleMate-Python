import http.client

conn = http.client.HTTPSConnection("weatherapi-com.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "7e5ccd8f73msh0de7c965c7f0099p1c2d8ejsnae8e7d33865d",
    'X-RapidAPI-Host': "weatherapi-com.p.rapidapi.com"
}


# gets current temperature (f) in a given zipcode area
def get_current_temp(zipcode):
    pass


# gets current wind speed (mph) in a given zipcode area
def get_current_wind(zipcode):
    pass


# gets current humidity (%) in a given zipcode area
def get_current_humidity(zipcode):
    pass


# gets current uv index in a given zipcode area
def get_current_uv_index(zipcode):
    pass


# gets temp forecast for next 10 days and returns as a list
def get_forecast(zipcode):
    pass


def main():
    conn.request("GET", "/current.json?q=46231", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


if __name__ == '__main__':
    main()