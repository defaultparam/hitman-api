from pydantic import BaseModel, Field, StrictStr
from typing import Optional, List, Dict
from uuid import UUID
from enum import Enum

class CategoryEnum(Enum): # find a way to track how many total challenges are available under 1 category
	ASSASSINATION = 'assassination'
	DISCOVERY = 'discovery'
	FEATS = 'feats'
	TARGETS = 'targets'
	THE_CLASSICS = 'the_classics'
	ARCADE = 'arcade'
	ESCALATION_TRACK_1 = 'escalation_track_1'
	ESCALATION_TRACK_2 = 'escalation_track_2'
	CODENAME_47 = 'codename_47'
	CLOUD_NINE = 'cloud_nine'


class DestinationEnum(Enum):
	ICA_FACILITY__CLASSIFIED = 'ica_facility__classified'
	PARIS__FRANCE = 'paris__france'
	SAPIENZA__ITALY = 'sapienza__italy'
	MARRAKESH__MOROCCO = 'marrakesh__morocco'
	BANGKOK__THAILAND = 'bangkok__thailand'
	COLORADO__USA = 'colorado__usa'
	HOKKAIDO__JAPAN = 'hokkaido__japan'
	HAWKES_BAY__NEW_ZEALAND = 'hawkes_bay__new_zealand'
	MIAMI__USA = 'miami__usa'
	SANTA_FORTUNA__COLOMBIA = 'santa_fortuna__colombia'
	MUMBAI__INDIA = 'mumbai__india'
	WHITTLETON_CREEK__USA = 'whittleton_creek__usa'
	AMBROSE_ISLAND__ANDAMAN_SEA = 'ambrose_island__andaman_sea'
	ISLE_OF_SGAIL__NORTH_ATLANTIC = 'isle_of_sgail__north_atlantic'
	NEW_YORK__USA = 'new_york__usa'
	HAVEN_ISLAND__MALDIVES = 'haven_island__maldives'
	DUBAI__UNITED_ARAB_EMIRATES = 'dubai__united_arab_emirates'
	DARTMOOR__ENGLAND = 'dartmoor__england'
	BERLIN__GERMANY = 'berlin__germany'
	CHONGQING__CHINA = 'chongqing__china'
	MENDOZA__ARGENTINA = 'mendoza__argentina'
	CARPATHIAN_MOUNTAINS__ROMANIA = 'carpathian_mountains__romania'
	SECRET_LOCATION_SAFEHOUSE__CLASSIFIED = 'secret_location_safehouse__classified'
	
	#sniper assassin
	HIMMELSTEIN__AUSTRIA = 'himmelstein__austria'
	HANTU_PORT__SINGAPORE = 'hantu_port__singapore'
	SIBERIA__RUSSIA = 'siberia__russia'

class Challenge(BaseModel):
	id: UUID = Field(..., description="Unique identifier for the challenge") # Using ULID from Pydantic
	title: StrictStr = Field(..., description='Title of the challenge')
	description: StrictStr = Field(..., description='Description of the challenge')
	image: StrictStr = Field(..., description="Base64-encoded image string (required)", 
		pattern=r"^[A-Za-z0-9+/]+={0,2}$") #Image validation; Do it separately? TODO
	is_completed: bool = Field(default=False, description="Completion status of the challenge")
	category: CategoryEnum
	destination: DestinationEnum
	rewards: List[str] = Field(..., description="List of rewards, e.g., '4000xp' or 'unlockable'")
	available_in: StrictStr = Field(..., description="Campaign mission in which this challenge is available") #Campaign Mission class
	additional_properties: Optional[Dict[str, str]] = Field(default=None, description="Any additional properties as key-value pairs")