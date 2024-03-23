#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", backref="state", cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """Return Cities linked to this state"""
            from models import storage
            from models.city import City
            result = []
            for _, city in storage.all(City).items():
                if city.state_id == self.id:
                    result.append(city)
            return (result)
