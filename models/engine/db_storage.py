"""DBStorage Module"""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, MetaData
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

import os


class DBStorage:
    """Class for handling db engine"""
    __engine = None
    __session = None
    __tables = [City, State]

    def __init__(self):
        """Initializing The class based on env variables"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.environ["HBNB_MYSQL_USER"],
                os.environ["HBNB_MYSQL_PWD"],
                os.environ["HBNB_MYSQL_HOST"],
                os.environ["HBNB_MYSQL_DB"]), pool_pre_ping=True)
        if 'HBNB_ENV' in os.environ and os.environ["HBNB_ENV"] == "test":
            metadata = MetaData(bind=self.__engine)
            metadata.reflect()
            metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return all instances of a model."""
        if cls is None:
            all_data = []
            for table in self.__tables:
                all_data.extend(self.__session.query(table).all())
        else:
            all_data = self.__session.query(cls).all()
        result = {}
        for item in all_data:
            item_dict = item.to_dict()
            result['{}.{}'.format(
                item_dict['__class__'], item_dict['id'])] = item
        return result

    def reload(self):
        """Reload the database session."""
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(
            autoflush=False, expire_on_commit=False, bind=self.__engine)
        self.__session = scoped_session(Session)

    def new(self, obj):
        """Add an object to the session."""
        self.__session.add(obj)

    def save(self):
        """Save the current state of the session."""
        self.__session.commit()

    def delete(self, obj):
        """Delete an object from the session."""
        if obj is not None:
            self.__session.delete(obj)
