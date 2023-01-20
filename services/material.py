from sqlalchemy.orm import Session

from fastapi import Depends
from fastapi.exceptions import HTTPException

from database import get_session
from models.material import Rarity
from tables import Character as sqlCharacter, Evelation, Talant
from utils import Pars


class MaterialService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self, rarity: Rarity = None) -> list[sqlCharacter]:
        result = self.session.query(sqlCharacter)
        if rarity:
            return result.filter_by(rarity=rarity).all()
        return result.all()
    
    def get_list_full(self, rarity: Rarity = None):
        result = self.session.query(sqlCharacter)
        result = result.join(Evelation, sqlCharacter.evelation_id == Evelation.id)
        result = result.join(Talant, sqlCharacter.talant_id == Talant.id)
        if rarity:
            result = result.filter_by(rarity=rarity)
        return result.all()
    
    def get_character_evelation(self, rarity: Rarity = None):
        result = self.session.query(sqlCharacter)
        result = result.join(Evelation, sqlCharacter.evelation_id == Evelation.id)
        if rarity:
            result = result.filter_by(rarity=rarity)
        return result.all()
    
    def get_character_talant(self, rarity: Rarity = None):
        result = self.session.query(sqlCharacter)
        result = result.join(Talant, sqlCharacter.talant_id == Talant.id)
        if rarity:
            result = result.filter_by(rarity=rarity)
        return result.all()

    def get_filter_name(self, character_name: str) -> sqlCharacter:
        result = self.session.query(sqlCharacter).filter(sqlCharacter.name.contains(character_name)).all()
        if result:
            return result
        raise HTTPException(status_code=400, detail='Characters not found')
