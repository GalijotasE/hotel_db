from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

engine = create_engine('sqlite:///front_of_house.db')
Base = declarative_base()

class Hotel_Guest(Base):
    __tablename__ = "hotel_guest"
    id = Column(Integer, primary_key = True)
    guest_f_name = Column("first_name", String)
    guest_l_name = Column("last_name", String)
    reason_of_stay = Column("reasons_of_stay", String)
    requests = Column("request_id", Integer, ForeignKey("requests.id"))
    complaints = Column("complaint_id", Integer, ForeignKey("complaints.id"))
    loyalty = Column("loyalty_level", String, ForeignKey("loyalty.name"))
    booking_id = Column("booking_id", Integer, ForeignKey("booking_details.id"))
    room_id = Column("room_id", Integer, ForeignKey("hotel_room.id"))


class Requests(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key = True)
    request = Column("request", String)
    guest_id = Column("guest_id", Integer, ForeignKey("hotel_guest.id"))
    room_id = Column("room_id", Integer, ForeignKey("hotel_room.id"))


class Complaints(Base):
    __tablename__ = "complaints"
    id = Column(Integer, primary_key = True)
    complaint = Column("complaint", String)
    guest_id = Column("guest_id", Integer, ForeignKey("hotel_guest.id"))
    room_id = Column("room_id", Integer, ForeignKey("hotel_room.id"))


class Loyalty(Base):
    __tablename__ = "loyalty"
    id = Column(Integer, primary_key = True)
    name = Column("name", String)
    

class Room_Type(Base):
    __tablename__ = "room_type"
    id = Column(Integer, primary_key = True)
    type_of_room = Column("type_of_room", String)
    room_description = Column("room_description", String)
    price_per_night = Column("price_per_night", Float)


class Hotel_Room(Base):
    __tablename__ = "hotel_room"
    id = Column(Integer, primary_key = True)
    room_type = Column("room_type_id", String, ForeignKey("room_type.id"))
    guest_id = Column("guest_id", Integer, ForeignKey("hotel_guest.id"))
    room_price = Column("room_price", Float, ForeignKey("room_type.price_per_night"))
    booking_id = Column("booking_id", Integer, ForeignKey("booking_details.id"))


class Employees(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key = True)
    e_f_name = Column("first_name", String)
    e_l_name = Column("last_name", String)
    address = Column("address", String)
    phone_no = Column("phone_number", String)
    email = Column("email", String)
    position = Column("position", String)


class Booking_details(Base):
    __tablename__ = "booking_details"
    id = Column(Integer, primary_key = True)
    check_in = Column("check_in", String)
    room_type = Column("room_type", Integer, ForeignKey("room_type.id"))
    guest_id = Column("guest_Id", Integer, ForeignKey("hotel_guest.id"))
    number_of_guests = Column("num_of_guests", Integer)
    nights = Column("nights", Integer)
    rate = Column("night_rate", Float, ForeignKey("room_type.price_per_night"))
    payment = Column("payment_method", String)
    total = Column("total_price", String)



Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)