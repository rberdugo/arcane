from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from yourapplication.database import Base
from yourapplication.database import db_session


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    lastName = Column(String(50), unique=False)
    firstName = Column(String(50), unique=False)
    birthdate = Column(String(10),unique=False)
    __table_args__ = (UniqueConstraint('lastName', 'firstName', 'birthdate', name='uix_1'),
                     )
    def __init__(self, lastName=None, firstName=None, birthdate=None):
        self.lastName = lastName
        self.firstName = firstName
        self.birthdate = birthdate

    def __repr__(self):
        return '<User %r %r %r %r>' % (self.lastName, self.firstName, self.birthdate, self.id)

class Goods(Base):
    __tablename__ = 'goods'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=False)
    user_lastName = Column(String(50), unique=False)
    user_firstName = Column(String(50), unique=False)
    productName = Column(String(50), unique=False)
    description = Column(String(2000), unique=False)
    city = Column(String(50),unique=False)
    numberOf_Rooms = Column(Integer, unique=False)
    roomFeature = Column(String(2000), unique=False)
    address = Column(String(200), unique=False)
    UniqueConstraint(user_id, city, productName, address, name='uix_2')
    __table_args__ = (UniqueConstraint('user_id', 'city', 'productName','address',
                    name='uix_2'),)
    def __init__(self, user_id=None, user_lastName= None, user_firstName = None, productName=None,
            description=None,city=None, address=None, numberOf_Rooms=None, roomFeature=None):
        self.user_id = user_id
        self.user_lastName = user_lastName
        self.user_firstName = user_firstName
        self.productName = productName
        self.description = description
        self.city = city
        self.numberOf_Rooms = numberOf_Rooms
        self.roomFeature = roomFeature
        self.address = address

    def __repr__(self):
        return '<User number %r  who is named %r %r has added an %r in %r with %r rooms>' % (self.user_id, self.user_lastName,
                    self.user_firstName ,
                    self.productName,
                    self.city,
                    self.numberOf_Rooms)
