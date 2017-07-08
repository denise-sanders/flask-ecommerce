from app import db
import enum

class DressStatus(enum.Enum):
    one = 1
    two = 2
    three = 3


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_first = db.Column(db.String(64), index=True)
    name_last = db.Column(db.String(64), index=True)
    name_full = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    selling = db.relationship('Dress', backref='seller', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.name_full)

class Dress(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Float, primary_key=True)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.Enum(DressStatus))
    # can I make the status an enum type value, as sold, on the market, removed, closed, in process
    # add multiple picutres to be allowed (perhaps up to three?)
    def __repr__(self):
       return '<Post %r>' % (self.body)


class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    dress_id = db.Column(db.Integer, db.ForeignKey('dress.id'))

    def __repr__(self):
        return '<Picture %r %r>' % (self.file_name, self.dress_id)
