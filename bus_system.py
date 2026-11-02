from bus import Bus
from passenger import Passenger

class BusSystem:

    def __init__(self):
        self.buses = []
        self.passengers = []


    def add_bus(self, number,route,seats):
        for bus in self.buses:
            if bus.number == number:
                print("\nBus already exists!")
                return
        if seats <= 0:
            print("Invalid seat number!")
            return
        
        new_bus = Bus(number,route,seats)

        self.buses.append(new_bus)

    def book_ticket(self, bus_number, name, phone):

        for bus in self.buses:
            if bus.number == bus_number:
                if bus.available_seats() > 0:

                    print("Ticket prize is : 500 taka")
                    prize = int(input("Pay Your prize : "))
                    if prize < 500:
                        print("\nSorry, below 500 taka we can't accept")
                    else:
                        if bus.book_seat():
                            if prize > 500:
                                calculate = prize - 500
                                print(f"Here's your extra: {calculate}")
                            passenger  = Passenger(name,phone,bus)
                            self.passengers.append(passenger)

                            print("\nThank you! Your ticket is booked")
                else:
                    print("\nNo Seats available on this bus")
                return
            
        print("\nBus Not Found")        
                    
    def show_buses(self):
        if len(self.buses) == 0:
            print("No Buses available")
        else:
            for bus in self.buses:
                print(f"\nBus Number : {bus.number}, Available Seats : {bus.available_seats()}, Total seats : {bus.total_seats}, Bus Route : {bus.route}\n")
