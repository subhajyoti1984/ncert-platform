import openai

def explain(concept, language="en", tone="neutral"):
    prompt = f"""
Explain the following NCERT concept.
Do not add new information.
Do not skip steps.

Concept:
{concept["canonical_explanation"]["english"]}
"""
    return openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )["choices"][0]["message"]["content"]
