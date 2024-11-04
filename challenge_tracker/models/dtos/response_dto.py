from pydantic import BaseModel, StrictStr

class Response(BaseModel):
    message: StrictStr
