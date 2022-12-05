class booking():
    __booking_id = ''
    __booking_date = ''
    __num_weeks = 0
    __property_owner_name = ''
    __contact_number = ''
    __address = ''
    __rooms = 0
    __rooms_cost = 0
    __garden_area = 0
    __garden_area_cost = 0

    def __init__(self, booking_id = '', booking_date = '', num_weeks = 0, property_owner_name = '', contact_number = '', address = '', rooms = 0, rooms_cost = 0, garden_area = 0, garden_area_cost = 0):
        self.__booking_id = booking_id
        self.__booking_date = booking_date
        self.__num_weeks = num_weeks
        self.__property_owner_name = property_owner_name
        self.__contact_number = contact_number
        self.__address = address
        self.__rooms = rooms
        self.__rooms_cost = rooms_cost
        self.__garden_area = garden_area
        self.__garden_area_cost = garden_area_cost

    def booking(self, booking_id, booking_date, num_weeks, property_owner_name, contact_number, address, rooms, rooms_cost, garden_area, garden_area_cost):
        self.__booking_id = booking_id
        self.__booking_date = booking_date
        self.__num_weeks = int(num_weeks)
        self.__property_owner_name = property_owner_name
        self.__contact_number = contact_number
        self.__address = address
        self.__rooms = int(rooms)
        self.__rooms_cost = int(rooms_cost)
        self.__garden_area = int(garden_area)
        self.__garden_area_cost = int(garden_area_cost)
    
    def set_booking_id(self, booking_id):
        self.__booking_id = booking_id
    def get_booking_id(self):
        return self.__booking_id

    def set_booking_date(self, booking_date):
        self.__booking_date = booking_date
    def get_booking_date(self):
        return self.__booking_date
    
    def set_num_weeks(self, num_weeks):
        self.__num_weeks = num_weeks
    def get_num_weeks(self):
        return self.__num_weeks
    
    def set_property_owner_name(self, property_owner_name):
        self.__property_owner_name = property_owner_name
    def get_property_owner_name(self):
        return self.__property_owner_name
    
    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number
    def get_contact_number(self):
        return self.__contact_number

    def set_address(self, address):
        self.__address = address
    def get_address(self):
        return self.__address
    
    def set_rooms(self, rooms):
        self.__rooms = rooms
    def get_rooms(self):
        return self.__rooms
    
    def set_rooms_cost(self, rooms_cost):
        self.__rooms_cost = rooms_cost
    def get_rooms_cost(self):
        return self.__rooms_cost
    
    def set_garden_area(self, garden_area):
        self.__garden_area = garden_area
    def get_garden_area(self):
        return self.__garden_area
    
    def set_garden_area_cost(self, garden_area_cost):
        self.__garden_area_cost = garden_area_cost
    def get_garden_area_cost(self):
       return self.__garden_area_cost
    
    def __str__(self):
        return f'{self.__booking_id} {self.__booking_date} {self.__num_weeks} {self.__property_owner_name} {self.__contact_number} {self.__address} {self.__rooms} {self.__rooms_cost} {self.__garden_area} {self.__garden_area_cost}'

class luxury(booking):
    __security_alarm_check = False
    __pool_maintenance = False
    __luxury_cost = 0

    def __init__(self, booking_id = '', booking_date = '', num_weeks = 0, property_owner_name = '', contact_number = '', address = '', rooms = 0, rooms_cost = 0, garden_area = 0, garden_area_cost = 0, security_alarm_check = False, pool_maintenance = False, luxury_cost = 0):
        super().__init__(booking_id, booking_date, num_weeks, property_owner_name, contact_number, address, rooms, rooms_cost, garden_area, garden_area_cost)
        self.__security_alarm_check = security_alarm_check
        self.__pool_maintenance = pool_maintenance
        self.__luxury_cost = luxury_cost
    
    def set_security_alarm_check(self, security_alarm_check):
        self.__security_alarm_check = security_alarm_check
        if(security_alarm_check == True):
            self.__luxury_cost += 50

    def get_security_alarm_check(self):
        return self.__security_alarm_check

    def set_pool_maintenance(self, pool_maintenance):
        self.__pool_maintenance = pool_maintenance
        if(pool_maintenance == True):
           self.__luxury_cost += 50

    def get_pool_maintenance(self):
        return self.__pool_maintenance

    def get_luxury_cost(self):
        return self.__luxury_cost

    def __str__(self):
        return f'{self.__security_alarm_check} {self.__pool_maintenance} {self.__luxury_cost}'
