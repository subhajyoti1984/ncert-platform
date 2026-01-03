from fastapi import APIRouter
from app.services.progress_service import (
    get_section_progress,
    update_concept_progress
)

router = APIRouter()

@router.get("/section/{section_id}")
def fetch_section_progress(user_id: str, section_id: str):
    """
    Returns progress snapshot for a given section.
    """
    return get_section_progress(user_id, section_id)


@router.post("/concept/update")
def update_progress(payload: dict):
    """
    Updates concept-level progress after evaluation.
    """
    return update_concept_progress(
        user_id=payload["user_id"],
        concept_id=payload["concept_id"],
        status=payload["status"],
        mistake_code=payload.get("mistake_code")
    )
