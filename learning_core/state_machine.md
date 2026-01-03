# LEARNING CORE — STATE MACHINE (FROZEN)

This document defines the immutable teaching flow.
No AI, UI, or payment logic is allowed here.

---

## STATES

START_CONCEPT  
EXPLAIN  
QUESTION_LOOP  
EVALUATE  
CORRECT  
WRONG  
RETRY  
ADVANCE  
CONCEPT_COMPLETE  

---

## FLOW DEFINITION

START_CONCEPT
 → EXPLAIN
 → QUESTION_LOOP
     → EVALUATE
         → CORRECT → NEXT_QUESTION / ADVANCE
         → WRONG
             → RETRY (if retries left)
             → SIGNAL_STUCK (if retries exhausted)
 → CONCEPT_COMPLETE

---

## RULES (NON-NEGOTIABLE)

1. Each concept is processed independently.
2. Multiple questions per concept are allowed.
3. Advancement requires conceptual correctness.
4. Guessing must not allow advancement.
5. Learning Core does NOT:
   - Generate explanations
   - Diagnose mistakes
   - Choose language
   - Decide tutor or AI usage

---

## EXTERNAL SIGNALS

- STUCK → handled by Orchestration Engine
- ADVANCE → handled internally
- COMPLETE → move to next concept

---

Status: FROZEN (v1.0)
