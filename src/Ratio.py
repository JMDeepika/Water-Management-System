from src import Apartment
import math

class Ratio_:
    def __init__(self, ratio, month_water_allowed):
        self.corporation = int(ratio[0])
        self.borewell = int(ratio[2])
        self.month_water_allowed = month_water_allowed
    def corporation_part(self):
        corporation_rate_per_litre = 1
        waterrate_from_corporation = round((self.corporation * self.month_water_allowed * corporation_rate_per_litre)/
                                     (self.corporation + self.borewell))
        return waterrate_from_corporation
    def borewell_part(self):
        borewell_rate_per_litre = 1.5
        waterrate_from_borewell = ((self.borewell * self.month_water_allowed)/
                                   (self.corporation + self.borewell))
        if math.ceil(waterrate_from_borewell) - waterrate_from_borewell == 0.5:
            waterrate_from_borewell = math.ceil(waterrate_from_borewell)
        else:
            waterrate_from_borewell = round(waterrate_from_borewell)
        waterrate_from_borewell = waterrate_from_borewell * borewell_rate_per_litre
        if math.ceil(waterrate_from_borewell) - waterrate_from_borewell == 0.5:
            waterrate_from_borewell = math.ceil(waterrate_from_borewell)
        else:
            waterrate_from_borewell = round(waterrate_from_borewell)
        return waterrate_from_borewell
