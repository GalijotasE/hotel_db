from hotel_database import Hotel_Guest, Hotel_Room, Room_Type, Booking, Payment, Transaction, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

#### VIEW DATA FROM THE DATABASE

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
    
#### ADD DATA TO THE DATABASE


# def edit_all_hotel_guest():
#     print("---Editor of Hotel Guests---")
#     try:
#        f_name = input("first name: ")
#        l_name = input("last name: ")
#        reasons = input("reasons of stay: ")
#        requests = input("requests: ")
#        payment_id = input("choose payment id")
       

while True:
    print("---HOTEL DATABASE EDITOR---")
    print("Please choose one of the following:")
    print("a - Add New Data To The Database")
    print("v - View Data In The Database")
    print("d - Delete Data In The Database")
    print("q - Quit")
    action = input("please choose: ").casefold()
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
            pass
        elif choice == "r":
            pass
        elif choice == "t":
            pass
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