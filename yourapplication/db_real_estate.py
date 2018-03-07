from yourapplication.database import init_db
from yourapplication.database import db_session
from yourapplication.real_estate import Users, Goods
import sqlalchemy
from sqlalchemy import update
init_db()

"Check the state of the DB"
Users.query.all()


def create_user(lastName, firstName, birthdate):
    try :
        u = Users(lastName, firstName, birthdate)
        db_session.add(u)
        db_session.commit()
        print('Your identification number is ', db_session.query(Users).count(), '. Remember it!')
    except :
        print('error except rollback')
        db_session.rollback()

def modify_user_info(variable, new_value, id_value):
    "variable = lastName or variable = firsName or variable = birthdate"
    try :
        if variable =='lastName':
            db_session.execute(update(Users).where(Users.id == id_value).values({Users.lastName: new_value}))
            db_session.commit()
        elif variable =='firstName':
            db_session.execute(update(Users).where(Users.id == id_value).values({Users.firstName: new_value}))
            db_session.commit()
        elif variable=='birthdate':
            db_session.execute(update(Users).where(Users.id == id_value).values({Users.birthdate: new_value}))
            db_session.commit()
    except :
        print('error except rollback')
        db_session.rollback()

def add_real_estate_good(user_id, productName, description, city, address, numberOf_Rooms, roomFeature):
    try :
        qry = db_session.query(Users).filter(Users.id==user_id).all()[0]
        user_lastName = qry.lastName
        user_firstName = qry.firstName
        u = Goods(user_id, user_lastName, user_firstName, productName,
                description,city, address, numberOf_Rooms, roomFeature)
        db_session.add(u)
        db_session.commit()
        print('Product identification number is ', db_session.query(Goods).count(), '. Remember it!')
    except :
        print('error except rollback')
        db_session.rollback()

def modify_real_estate_goods(variable, new_value, good_id, user_id):
    good_user_id = db_session.query(Goods).filter(Goods.id == good_id).all()[0].user_id
    if good_user_id == user_id :
        try :
            if variable =='productName':
                db_session.execute(update(Goods).where(Goods.id == good_id).values({Goods.productName: new_value}))
                db_session.commit()
            elif variable =='description':
                db_session.execute(update(Goods).where(Goods.id == good_id).values({Goods.description: new_value}))
                db_session.commit()
            elif variable=='city':
                db_session.execute(update(Goods).where(Goods.id == good_id).values({Goods.city: new_value}))
                db_session.commit()
            elif variable =='address':
                db_session.execute(update(Goods).where(Goods.id == good_id).values({Goods.address: new_value}))
                db_session.commit()
            elif variable =='numberOf_Rooms':
                db_session.execute(update(Goods).where(Goods.id == good_id).values({Goods.numberOf_Rooms: new_value}))
                db_session.commit()
            elif variable=='roomFeature':
                db_session.execute(update(Goods).where(Goods.id == good_id).values({Goods.roomFeature: new_value}))
                db_session.commit()
        except :
            print('error except rollback')
            db_session.rollback()
    else :
        print('You are not allowed to edit this real estate good!!')

def consulting_real_estate_db(city):
    print(db_session.query(Goods).filter(Goods.city == city).all())

#Create a condition that you cannot create two similars individual with same name, same birthdate
