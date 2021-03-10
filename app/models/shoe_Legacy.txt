from app import db

class Shoe(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Float, index=True)
    brand = db.Column(db.String(80), index=True)
    model = db.Column(db.String(80), index=True, unique=True)

    # override python print
    def __repr__(self):
        return '<Shoe {}>'.format(self.model)

    


    #CREATE
    def save(self):
        # saving shoe
        db.session.add(self)
        # commit transaction
        db.session.commit()

        return self.id

    #READ
    # Shoe.query.get()
    def get_all():
        # get all shoes
        return Shoe.query.all()

    def get(id):
        return db.session.query(Shoe).filter(Shoe.id == id).first()


    #UPDATE
    def update(self):
        # session is th connection with the database
        db.session.commit()

    #DELETE
    def delete(id):
        shoe = Shoe.get(id=id)
        db.session.delete(shoe)
        db.session.commit()