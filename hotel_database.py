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
    payment_id = Column("payment_id", Integer)
    loyalty = Column("loyalty_level", String) # ar griztantis svecias
    room_no = Column("room_no", Integer, ForeignKey("hotel_room.room_no"))
    booking_id = Column("booking_id", Integer)


class Hotel_Room(Base):
    __tablename__ = "hotel_room"
    room_no = Column(Integer, primary_key = True)
    room_type = Column("room_type_id", String, ForeignKey("room_type.type_of_room"))
    guest_id = Column("guest_id", Integer, ForeignKey("main_guest.id"))
    nightly_rate = Column("nightly_rate", Float, ForeignKey("room_type.nightly_rate"))
    booking_id = Column("booking_id", Integer, ForeignKey("booking.id"))


class Room_Type(Base):
    __tablename__ = "room_type"
    id = Column(Integer, primary_key = True)
    type_of_room = Column("type_of_room", String)
    nightly_rate = Column("nightly_rate", Float)


class Booking(Base):
    __tablename__ = "booking"
    id = Column(Integer, primary_key = True)
    guest_id = Column("guest_Id", Integer, ForeignKey("main_guest.id"))
    payment_id = Column("payment_id", Integer, ForeignKey("payment.id"))
    room_no = Column("room_no", Integer, ForeignKey("hotel_room.room_no"))
    check_in = Column("check_in", String)
    check_out = Column("check_out", String)
    number_of_guests = Column("num_of_guests", Integer)
    nightly_rate = Column("nightly_rate", Float, ForeignKey("room_type.nightly_rate"))
    nights = Column("nights", Integer)
    total = Column("total_price", Float)


class Payment(Base):
    __tablename__ = "payment"
    id = Column(Integer, primary_key = True)
    guest_id = Column("guest_id", Integer, ForeignKey("main_guest.id"))
    payment_method = Column("payment_method", String)
    booking_id = Column("booking_id", Integer, ForeignKey("booking.id"))
    nightly_rate = Column("nightly_rate", Float, ForeignKey("room_type.nightly_rate"))
    total = Column("total", Float)


class Transaction(Base):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key = True)
    guest_id = Column("guest_id", Integer, ForeignKey("main_guest.id"))
    payment_method = Column("payment_method", String, ForeignKey("payment.payment_method"))
    total = Column("total", Float, ForeignKey("payment.total"))
    acc_no = Column("acc_no", String)
    payment_status = Column("payment_status", String)



Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)