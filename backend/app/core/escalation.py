def handle_stuck(concept_id):
    return {
        "action": "ESCALATE",
        "options": ["AI_EXPLANATION", "RETRY"]
    }
