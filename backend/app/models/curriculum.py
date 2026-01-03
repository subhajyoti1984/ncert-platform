from pydantic import BaseModel
from typing import List, Optional

class Section(BaseModel):
    section_id: str
    title: str
    concept_sequence: List[str]

class Question(BaseModel):
    question_id: str
    question_type: str
    prompt: str
    expected_answer: str

class Concept(BaseModel):
    concept_id: str
    title: str
    canonical_explanation: dict
    checkpoint_questions: List[Question]
    expected_mistakes: Optional[list] = []
