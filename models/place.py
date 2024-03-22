#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table("place_amenity",  Base.metadata,
                          Column('place_id', String(60), ForeignKey(
                              'places.id'), primary_key=True),
                          Column('amenity_id', String(60), ForeignKey(
                              'amenities.id'), primary_key=True),
                          )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey(
        "cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey(
        "users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', backref='place', cascade="all, delete")

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship(
            "Amenity", secondary=place_amenity,
            viewonly=False, back_populates='place_amenities')
    else:
        amenity_ids = []

        @property
        def amenities(self):
            """Return Cities linked to this state"""
            from models import storage
            from models.amenity import Amenity
            result = []
            for _, amenity in storage.all(Amenity).items():
                if amenity.id in self.amenity_ids:
                    result.append(amenity)
            return (result)

        @amenities.setter
        def amenities(self, val):
            from models.amenity import Amenity
            if type(val) is Amenity:
                self.amenity_ids.append(val.id)
