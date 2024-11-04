from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from ..models.challenge import Challenge
from ..models.dtos.challenge_create_dto import ChallengeCreateRequest, ChallengeCreateResponse
from ..models.dtos.challenge_update_dto import ChallengeUpdateRequest, ChallengeUpdateResponse
from ..services.config_service import ConfigService

router = APIRouter(prefix='/challenges', tags=["Challenges Configuration"])

config_service = ConfigService()

# Create challenge
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_challenge(challenge: ChallengeCreateRequest) -> ChallengeCreateResponse:
	try:
		challenge_id = config_service.create_challenge(challenge)
		return ChallengeCreateResponse(message='Challenge created successfully', challenge_id=challenge_id)
	except Exception as e:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# Update challenge
@router.put('/<challenge_id>', status_code=status.HTTP_200_OK)
def update_challenge(challenge_id: UUID, challenge: ChallengeUpdateRequest) -> ChallengeUpdateResponse:
	try:
		challenge = config_service.update_challenge(challenge_id, challenge)
		return ChallengeUpdateResponse(message='Challenge updated successfully')
	except Exception as e:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# Delete challenge
@router.delete('/<challenge_id>', status_code=status.HTTP_204_NO_CONTENT)
def delete_challenge(challenge_id: UUID):
	return config_service.delete_challenge(challenge_id)

# Get challenge by id 
@router.get('/<challenge_id>')
def get_challenge(challenge_id: UUID):
	return config_service.get_challenge(challenge_id)

# Get all challenges in the db
@router.get('/all', status_code=status.HTTP_200_OK)
def get_all_challenges():
	return config_service.get_all_challenges()