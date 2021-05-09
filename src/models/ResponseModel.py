class ResponseModel(object):
    name = ''
    address = ''
    district = ''
    block = ''
    fee = ''
    vaccine = ''
    available_capacity = ''
    date = ''
    slots = ''

    def __init__(self):
        print('response initialize')

    def __init__(self, name, address, district, block, fee, vaccine, available_capacity, date, slots):
        self.name = name
        self.address = address
        self.district = district
        self.block = block
        self.fee = fee
        self.vaccine = vaccine
        self.available_capacity = available_capacity
        self.date = date
        self.slots = slots

    def __str__(self):
        return 'Name: ' + self.name + ' Address: ' + self.address + ' District: ' + self.district + ' Block: ' + \
               self.block + ' Fee: ' + self.fee + ' Vaccine: ' + self.vaccine + ' Available Capacity: ' + \
               self.available_capacity.__str__() + ' Date: ' + self.date + ' Slots: ' + self.slots.__str__()
