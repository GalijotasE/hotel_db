from hotel_database import Hotel_Guest, Hotel_Room, Room_Type, Booking, Payment, engine
from sqlalchemy.orm import sessionmaker
import sqlite3

Session = sessionmaker(bind=engine)
session = Session()

conn = sqlite3.connect('front_of_house.db')
cursor = conn.cursor()

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
    
########## ADD DATA TO THE DATABASE


def edit_all_hotel_guest():
    print("---Editor Of Hotel Guests---")
    try:
       f_name = input("first name: ")
       l_name = input("last name: ")
       reason = input("reason of stay: ")
       request = input("requests: ")
       loyalty_g = input("loyalty: ")
    except ValueError:
        print("ERROR!!!")
    else:
        new_guest = Hotel_Guest(
            guest_f_name= f_name,
            guest_l_name= l_name,
            reason_of_stay= reason,
            requests= request,
            loyalty= loyalty_g,
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

    except ValueError:
        print("ERROR!!!")
    else:
        new_room = Hotel_Room(
            room_type= type_of_room,
            guest_id= g_id
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
        print("Choose room number:")
        show_all_hotel_room()
        rooms = input("Room number: ")
        c_in = input("Check in: ")
        c_out = input("Check out: ")
        night = input("Nights: ")
    except ValueError:
        print("ERROR!!!")
    else:
        new_booking = Booking(
            guest_id= guest,
            room_no= rooms,
            check_in= c_in,
            check_out= c_out,
            nights= night,
        )
        session.add(new_booking)
        session.commit()
        print(f"New booking for {guest} has been added to the database.")


def edit_all_payment():
    try:
        print("Choose guest id: ")
        show_all_hotel_guest()
        guest = input("Guest id: ")
        payment = input("Payment method: ")
        print("Choose booking id:")
        show_all_booking()
        booking = input("Booking id: ")
    except ValueError:
        print("ERROR!!!")
    else:
        new_payment = Payment(
            guest_id= guest,
            payment_method= payment,
            booking_id= booking,
        )
        session.add(new_payment)
        session.commit()
        print(f"Payment from {guest} has been added to the database.")


########## DELETE DATA FROM DATABASE

# def guest_data_choice():
#     show_all_hotel_guest()
#     try:
#         guest_id = int(input("Guest id: "))
#     except ValueError:
#         print("ERROR!!! Input is supposed to be integer!!!")
#         return None
#     else:
#         if guest_id:
#             guest = session.query(Hotel_Guest).get(id)
#             if guest:
#                 return guest
#             else:
#                 print(f"ERROR!!! Guest with an id {id} does not exist!")


# def delete_hotel_guest():
#     deleting = guest_data_choice()
#     if deleting:
#         session.delete(deleting)
#         session.commit()
#         print(f"Guest {deleting} has been deleted.")
#     else:
#         print(f"ERROR!!! Guest {deleting} does not exist.")



########## INFINITE MENU CYCLE

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
        print("q - Quit")
        choice = input("please choose: ").casefold()
        if choice == "g":
            edit_all_hotel_guest()
        elif choice == "r":
            edit_all_hotel_room()
        elif choice == "t":
            edit_all_room_type()
        elif choice == "b":
            edit_all_booking()
        elif choice == "p":
            edit_all_payment()
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
        elif choice == "q":
            break
        else:
            print("ERROR!!! Please Choose Only From Given Inputs!!!")

    #### Deleting data cycle
    elif action == "d":
        print("---Deleting Data From The Database---")
        print("g - Delete Hotel Guest")
        print("r - Delete Hotel Room")
        print("t - Delete Hotel Room Type")
        print("b - Delete Booking")
        print("p - Delete Payment")
        print("q - Quit")
        choice = input("Please Choose: ")
        if choice == "g":
            #delete_hotel_guest()
            pass
        elif choice == "r":
            pass
        elif choice == "t":
            pass
        elif choice == "b":
            pass
        elif choice == "p":
            pass
        elif choice == "q":
            break

    #### Quit
    elif action == "q":
        break
    else:
        print("ERROR!!! Please Choose Only From Given Inputs!!!")