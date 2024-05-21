from src import Ratio

class Apartment_:
    def __init__(self, apartment_type, ratio):
        number_of_litres_allowed = 10
        number_of_days = 30
        if apartment_type == '2':
            no_of_people = 3
        if apartment_type == '3':
            no_of_people = 5
        self.ratio = ratio
        self.month_water_allowed = no_of_people * number_of_litres_allowed * number_of_days
    def resident_water_bill_calculation(self):
        ratio_object = Ratio.Ratio_(self.ratio, self.month_water_allowed)
        corporation_water_rate = ratio_object.corporation_part()
        borewell_water_rate = ratio_object.borewell_part()
        return corporation_water_rate + borewell_water_rate
    
