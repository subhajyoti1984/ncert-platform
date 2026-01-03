import json
from app.config import CURRICULUM_DIR

def load_section(class_id, subject, chapter, section_file):
    path = CURRICULUM_DIR / class_id / subject / chapter / section_file
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_concept(class_id, subject, chapter, concept_id):
    path = (
        CURRICULUM_DIR /
        class_id /
        subject /
        chapter /
        "concepts" /
        f"{concept_id}.json"
    )
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
