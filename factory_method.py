class Weather(object):
    precipitation = ""

    def get_data(self):
        return self.precipitation


class Heavy_snowfall(Weather):
    precipitation = "0.5 mm/hr"


class Light_rain(Weather):
    precipitation = "0.4 mm/hr"


class Sunny(Weather):
    precipitation = "0 mm/hr"


class WeatherFactory():
    def create(self, typ):
        targetclass = typ.capitalize()
        return globals()[targetclass]()


weather_conditions = WeatherFactory()
weather = ['heavy_snowfall', 'light_rain', 'sunny']
for w in weather:
    print(weather_conditions.create(w).get_data())
