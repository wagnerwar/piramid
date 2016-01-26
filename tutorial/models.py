from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Float
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Video(Base):
    __tablename__ = 'video'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    descricao = Column(Text)
    preco = Column(Float)

Index('my_index', Video.name, unique=True, mysql_length=255)
