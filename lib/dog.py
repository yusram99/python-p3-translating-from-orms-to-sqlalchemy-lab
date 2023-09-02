from models import Dog

def create_table(base):
    # Create the Dog table
    base.metadata.create_all()

def save(session, dog):
    # Save a dog to the database
    session.add(dog)
    session.commit()

def get_all(session):
    # Retrieve all dogs from the database
    return session.query(Dog).all()

def find_by_name(session, name):
    # Find a dog by name
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    # Find a dog by ID
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    # Find a dog by name and breed
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    # Update the breed of a dog
    dog.breed = breed
    session.commit()