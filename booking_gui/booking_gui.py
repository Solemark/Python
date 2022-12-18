import booking
from tkinter import Tk, Label, Entry, StringVar, Button, Checkbutton, BooleanVar

def booking_gui():
    booking_id = ''
    booking_date = ''
    num_weeks = 0
    property_owner_name = ''
    contact_number = ''
    address = ''
    rooms = 0
    rooms_cost = 0
    garden_area = 0
    garden_area_cost = 0
    total_price = 0
    display_all = ''
    security_alarm_check = False
    pool_maintenance = False
    booking_list = []

    def clear():
        booking_id.set('')
        booking_date.set('')
        num_weeks.set('')
        property_owner_name.set('')
        contact_number.set('')
        address.set('')
        rooms.set('')
        garden_area.set('')
        security_alarm_check.set(False)
        pool_maintenance.set(False)
    
    def calculation():
        price = 0
        price += int(rooms.get())*5
        price += int(garden_area.get())*2
        price += price*int(num_weeks.get())
        rooms_cost.set(int(rooms.get())*5)
        garden_area_cost.set(int(garden_area.get())*2)

        if(security_alarm_check.get() == True):
            price += 50
        if(pool_maintenance.get() == True):
            price += 50
        total_price.set(price)

    def submit():
        calculation()
        b = booking.luxury(booking_id.get(), booking_date.get(), num_weeks.get(), property_owner_name.get(), contact_number.get(), address.get(), rooms.get(), rooms_cost.get(), garden_area.get(), garden_area_cost.get())
        b.set_security_alarm_check(security_alarm_check.get())
        b.set_pool_maintenance(pool_maintenance.get())
        booking_list.append(b)
        clear()
    
    def display():
        text = ''
        for x in booking_list:
            text += 'id: ' + x.get_booking_id() + ' date: ' + x.get_booking_date() + ' nweeks: ' + str(x.get_num_weeks()) + ' owner: ' + x.get_property_owner_name() + ' number: ' + x.get_contact_number() + ' address: ' + x.get_address() + ' rooms: ' + str(x.get_rooms()) + ' room cost: ' + str(x.get_rooms_cost()) + ' garden area: ' + str(x.get_garden_area()) + ' garden area cost: ' + str(x.get_garden_area_cost()) + ' sec check: ' + str(x.get_security_alarm_check()) + ' pool check: ' + str(x.get_pool_maintenance()) + ' lux cost: ' + str(x.get_luxury_cost()) + '\n'  
        display_all.set(text)

    root = Tk()
    root.title('NQ-RE Services Calculator')
    booking_id = StringVar()
    booking_date = StringVar()
    num_weeks = StringVar()
    property_owner_name = StringVar()
    contact_number = StringVar()
    address = StringVar()
    rooms = StringVar()
    rooms_cost = StringVar()
    garden_area = StringVar()
    garden_area_cost = StringVar()
    total_price = StringVar()
    display_all = StringVar()
    security_alarm_check = BooleanVar()
    pool_maintenance = BooleanVar()

    Label(root, text='Please enter your booking details').grid(row=0, columnspan=2)
    Label(root, text='BookingId: ').grid(row=1, column=0)
    Entry(root, textvariable=booking_id).grid(row=1, column=1)
    Label(root, text='Booking Date: ').grid(row=2, column=0)
    Entry(root, textvariable=booking_date).grid(row=2, column=1)
    Label(root, text='Weeks: ').grid(row=3, column=0)
    Entry(root, textvariable=num_weeks).grid(row=3, column=1)
    Label(root, text='Owner Name: ').grid(row=4, column=0)
    Entry(root, textvariable=property_owner_name).grid(row=4, column=1)
    Label(root, text='Contact Number: ').grid(row=5, column=0)
    Entry(root, textvariable=contact_number).grid(row=5, column=1)
    Label(root, text='Address: ').grid(row=6, column=0)
    Entry(root, textvariable=address).grid(row=6, column=1)
    Label(root, text='Rooms: ').grid(row=7, column=0)
    Entry(root, textvariable=rooms).grid(row=7, column=1)
    Label(root, text='Garden Area: ').grid(row=8, column=0)
    Entry(root, textvariable=garden_area).grid(row=8, column=1)
    Button(root, text='Submit', command=submit).grid(row=9, column=0, columnspan=1)
    Button(root, text='Clear', command=clear).grid(row=9, column=1, columnspan=1)
    Button(root, text='Display', command=display).grid(row=9, column=1, columnspan=1)
    Checkbutton(root, text='Security Check', variable=security_alarm_check, onvalue=True, offvalue=False).grid(row=10, column=0, columnspan=1)
    Checkbutton(root, text='Pool Maintenance', variable=pool_maintenance, onvalue=True, offvalue=False).grid(row=10, column=1, columnspan=1)
    Label(root, text='Rooms Cost: ').grid(row=11, column=0, columnspan=1)
    Label(root, textvariable=rooms_cost).grid(row=11, column=1, columnspan=1)
    Label(root, text='Garden Area Cost: ').grid(row=12, column=0, columnspan=1)
    Label(root, textvariable=garden_area_cost).grid(row=12, column=1, columnspan=1)
    Label(root, text='Total Price: ').grid(row=13, column=0, columnspan=1)
    Label(root, textvariable=total_price).grid(row=13, column=1, columnspan=1)
    Label(root, textvariable=display_all).grid(row=14, columnspan=2)
    root.mainloop()
booking_gui()