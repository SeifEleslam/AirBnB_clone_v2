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
    __engine = None
    __session = None

    def __init__(self):
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

        if cls is None:
            all_data = self.__session.query(
                User, State, City, Amenity, Place, Review
            ).all()
        else:
            all_data = self.__session.query(cls).all()
        result = {}
        for item in all_data:
            item_dict = item.to_dict()
            result['{}.{}'.format(
                item_dict['__class__'], item_dict['id'])] = item
        return result

    def reload(self):
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(
            autoflush=False, expire_on_commit=False, bind=self.__engine)
        self.__session = scoped_session(Session)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj):
        if obj is not None:
            self.__session.delete(obj)
