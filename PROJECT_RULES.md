# PROJECT_RULES.md

# Intelligent Document Intelligence Engine (IDIE)

This document defines the engineering rules that MUST be followed during the development of this project.

These rules apply to every contributor, AI assistant, code generator, or future developer.

Violating these rules is considered an architectural error.

---

# 1. Primary Goal

The project aims to build a professional Document Intelligence Engine capable of understanding documents rather than simply extracting text.

The engine must:

- Understand document structure.
- Understand logical relationships.
- Extract metadata.
- Detect semantic sections.
- Analyze layout.
- Extract knowledge.
- Build structured representations of documents.

The project is NOT a simple OCR tool.

---

# 2. Development Philosophy

Always prioritize:

Architecture > Features

Correctness > Speed

Maintainability > Clever Code

Readability > Short Code

Extensibility > Temporary Solutions

Every implementation must support future expansion.

---

# 3. Architecture Stability

Never redesign the architecture unless absolutely necessary.

Do not rename core modules without explicit approval.

Avoid unnecessary refactoring.

Large architectural changes should happen only after an entire subsystem is mature.

---

# 4. Single Responsibility Principle

Every class should have one responsibility.

Examples:

PDFReader
only reads PDF files.

LayoutAnalyzer
only analyzes layout.

TitleDetector
only detects titles.

FeatureExtractor
only computes features.

Never mix responsibilities.

---

# 5. Pipeline Rules

The pipeline must remain modular.

Reader

↓

Layout

↓

Feature Extraction

↓

Detection

↓

Extraction

↓

Knowledge

↓

Inference

↓

Output

Each stage should only communicate through shared models.

Stages should never directly depend on future stages.

---

# 6. Detector Rules

Each detector must detect exactly one thing.

Examples:

TitleDetector

AuthorDetector

UniversityDetector

YearDetector

DepartmentDetector

AbstractDetector

Never create a detector responsible for multiple metadata fields.

---

# 7. Feature First

Detectors should NOT calculate geometry.

Detectors should NOT inspect raw PDF objects.

Detectors should consume features produced by FeatureExtractor.

If a detector requires new information:

Add a new feature.

Do NOT duplicate calculations.

---

# 8. No Duplicate Logic

If code is repeated twice:

Move it into a utility.

If repeated by several detectors:

Move it into FeatureExtractor.

Never duplicate algorithms.

---

# 9. Core Models

Core models represent the truth.

Avoid storing duplicated information.

Models should remain simple.

Business logic belongs outside models.

---

# 10. Layout Engine

Layout Engine is responsible for:

Header detection

Footer detection

Column detection

Reading order

Regions

Visual structure

Nothing else.

Never perform metadata extraction inside Layout.

---

# 11. Detection Engine

Detection Engine is responsible for finding metadata candidates.

Detectors should not modify unrelated fields.

Detectors should be independent.

---

# 12. Knowledge Engine

Knowledge Engine does not detect.

Knowledge Engine reasons.

Responsibilities include:

Normalization

Validation

Conflict resolution

Knowledge enrichment

Entity relationships

---

# 13. AI Usage Policy

Artificial Intelligence should assist the engine.

AI should NOT replace deterministic extraction.

Whenever possible:

Rule-based extraction first.

AI only when necessary.

The engine must remain explainable.

---

# 14. Language Independence

The engine should support multiple languages.

Avoid hardcoded assumptions.

Language-specific rules belong inside dedicated modules.

Never mix Arabic rules with English rules inside the same algorithm.

---

# 15. File Structure

Keep folders organized.

Avoid placing unrelated files together.

Prefer:

core/

readers/

layout/

detectors/

extractors/

knowledge/

pipeline/

utils/

tests/

---

# 16. Code Style

Use type hints.

Use dataclasses where appropriate.

Prefer composition over inheritance.

Avoid global variables.

Avoid magic numbers.

Use meaningful names.

Keep methods small.

---

# 17. Comments

Write comments only when necessary.

Explain WHY.

Avoid explaining WHAT.

Bad:

Increment counter.

Good:

Counter is required because PyMuPDF merges adjacent spans.

---

# 18. Testing

Every new subsystem should be tested.

Do not merge unfinished experimental code.

Use sample documents covering:

Academic thesis

Book

Report

Article

Scanned document

Arabic document

English document

Mixed language

---

# 19. Backward Compatibility

Avoid breaking existing APIs.

Prefer extending functionality.

Breaking changes require explicit approval.

---

# 20. External Dependencies

Do not add new dependencies unless they provide significant value.

Always prefer Python standard library when possible.

Every dependency must have a clear purpose.

---

# 21. Performance

Optimize only after correctness.

Avoid premature optimization.

Large documents should remain processable.

Memory usage matters.

---

# 22. Logging

Use logging instead of print() for production.

Debug output should be removable.

Never leave temporary debug code.

---

# 23. Error Handling

Never silently ignore exceptions.

Provide meaningful error messages.

Recover when possible.

Fail clearly when recovery is impossible.

