from abc import ABCMeta
import Constant as C
import DisplayStrategy as ds

class WeightStrategy:
    __metaclass__ = ABCMeta
    StartWeight
    Display
    
    @classmethod
    def __init__(cls, display):
        Display = display

    @classmethod
    def get_current_weight(cls):
        raise NotImplementedError

    @classmethod
    def get_total_beers_amount(cls):
        raise NotImplementedError

    @classmethod
    def get_finished_beer_amount(cls):
        raise NotImplementedError

    @classmethod
    def get_full_beer_amount(cls):
        raise NotImplementedError

    @classmethod
    def initialize_weights(cls):
        raise NotImplementedError

class FakeWeight(WeightStrategy):
    weight = 100
    startWeight = weight

    @classmethod
    def get_current_weight(cls):
        weight = weight - 1
        return weight

    @classmethod
    def get_total_beers_amount(cls):
        return startWeight / C.VOLUME

    @classmethod
    def get_finished_beer_amount(cls):
        pass

    @classmethod
    def get_full_beer_amount(cls):
        pass
    
    @classmethod
    def initialize_weights(cls):
        pass


print(FakeWeight().get_total_beers_amount())
print(FakeWeight().get_current_weight())

