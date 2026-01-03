from app.core.db import conn

def update_concept_progress(user_id, concept_id, status, mistake_code=None):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO concept_progress (user_id, concept_id, status, dominant_mistake)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (user_id, concept_id)
            DO UPDATE SET status=%s, dominant_mistake=%s, updated_at=NOW()
        """, (user_id, concept_id, status, mistake_code, status, mistake_code))
        conn.commit()
