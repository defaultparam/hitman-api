from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from uuid import UUID
from ..challenge import *
from .response_dto import Response

class ChallengeUpdateRequest(BaseModel):
	title: Optional[str] = Field(default=None, description='Title of the challenge')
	description: Optional[str] = Field(default=None, description='Description of the challenge')
	image: Optional[str] = Field(default=None, description="Base64-encoded image string (optional)", pattern=r"^[A-Za-z0-9+/]+={0,2}$")  # Image validation; do it separately? TODO
	category: Optional[CategoryEnum] = Field(default=None, description='Category of the challenge')
	destination: Optional[DestinationEnum] = Field(default=None, description='Destination of the challenge')
	rewards: Optional[List[str]] = Field(default=None, description="List of rewards, e.g., '4000xp' or 'unlockable'")
	available_in: Optional[str] = Field(default=None, description="Campaign mission in which this challenge is available")  # Campaign Mission class
	additional_properties: Optional[Dict[str, str]] = Field(default={}, description="Any additional properties as key-value pairs")

class ChallengeUpdateResponse(Response):
	pass