class Tanker:
    def __init__(self, guests):
        self.water_guests_consume = guests * 10 * 30
        self.rate = 0

    def guest_water_consumption(self):
        return self.water_guests_consume

    def tanker_water_bill(self):
        slab_0_500 = 2
        slab_501_1500 = 3
        slab_1501_3000 = 5
        slab_3001_ = 8
        water_available = self.water_guests_consume
        #duplicate value to keep tracking the slab
        if self.water_guests_consume > 500:
            water_available -= 500
            self.rate += 500 * slab_0_500
        else:
            self.rate += self.water_guests_consume * slab_0_500
            return self.rate
        if self.water_guests_consume > 1500:
            water_available -= 1000
            self.rate += 1000 * slab_501_1500
        else:
            self.rate += water_available * slab_501_1500
            return self.rate
        if self.water_guests_consume > 3000:
            water_available -= 1500
            self.rate += 1500 * slab_1501_3000
        else:
            self.rate += water_available * slab_1501_3000
            return self.rate
        if self.water_guests_consume > 3000:
            self.rate += water_available * slab_3001_
        return self.rate
