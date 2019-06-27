from abc import ABCMeta


class WeightStrategy:
    __metaclass__ = ABCMeta

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


class FakeWeight(WeightStrategy):
    weight = 100

    @classmethod
    def get_current_weight(cls):
        return cls.weight

    @classmethod
    def get_total_beers_amount(cls):
        pass

    @classmethod
    def get_finished_beer_amount(cls):
        pass

    @classmethod
    def get_full_beer_amount(cls):
        pass
