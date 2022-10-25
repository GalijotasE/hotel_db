from hotel_database import Hotel_Guest, Hotel_Room, Room_Type, Booking, Payment, Transaction, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


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
    



# def edit_all_hotel_guest():
#     print("---Editor of Hotel Guests---")
#     try:
#        f_name = input("first name: ")
#        l_name = input("last name: ")
#        reasons = input("reasons of stay: ")
#        requests = input("requests: ")
#        payment_id = input("choose payment id")
       

