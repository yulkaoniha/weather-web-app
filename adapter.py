class Continental_climate:
    def __init__(self):
        self.name = "Continental climate"

    def SmallAmountPrecipitation(self):
        return "small amount of precipitation"


class Polar_climate:
    def __init__(self):
        self.name = "Polar climate"

    def AverageTemp(self):
        return "average temperature less than 10 °C"


class Intertropical:
    def __init__(self):
        self.name = "Intertropical Convergence Zone"

    def Placing(self):
        return "by liying near the geographic Equator"


class Adapter:

    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__


if __name__ == "__main__":

    climates = []

    сontinental = Continental_climate()
    climates.append(
        Adapter(сontinental, characteristic=сontinental.SmallAmountPrecipitation))

    polar = Polar_climate()
    climates.append(Adapter(polar, characteristic=polar.AverageTemp))

    intertropical = Intertropical()
    climates.append(
        Adapter(intertropical, characteristic=intertropical.Placing))

    for climate in climates:
        print("{0} is characterized with {1} ".format(
            climate.name, climate.characteristic()))
