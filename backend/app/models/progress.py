from pydantic import BaseModel
from typing import Optional

class ConceptProgress(BaseModel):
    concept_id: str
    attempts: int = 0
    status: str = "NOT_ATTEMPTED"
    dominant_mistake: Optional[str] = None
