from abc import ABCMeta
import Constant as C
import DisplayStrategy as ds
import time

class WeightStrategy:
    __metaclass__ = ABCMeta
    StartWeight = 0
    Display = None
    
    @classmethod
    def __init__(cls, display):
        cls.Display = display

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
    beerAmount = 0

    @classmethod
    def get_current_weight(cls):
        cls.weight -= 1
        return cls.weight

    @classmethod
    def get_total_beers_amount(cls):
        return cls.startWeight / C.VOLUME

    @classmethod
    def get_finished_beer_amount(cls):
        pass

    @classmethod
    def get_full_beer_amount(cls):
        pass
    
    @classmethod
    def initialize_weights(cls):
        cls.Display.show_msg("Setting up \nBoard")
        time.sleep(1)
        cls.Display.show_msg("Please place one\nbeer at a time")
        time.sleep(1)
        for i in range(3):
            cls.beerAmount += 1
            cls.Display.show_msg(f"{cls.beerAmount} has been placed")
            time.sleep(1)
        
