__author__ = 'yuhuishi'

from MenuApp import db


class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_plate = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer)
    cdsid = db.Column(db.String(50))
    comment = db.Column(db.String)

    def __init__(self, name, year, cdsid, comment):
        self.name_plate = name
        self.year = year
        self.cdsid = cdsid
        self.comment = comment

    def __repr__(self):
        return "<Program: %s, %d>" % (self.name_plate, self.year)
