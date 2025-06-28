import uuid
from typing import Optional, List

class Player:
    def __init__(
        self,
        name: str,
        occupation: str,
        race: str,
        gender: str,
        age: int,
        height: str,
        weight: str,
        fate_points: int,
        character_points: int,
        silver: int,
        move: int,
        body_points: int,
        agility: str,
        coordination: str,
        intellect: str,
        physique: str,
        acumen: str,
        charisma: str,
        agility_skills: Optional[List[str]] = None,
        coordination_skills: Optional[List[str]] = None,
        intellect_skills: Optional[List[str]] = None,
        physique_skills: Optional[List[str]] = None,
        acumen_skills: Optional[List[str]] = None,
        charisma_skills: Optional[List[str]] = None,
        element_id: Optional[uuid.UUID] = None
    ):
        self.element_id = element_id or uuid.uuid4()
        self.name = name
        self.occupation = occupation
        self.race = race
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.fate_points = fate_points
        self.character_points = character_points
        self.silver = silver
        self.move = move
        self.body_points = body_points
        self.agility = agility
        self.coordination = coordination
        self.intellect = intellect
        self.physique = physique
        self.acumen = acumen
        self.charisma = charisma
        self.agility_skills = agility_skills or []
        self.coordination_skills = coordination_skills or []
        self.intellect_skills = intellect_skills or []
        self.physique_skills = physique_skills or []
        self.acumen_skills = acumen_skills or []
        self.charisma_skills = charisma_skills or [] 