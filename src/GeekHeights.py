from src import Apartment
from src import TankerBill

class Geekheights:
    def __init__(self, file_data):
        self.no_of_guests = 0
        if file_data[0][0] == 'ALLOT_WATER':
            #self.bhk = ,self.corporation_borewell_ratio = 
            apartment_object = Apartment.Apartment_(file_data[0][1], file_data[0][2])
            self.resident_water_bill = Apartment.Apartment_.resident_water_bill_calculation(apartment_object)
            self.resident_water_allowed = apartment_object.month_water_allowed
        for arguments in file_data[1:-1]:
            if arguments[0] =='ADD_GUESTS':
                self.total_no_of_guests(arguments[1])
        if self.no_of_guests == 0:
            self.total_guest_bill = 0
            self.total_extra_water = 0
        else:
            tanker_object = TankerBill.Tanker(self.no_of_guests)
            self.total_guest_bill = TankerBill.Tanker.tanker_water_bill(tanker_object)
            self.total_extra_water = TankerBill.Tanker.guest_water_consumption(tanker_object)
            
            
    def total_no_of_guests(self, addguests):
        self.no_of_guests += int(addguests)

    def total_bill(self):
        return self.resident_water_bill + self.total_guest_bill

    def total_water_consumption(self):
        return self.resident_water_allowed + self.total_extra_water
        
        
#a = Geekheights([['ALLOT_WATER', '3', '2:1'],
 #  ['ADD_GUESTS', '4'], ['ADD_GUESTS', '1'], ['BILL']])