---

# 24. Future AI Integration

The architecture must remain compatible with future LLM integration.

LLMs should consume structured information produced by the engine.

LLMs should not replace the engine.

---

# 25. Documentation

Every subsystem must have documentation.

Every public class should include a docstring.

Complex algorithms should be documented.

Architecture decisions should be recorded.

---

# 26. Git Rules

Commit frequently.

One feature per commit.

Meaningful commit messages.

Never commit broken code.

---

# 27. Review Rule

Before implementing new code ask:

Does this duplicate existing functionality?

Can this be reused?

Does this belong in another layer?

Will this still make sense one year from now?

If the answer is "No",

Redesign before implementation.

---

# 28. Ultimate Goal

The final system should become a professional Document Intelligence Platform capable of understanding documents with minimal AI assistance while remaining deterministic, explainable, modular, extensible, and maintainable.

Every design decision should move the project toward this goal.

---

# 29. AI Collaboration Rules

The AI assistant is a collaborator, not the project owner.

The AI must preserve the project's architecture and coding standards.

The AI should improve the project incrementally rather than redesigning it frequently.

The AI must respect previous engineering decisions unless explicitly instructed otherwise.

---

# 30. No Unrequested Refactoring

Never refactor working code unless explicitly requested.

Never redesign existing modules simply because a "better" approach exists.

If the current implementation is correct and maintainable, leave it unchanged.

Stability is preferred over perfection.

---

# 31. Preserve Existing Code

Never remove existing functionality unless instructed.

Never delete files without explicit approval.

Never replace a subsystem unless the user requests it.

Prefer extending existing code over replacing it.

---

# 32. Full File Responses

Whenever practical, provide complete files instead of partial snippets.

Avoid responses such as:

"Insert these lines..."

Prefer:

"Replace the entire file with the following."

This reduces integration mistakes.

---

# 33. Project Consistency

Before generating code, understand the existing project structure.

Do not invent filenames.

Do not assume modules exist.

Use the project's current architecture.

---

# 34. Minimize Breaking Changes

Every modification should minimize its impact.

Avoid changing public APIs.

Avoid changing model structures unless absolutely necessary.

Backward compatibility is preferred.

---

# 35. Respect Existing Naming

Use existing naming conventions.

Do not rename:

Classes

Modules

Packages

Folders

Methods

without explicit approval.

Consistency is more important than personal preference.

---

# 36. Incremental Development

Large features should be implemented gradually.

One stable improvement is better than one massive unstable rewrite.

Every stage should leave the project in a working state.

---

# 37. Explain Architectural Changes

Whenever proposing an architectural modification:

Explain:

Why the change is needed.

Benefits.

Drawbacks.

Migration impact.

Never apply architectural changes silently.

---

# 38. Never Guess Project Structure

If information is missing:

Ask.

Do not assume.

Incorrect assumptions create technical debt.

---

# 39. Prefer Reuse

Before creating:

a utility,

a model,

a helper,

a detector,

or a pipeline,

first verify whether something similar already exists.

Avoid duplication.

---

# 40. Protect the Core Models

Core models are shared across the entire engine.

Changing them has system-wide consequences.

Treat them as stable interfaces.

Modify them only when long-term benefits clearly outweigh migration costs.

---

# 41. Long-Term Thinking

Every implementation should still make sense after several years.

Avoid temporary hacks.

Avoid shortcuts.

Prefer scalable solutions.

---

# 42. Engineering over Demonstration

The objective is to build a production-quality engine.

Avoid writing code merely to demonstrate a concept.

Every implementation should be suitable for real-world use.

---

# 43. Deterministic First

Whenever possible:

Use deterministic algorithms first.

Use heuristics second.

Use AI only when deterministic methods become insufficient.

The engine should always explain how a decision was made.

---

# 44. Confidence Matters

Every extracted piece of information should eventually have:

Source

Confidence

Reason

Detection method

Even if confidence is not implemented yet, new code should be compatible with this future design.

---

# 45. Maintain Pipeline Independence

Each pipeline stage must remain independent.

A stage may consume outputs from previous stages.

A stage must never depend on future stages.

Avoid circular dependencies.

---

# 46. Production Mindset

Write code as if it will eventually process:

Millions of pages.

Thousands of books.

Scientific archives.

Government documents.

Historical manuscripts.

The architecture should support growth without major redesign.

---

# 47. Final Engineering Principle

When multiple solutions exist, choose the one that:

is easier to maintain,

is easier to test,

is easier to extend,

is easier to understand,

and preserves architectural consistency.

---

# 48. Project Constitution

This project is not being developed to become another PDF parser.

It is being developed as a complete Document Intelligence Engine.

Every subsystem should contribute to one ultimate objective:

Understanding documents rather than merely reading them.

If a proposed feature does not move the project toward that objective, it should be reconsidered.

Architecture decisions should always favor long-term scalability, explainability, determinism, and maintainability over short-term convenience.

Every contributor, whether human or AI, is expected to preserve this vision.