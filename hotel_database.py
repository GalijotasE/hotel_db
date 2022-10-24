from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///front_of_house.db')
Base = declarative_base()

class Hotel_Guest(Base):
    __tablename__ = "hotel_guest"
    id = Column(Integer, primary_key = True)
    guest_f_name = Column("first_name", String)
    guest_l_name = Column("last_name", String)
    reason_of_stay = Column("reasons_of_stay", String)
    requests = Column("requests", String)
    complaints = Column("complaints", String)
    payment = Column("payment_method", String)
    loyalty = Column("loyalty_level", String)
    length = Column("length_of_stay", String)
    check_in = Column("check_in", String)
    check_out = Column("check_out", String)
    room_id = Column("room_id", Integer, ForeignKey("hotel_room.id"))



class Hotel_Room(Base):
    __tablename__ = "hotel_room"
    id = Column(Integer, primary_key = True)
    guest_id = Column("guest_id", Integer, ForeignKey("hotel_guest.id"))
    room_price = Column("room_price", Float)
    check_in = Column("check_in", String, ForeignKey("hotel_guest.check_in"))
    check_out = Column("check_out", String, ForeignKey("hotel_guest.check_out"))



class Employees(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key = True)
    e_f_name = Column("first_name", String)
    e_l_name = Column("last_name", String)
    address = Column("address", String)
    phone_no = Column("phone_number", String)
    email = Column("email", String)
    position = Column("position", String)



class Room_Service(Base):
    __tablename__ = "room_service"




Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)