from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

class Venue(db.Model):
     __tablename__ = 'venue'
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String)
     genres = db.Column(db.ARRAY(db.String()))
     address = db.Column(db.String(120))
     city = db.Column(db.String(120))
     state = db.Column(db.String(120))
     phone = db.Column(db.String(120))
     image_link = db.Column(db.String(500))
     facebook_link = db.Column(db.String(120))
     website = db.Column(db.String(120))
     seeking_talent = db.Column(db.Boolean)
     seeking_description = db.Column(db.String(500))
     shows = db.relationship('Show', backref="venue", lazy=True)

    #  def __repr__(self):
    #      return f'<Venue:: id:{self.id}, name:{self.name}>'    

     def __repr__(self):
         value = "Venue({}, {})".format(self.id, self.name)
         return value 


class Artist(db.Model):
    __tablename__ = 'artist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genres = db.Column(db.ARRAY(db.String()))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref="artist", lazy=True)

    def __repr__(self):
        return f'<Artist:: id:{self.id}, name:{self.name}>'

class Show(db.Model):
     __tablename__ = 'show'
     id         = db.Column(db.Integer, primary_key=True)
     artist_id  = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
     venue_id   = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
     start_time = db.Column(db.DateTime, nullable=False)

     def __repr__(self):
         return '<Show: Artist: {} Venue: {} start: {}>'.format(self.artist_id, self.venue_id, self.start_time)