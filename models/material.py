from pydantic import BaseModel

from enum import Enum


class Rarity(str, Enum):
    five_star = '5 Stars'
    four_star = '4 Stars'


class Character(BaseModel):
    id: int
    name: str
    rarity: Rarity

    class Config:
        orm_mode = True


class BaseMaterial(BaseModel):
    id: int
    mora: int
    mobs_shard: list[str, int]
    mobs_fragment: list[str, int]
    mobs_jewel: list[str, int]

    class Config:
        orm_mode = True


class Evelation(BaseMaterial):
    curiosity: list[str, int]
    shard: list[str, int]
    fragment: list[str, int]
    piece: list[str, int]
    gem: list[str, int]
    boss_drop: list[str, int]


class Talant(BaseMaterial):
    book_shard: list[str, int]
    book_fragmet: list[str, int]
    book_jewel: list[str, int]
    weekly_boss_drop: list[str, int]
    crown: list[str, int]


class CharacterFull(Character):
    evelation: Evelation
    talant: Talant


class CharacterEvelation(Character):
    evelation: Evelation


class CharacterTalant(Character):
    talant: Talant


class CharacterFullID(Character):
    evelation_id: int
    talant_id: int
