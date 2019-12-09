from app import db


acc_assc = db.Table('acc_assc',
                                db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                                db.Column('service_id', db.Integer, db.ForeignKey('services.id')),
                                db.Column('veterinarian_id', db.Integer, db.ForeignKey('veterinarians.id')),
                                db.Column('pet_id', db.Integer, db.ForeignKey('pets.id'))

                    )

class User(db.Model):
    __tablename__ = "users"
    #properties
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String)

    #relations
    veterinarians = db.relationship("Veterinarian",
                                    secondary=acc_assc,
                                    backref=db.backref('users',lazy='dynamic'))
    pets = db.relationship("Pet",
                            secondary=acc_assc,
                            backref=db.backref('users',lazy='dynamic'))

    services = db.relationship("Service",
                                secondary=acc_assc,
                                backref=db.backref('users',lazy='dynamic'))


    def __init__(self,name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User {}>".format(self.name)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

class Veterinarian(db.Model):
    __tablename__ = "veterinarians"
    #properties
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.Integer)

    #relations
    services = db.relationship("Service",
                                secondary=acc_assc,
                                backref=db.backref('veterinarians',lazy='dynamic'))
    def __eq__(self,a):
        return a.email == self.email

    def __repr__(self):
        return "<Veterinary {}>".format(self.name)

class Pet(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key = True)
    #properties
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    race = db.Column(db.String(255))
    gender = db.Column(db.Integer)
    owner_name = db.Column(db.String(255))

    #relations
    services = db.relationship("Service",
                                secondary=acc_assc,
                                backref=db.backref('pets',lazy='dynamic'))
    def __eq__(self,a):
        return a.name == self.name and \
        a.age == self.age and \
        a.race == self.race and \
        a.gender == self.gender and \
        a.owner_name == self.owner_name

    def __repr__(self):
        return "<Pet {}>".format(self.name)


class Service(db.Model):
    __tablename__ = "services"
    id = db.Column(db.Integer, primary_key = True)
    veterinarian_name = db.Column(db.String(255))
    pet_name = db.Column(db.String(255))
    price = db.Column(db.Float)
    date = db.Column(db.DateTime)
    description = db.Column(db.String(255))

    def __eq__(self,a):
        return self.veterinarian_name == a.veterinarian_name and \
                self.pet_name == a.pet_name and \
                self.price == a.price and \
                self.description == a.description
#db.create_all()
