from pydantic import BaseModel
from typing import Optional, Any

class LearningResponse(BaseModel):
    result: str
    concept_id: Optional[str] = None
    message: Optional[str] = None
    payload: Optional[Any] = None


class EscalationResponse(BaseModel):
    action: str
    options: list
    concept_id: str
