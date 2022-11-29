from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, date

engine = create_engine('sqlite:///front_of_house.db')
Base = declarative_base()

class Hotel_Guest(Base):
    __tablename__ = "main_guest"
    id = Column(Integer, primary_key = True)
    guest_f_name = Column("first_name", String)
    guest_l_name = Column("last_name", String)
    reason_of_stay = Column("reasons_of_stay", String)
    requests = Column("request_id", Integer)
    loyalty = Column("loyalty_level", String) # ar griztantis svecias

    def __init__(self, guest_f_name, guest_l_name, reason_of_stay, requests, loyalty):
        self.guest_f_name = guest_f_name
        self.guest_l_name = guest_l_name
        self.reason_of_stay = reason_of_stay
        self.requests = requests
        self.loyalty = loyalty

    def __repr__(self):
        return f"({self.id}, {self.guest_f_name}, {self.guest_l_name}, {self.reason_of_stay}, {self.requests}, {self.loyalty})"


class Hotel_Room(Base):
    __tablename__ = "hotel_room"
    room_no = Column(Integer, primary_key = True)
    room_type = Column("room_type_id", String, ForeignKey("room_type.type_of_room"))
    guest_id = Column("guest_id", Integer, ForeignKey("main_guest.id"))

    def __init__(self, room_type, guest_id):
        self.room_type = room_type
        self.guest_id = guest_id
    
    def __repr__(self):
        return f"({self.room_no}, {self.room_type}, {self.guest_id})"


class Room_Type(Base):
    __tablename__ = "room_type"
    id = Column(Integer, primary_key = True)
    type_of_room = Column("type_of_room", String)
    nightly_rate = Column("nightly_rate", Float)

    def __init__(self, type_of_room, nightly_rate):
        self.type_of_room = type_of_room
        self.nightly_rate = nightly_rate

    def __repr__(self):
        return f"({self.id}, {self.type_of_room}, {self.nightly_rate})"


class Booking(Base):
    __tablename__ = "booking"
    id = Column(Integer, primary_key = True)
    guest_id = Column("guest_Id", Integer, ForeignKey("main_guest.id"))
    room_no = Column("room_no", Integer, ForeignKey("hotel_room.room_no"))
    check_in = Column("check_in", String)
    check_out = Column("check_out", String)
    nights = Column("nights", Integer)

    def __init__(self, guest_id, room_no, check_in, check_out, nights):
        self.guest_id = guest_id
        self.room_no = room_no
        self.check_in = check_in
        self.check_out = check_out
        self.nights = nights

    def __repr__(self):
        return f"({self.id}, {self.guest_id}, {self.room_no}, {self.check_in}, {self.check_out}, {self.nights})"


class Payment(Base):
    __tablename__ = "payment"
    id = Column(Integer, primary_key = True)
    guest_id = Column("guest_id", Integer, ForeignKey("main_guest.id"))
    payment_method = Column("payment_method", String)
    booking_id = Column("booking_id", Integer, ForeignKey("booking.id"))
    total = Column("total", Float)

    def __init__(self, guest_id, payment_method, booking_id, total):
        self.guest_id = guest_id
        self.payment_method = payment_method
        self.booking_id = booking_id
        self.total = total

    def __repr__(self):
        return f"({self.id}, {self.guest_id}, {self.payment_method}, {self.booking_id}, {self.total})"


#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)