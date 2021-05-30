class Strategy:
    def __init__(self, search_by_city_name=None):
        if search_by_city_name is not None:
            self.search_by_city_name = search_by_city_name

    def search_by_city_name(self):
        print('Пошук за назвою міста(за замовчуаванням)')


def search_by_cityID():
    print('Пошук за ID міста')


def search_by_coordinates():
    print('Пошук по географічним координатам')


strategy_default = Strategy()
strategy_default.search_by_city_name()

strategy_cityID = Strategy(search_by_cityID)
strategy_cityID.search_by_city_name()

strategy_coordinates = Strategy(search_by_coordinates)
strategy_coordinates.search_by_city_name()
