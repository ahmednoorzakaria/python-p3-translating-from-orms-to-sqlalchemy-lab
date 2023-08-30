from models import Dog
from sqlalchemy import create_engine

def create_table(base,engine):

    if __name__ == "__main__" :
        engine = create_engine("sqlite:///dogs.db")
        base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    

def get_all(session):
   return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()
    pass

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

    pass

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name , breed=breed).first()
    pass

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    pass