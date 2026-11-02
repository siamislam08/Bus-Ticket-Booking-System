from bus_system import BusSystem
from admin import Admin

system = BusSystem()

system.add_bus("101","Dhaka to Mymenshing", 5)

while(True):
    print("+------------------------+")
    print("| 1. Admin Login         |")
    print("| 2. Book Ticket         |")
    print("| 3. View Buses          |")
    print("| 4. Exit                |")
    print("+------------------------+")

    try:
        option = int(input("Enter Your Option: "))
    except ValueError:
        print("\nplease enter a valid number\n")
        continue

    if option == 1:
        username = input("Enter your username : ")
        pas = input("Enter your password : ")
        ad = Admin(username, pas)
        if ad.login():
            
            while(True):
                print("+-------------------------+")
                print("| 1. Add Bus             |")
                print("| 2. View All Buses      |")
                print("| 3. View All Passenger  |")
                print("| 4. Logout              |")
                print("+-------------------------+")
                try:
                    option2 = int(input("Choose your option : "))
                except ValueError:
                    print("Please enter a valid number")
                    continue
                if option2 == 1:
                    
                    bus_number = input("Enter Bus Number : ")
                    bus_route = input("Enter Bus Route : ")
                    bus_seats = int(input("How many seats have : "))

                    # bus = Bus(bus_number, bus_route,bus_seats)
                    
                    system.add_bus(bus_number, bus_route, bus_seats)

                    # print("add buses")
                elif option2 == 2:
                    # for bus in system.buses:
                    #     print(f"\nBus Number : {bus.number}, Available Seats : {bus.available_seats()}, Total seats : {bus.total_seats}, Bus Route : {bus.route}\n")
                    system.show_buses()
                    # print("view busese")

                elif option2 == 3:
                    if len(system.passengers) == 0:
                        print("\n No passenger found!")
                    else:
                        for passenger in system.passengers:
                            print(f"\nPassenger Name : {passenger.name}, Passenger Phone : {passenger.phone}, Passenger bus number : {passenger.bus.number}, passenger route : {passenger.bus.route}")
                elif option2 == 4:
                    break
        else:
            print("\nYour Crediential is incorrect!")
            continue
    elif option == 2:
        bus_number = input("Enter Bus number : ")
        user_name = input("Enter Your name : ")
        user_phone = input("Enter Your Number : ")

        system.book_ticket(bus_number,user_name,user_phone)

        # print("booking ticket")
    elif option == 3:

        system.show_buses()

        # print("view bus")

    elif option == 4:
        break


