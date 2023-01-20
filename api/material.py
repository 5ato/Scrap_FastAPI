from fastapi import APIRouter, Depends

from models.material import CharacterFullID, CharacterFull, CharacterEvelation, CharacterTalant, Rarity
from services.material import MaterialService


router = APIRouter(prefix='/material')


@router.get('/', response_model=list[CharacterFull])
def get_all_charactersFull(
    rarity: Rarity = None,
    service: MaterialService = Depends()
):
    return service.get_list_full(rarity=rarity)


@router.get('/character_evelation', response_model=list[CharacterEvelation])
def get_all_charactersFull(
    rarity: Rarity = None,
    service: MaterialService = Depends()
):
    return service.get_character_evelation(rarity=rarity)


@router.get('/character_talants', response_model=list[CharacterTalant])
def get_all_charactersFull(
    rarity: Rarity = None,
    service: MaterialService = Depends()
):
    return service.get_character_talant(rarity=rarity)


@router.get('/character_full_id', response_model=list[CharacterFullID])
def get_all_characters(
    rarity: Rarity = None,
    service: MaterialService = Depends()
):
    return service.get_list(rarity=rarity)


@router.get('/{character_name}', response_model=list[CharacterFullID])
def get_filter_name_characters(
    character_name: str,
    service: MaterialService = Depends(),
):
    return service.get_filter_name(character_name)
