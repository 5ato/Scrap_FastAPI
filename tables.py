from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY


Base = declarative_base()


class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    rarity = Column(String(255))
    evelation_id = Column(Integer, ForeignKey('evelations.id'))
    talant_id = Column(Integer, ForeignKey('talants.id'))
    
    evelation = relationship('Evelation', back_populates='character')
    talant = relationship('Talant', back_populates='character')


class Evelation(Base):
    __tablename__ = 'evelations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    mora = Column(Integer)
    curiosity = Column(ARRAY(String(50)))
    shard = Column(ARRAY(String(50)))
    fragment = Column(ARRAY(String(50)))
    piece = Column(ARRAY(String(50)))
    gem = Column(ARRAY(String(50)))
    mobs_shard = Column(ARRAY(String(50)))
    mobs_fragment = Column(ARRAY(String(50)))
    mobs_jewel = Column(ARRAY(String(50)))
    boss_drop = Column(ARRAY(String(50)), default=[None])

    character = relationship('Character', back_populates='evelation', uselist=False)


class Talant(Base):
    __tablename__ = 'talants'

    id = Column(Integer, primary_key=True, autoincrement=True)
    mora = Column(Integer)
    mobs_shard = Column(ARRAY(String(50)))
    mobs_fragment = Column(ARRAY(String(50)))
    mobs_jewel = Column(ARRAY(String(50)))
    book_shard = Column(ARRAY(String(50)))
    book_fragmet = Column(ARRAY(String(50)))
    book_jewel = Column(ARRAY(String(50)))
    weekly_boss_drop = Column(ARRAY(String(50)))
    crown = Column(ARRAY(String(50)))

    character = relationship('Character', back_populates='talant', uselist=False)
