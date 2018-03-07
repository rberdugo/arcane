from db_real_estate import *
from sqlalchemy import and_, create_engine
engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)

                "If you want to clean the table"
Users.__table__.drop(engine)
Goods.__table__.drop(engine)
#Then leave python and restart

                """Example of ADDING a user"""

lastName = 'Berdugo'
firstName = 'Raphael'
birthdate = '13.10.1991'
create_user(lastName, firstName, birthdate)
Users.query.all()

#TEST OF UNIQUECONTRAINT
lastName = 'Berdugo'
firstName = 'Raphael'
birthdate = '13.10.1991'
create_user(lastName, firstName, birthdate)
Users.query.all()

lastName = 'BerdugoT'
firstName = 'Raphael'
birthdate = '13.10.1991'
create_user(lastName, firstName, birthdate)
Users.query.all()

            """Example of User information MODIFICATION"""

lastName = 'Berdugo'
firstName = 'Raphael'
birthdate = '13.10.1991'

variable_to_modify = 'lastName' #could be firstName ou birthdate
new_value = 'BerdugoT'

condition = and_(Users.lastName==lastName, Users.firstName==firstName, Users.birthdate==birthdate)#based on UniqueConstraint
user_id = db_session.query(Users).filter(condition).all()[0].id
modify_user_info(variable_to_modify, new_value, user_id)
Users.query.all()
#Not working because Raphael BerdugoT already exists


lastName = 'Berdugo'
firstName = 'Raphael'
birthdate = '13.10.1991'

variable_to_modify = 'lastName' #could be firstName ou birthdate
new_value = 'Lefevre'

condition = and_(Users.lastName==lastName, Users.firstName==firstName, Users.birthdate==birthdate)#based on UniqueConstraint
user_id = db_session.query(Users).filter(condition).all()[0].id

Users.query.all() #BEFORE
modify_user_info(variable_to_modify, new_value, user_id)
Users.query.all() #AFTER

                """Example of ADDING Real Estate Good"""

user_id = 2 #Pick a number withing the range of ids
productName = "Appartment"
description = "Very nice apprtment with sea view"
city = "Neuilly"
address = "3 rue des Ternes"
numberOf_Rooms = "3"
roomFeature = "25 m2 on average"
add_real_estate_good(user_id, productName, description, city, address, numberOf_Rooms, roomFeature)
#try it a second time and it won't work due to the UniqueConstraint defined
Goods.query.all()

                    """Example of MODIFYING Real Estate Good"""
variable = 'city'
new_value = "Monaco"

user_id = 2 #or recover user_id using query with lastName, firsName, birthdate
city = "Neuilly"
address = "3 rue des Ternes"
productName = "Appartment"

condition = and_(Goods.user_id==user_id, Goods.city==city,
            Goods.productName==productName, Goods.address==address) #based on UniqueConstraint
good_id = db_session.query(Goods).filter(condition).all()[0].id

Goods.query.all() #BEFORE
modify_real_estate_goods(variable, new_value, good_id, user_id)
Goods.query.all() #AFTER

                """CAN ONLY MODIFY YOU OWN REAL ESTATE PROPERTIES"""
modify_real_estate_goods(variable, new_value, good_id, 3)


                """Consulting the Real Estate DB"""
#Can only view one city at a time
city = "Monaco"
consulting_real_estate_db(city)
