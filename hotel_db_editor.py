from hotel_database import Hotel_Guest, Hotel_Room, Room_Type, Booking, Payment, Transaction, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

########## VIEW DATA FROM THE DATABASE

def show_all_hotel_guest():
    print("---List of Hotel Guests---")
    guests = session.query(Hotel_Guest).all()
    for guest in guests:
        print(guest)

def show_all_hotel_room():
    print("---List Of All Hotel Rooms---")
    rooms = session.query(Hotel_Room).all()
    for room in rooms:
        print(room)

def show_all_room_type():
    print("---List Of All Room Types---")
    room_types = session.query(Room_Type).all()
    for room_type in room_types:
        print(room_type)

def show_all_booking():
    print("---List Of All Bookings---")
    bookings = session.query(Booking).all()
    for booking in bookings:
        print(booking)

def show_all_payment():
    print("---List Of All Payments---")
    payments = session.query(Payment).all()
    for payment in payments:
        print(payment)

def show_all_transaction():
    print("---List Of All Transactions---")
    transactions = session.query(Transaction).all()
    for transaction in transactions:
        print(transaction)
    
########## ADD DATA TO THE DATABASE


def edit_all_hotel_guest():
    print("---Editor Of Hotel Guests---")
    try:
       f_name = input("first name: ")
       l_name = input("last name: ")
       reason = input("reason of stay: ")
       request = input("requests: ")
       print("Please choose payment id")
       show_all_payment()
       payment = input("payment id: ")
       loyalty_g = input("loyalty: ")
       print("Please choose room number")
       show_all_hotel_room()
       room_number = input("room number: ")
       print("Please choose booking")
       show_all_booking()
       booking = input("booking id: ")
    except ValueError:
        print("ERROR!!!")
    else:
        new_guest = Hotel_Guest(
            guest_f_name= f_name,
            guest_l_name= l_name,
            reason_of_stay= reason,
            requests= request,
            payment_id= payment,
            loyalty= loyalty_g,
            room_no= room_number,
            booking_id= booking
        )
        session.add(new_guest)
        session.commit()
        print(f"New Guest {f_name} has been added to the database.")


def edit_all_hotel_room():
    print("---Editor Of Hotel Rooms---")
    try:
        print("Choose Room Type Id")
        show_all_room_type()
        type_of_room = input("Room Type Id: ")
        print("Choose Guest Id")
        show_all_hotel_guest()
        g_id = input("Guest Id: ")
        print("Choose Nightly Rate")
        show_all_room_type()
        night_rate = input("Nightly rate: ")
        print("Choose Booking Id")
        show_all_booking()
        booking = input("Booking Id: ")
    except ValueError:
        print("ERROR!!!")
    else:
        new_room = Hotel_Room(
            room_type= type_of_room,
            guest_id= g_id,
            nightly_rate= night_rate,
            booking_id= booking
        )
        session.add(new_room)
        session.commit()
        print(f"New room {type_of_room} has been added to the database.")


def edit_all_room_type():
    print("---Editor Of Hotel Room Types---")
    try:
        room_type = input("Type Of Room: ")
        night_rate = input("Night Rate: ")
    except ValueError:
        print("ERROR!!!")
    else:
        new_type = Room_Type(
            type_of_room= room_type,
            nightly_rate= night_rate
        )
        session.add(new_type)
        session.commit()
        print(f"New room type {room_type} has been added to the database")


def edit_all_booking():
    print("---Editor Of Hotel Bookings---")
    try:
        print("Choose guest id")
        show_all_hotel_guest()
        guest = input("Guest id: ")
        print("Choose payment id")
        show_all_payment()
        payment = input("Payment id: ")
        print("Choose room number:")
        show_all_hotel_room()
        rooms = input("Room number: ")
        c_in = input("Check in: ")
        c_out = input("Check out: ")
        no_of_guests = input("Number Of Guests: ")
        print("Choose nightly rate")
        show_all_room_type()
        night_rate = input("Nightly rate: ")
        night = input("Nights: ")
        total = input("Total: ")
    except ValueError:
        print("ERROR!!!")
    else:
        new_booking = Booking(
            guest_id= guest,
            payment_id= payment,
            room_no= rooms,
            check_in= c_in,
            check_out= c_out,
            number_of_guests= no_of_guests,
            nightly_rate= night_rate,
            nights= night,
            total= total
        )
        session.add(new_booking)
        session.commit()
        print(f"New booking for {guest} has been added to the database.")


########## Infinite menu cycle

while True:
    print("---HOTEL DATABASE EDITOR---")
    print("Please choose one of the following:")
    print("a - Add New Data To The Database")
    print("v - View Data In The Database")
    print("d - Delete Data In The Database")
    print("q - Quit")
    action = input("please choose: ").casefold()

    #### adding data cycle
    if action == "a":
        print("---Adding Data To The Database---")
        print("g - Add New Hotel Guest")
        print("r - Add New Hotel Room")
        print("t - Add New Hotel Room Type")
        print("b - Add New Booking")
        print("p - Add New Payment")
        print("t - Add New Transaction")
        print("q - Quit")
        choice = input("please choose: ").casefold()
        if choice == "g":
            edit_all_hotel_guest()
        elif choice == "r":
            edit_all_hotel_room()
        elif choice == "t":
            edit_all_room_type()
        elif choice == "b":
            pass
        elif choice == "p":
            pass
        elif choice == "t":
            pass
        elif choice == "q":
            break
        else:
            print("ERROR!!! Please Choose Only From Given Inputs!!!")
            
    #### Viewing data cycle
    elif action == "v":
        print("---Viewing Data From The Database---")
        print("g - View New Hotel Guest")
        print("r - View New Hotel Room")
        print("t - View New Hotel Room Type")
        print("b - View New Booking")
        print("p - View New Payment")
        print("t - View New Transaction")
        print("q - Quit")
        choice = input("Please Choose: ").casefold()
        if choice == "g":
            show_all_hotel_guest()
        elif choice == "r":
            show_all_hotel_room()
        elif choice == "t":
            show_all_room_type()
        elif choice == "b":
            show_all_booking()
        elif choice == "p":
            show_all_payment()
        elif choice == "t":
            show_all_transaction()
        elif choice == "q":
            break
        else:
            print("ERROR!!! Please Choose Only From Given Inputs!!!")