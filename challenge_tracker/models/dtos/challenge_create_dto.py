from pydantic import BaseModel, constr, Field, StrictBool, StrictStr
from typing import Optional, List, Dict
from ..challenge import DestinationEnum, CategoryEnum, Challenge
from .response_dto import Response
from uuid import UUID, uuid4

class ChallengeCreateRequest(BaseModel):
	title: StrictStr = Field(..., description='Title of the challenge')
	description: StrictStr = Field(..., description='Description of the challenge')
	image: StrictStr = Field(..., description="Base64-encoded image string (required)", 
		pattern=r"^[A-Za-z0-9+/]+={0,2}$") #Image validation; Do it separately? TODO
	category: CategoryEnum
	destination: DestinationEnum
	rewards: List[str] = Field(..., description="List of rewards, e.g., '4000xp' or 'unlockable'")
	available_in: StrictStr = Field(..., description="Campaign mission in which this challenge is available") #Campaign Mission class
	additional_properties: Optional[Dict[str, str]] = Field(default={}, description="Any additional properties as key-value pairs")

	def to_challenge(self):
		challenge_id = uuid4()
		challenge = Challenge(
			id=challenge_id, 
			title=self.title, 
			description=self.description, 
			image=self.image,
			category=self.category,
			destination=self.destination,
			rewards=self.rewards,
			available_in=self.available_in,
			additional_properties=self.additional_properties,
			is_completed=False # default to false
		)

		return challenge

class ChallengeCreateResponse(Response):
	challenge_id: UUID