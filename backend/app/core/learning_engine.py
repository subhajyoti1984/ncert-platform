from app.core.curriculum_loader import load_concept
from app.config import MAX_RETRIES

class LearningEngine:

    def __init__(self, section, context):
        self.section = section
        self.sequence = section["concept_sequence"]
        self.index = context.get("index", 0)
        self.retries = context.get("retries", 0)

    def current_concept_id(self):
        return self.sequence[self.index]

    def load_concept(self, meta):
        return load_concept(
            meta["class"],
            meta["subject"],
            meta["chapter"],
            self.current_concept_id()
        )

    def evaluate(self, is_correct):
        if is_correct:
            self.index += 1
            self.retries = 0
            if self.index >= len(self.sequence):
                return "SECTION_COMPLETE"
            return "ADVANCE"
        else:
            self.retries += 1
            if self.retries > MAX_RETRIES:
                return "STUCK"
            return "RETRY"
