from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from settings import settings
from tables import Evelation, Talant, Character
from utils import Pars


engine = create_engine(url=settings.database_url, echo=True)


session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False
)


def get_session() -> Session:
    Session = session()
    try:
        yield Session
    finally:
        Session.close()


if __name__ == '__main__':
    with session() as db:
        p = Pars(url='https://genshin-impact.fandom.com/wiki/Character#Playable_Characters')
        result = db.query(Character).all()
        result = [i.name for i in result]
        for character in p.get_urls():
            if 'Traveler' not in character and character[0] not in result:
                info = p.get_character(url=character[1], name=character[0], rarity=character[2])
                c = Character(name=info[0][0], rarity=info[0][1])
                e = Evelation(mora=info[1][0][1], boss_drop=info[1][1], shard=info[1][2], fragment=info[1][3],
                              piece=info[1][4], gem=info[1][5], curiosity=info[1][6], mobs_shard=info[1][7],
                              mobs_fragment=info[1][8], mobs_jewel=info[1][9])
                t = Talant(mora=info[2][0][1], mobs_shard=info[2][1], mobs_fragment=info[2][2], mobs_jewel=info[2][3],
                           book_shard=info[2][4], book_fragmet=info[2][5], book_jewel=info[2][6], weekly_boss_drop=info[2][7],
                           crown=info[2][8])
                c.evelation = e
                c.talant = t
                db.add_all([e, t, c])
                db.commit()
