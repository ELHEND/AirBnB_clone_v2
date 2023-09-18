#!/usr/bin/python3
"""This is  amenity class"""
<<<<<<< HEAD

=======
>>>>>>> c5cc3f3369e8c3452879eee63c7f95a92f72757b
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

from models.place import place_amenity


class Amenity(BaseModel, Base):
    """This is  class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
