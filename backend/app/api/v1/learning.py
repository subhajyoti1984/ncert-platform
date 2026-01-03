from fastapi import APIRouter
from app.core.learning_engine import LearningEngine
from app.core.curriculum_loader import load_section
from app.core.evaluator import evaluate_answer
from app.core.escalation import handle_stuck

router = APIRouter()

@router.get("/section/start")
def start_section():
    section = load_section(
        "class9",
        "mathematics",
        "chapter2_polynomials",
        "section_2_2.json"
    )
    engine = LearningEngine(section, {})
    return {
        "concept_id": engine.current_concept_id()
    }

@router.post("/section/answer")
def submit_answer(payload: dict):
    engine = LearningEngine(payload["section"], payload["context"])
    correct = evaluate_answer(
        payload["student_answer"],
        payload["expected_answer"]
    )

    result = engine.evaluate(correct)

    if result == "STUCK":
        return handle_stuck(engine.current_concept_id())

    return {
        "result": result,
        "next_concept": engine.current_concept_id()
    }
