# CONTRIBUTING.md

# Contributing to Document Understanding Engine (DUE)

Thank you for your interest in contributing to the Document Understanding Engine (DUE).

This project aims to become a professional, modular, deterministic, and explainable document understanding platform.

Before writing any code, please read this document carefully.

---

# Before You Start

Every contributor (human or AI) should read the following documents in order:

1. PROJECT_VISION.md
2. PROJECT_RULES.md
3. ARCHITECTURE.md
4. ROADMAP.md
5. CONTRIBUTING.md

Do not begin implementation before understanding the project's philosophy and architecture.

---

# Project Philosophy

The objective of this project is NOT to extract text.

The objective is to understand documents.

Every contribution should move the engine toward deeper document understanding.

---

# Contribution Priorities

When choosing between multiple improvements, prioritize:

Architecture

↓

Correctness

↓

Maintainability

↓

Extensibility

↓

Performance

↓

Features

Feature count is never more important than architectural quality.

---

# Coding Standards

All new code should:

- Use Python type hints.
- Follow the existing project structure.
- Keep functions small and focused.
- Avoid duplicated logic.
- Prefer composition over inheritance.
- Include meaningful docstrings.
- Avoid unnecessary comments.
- Use descriptive names.

---

# File Organization

Place new files in the correct module.

Examples:

Readers

→ readers/

Layout

→ layout/

Detection

→ detectors/

Knowledge

→ knowledge/

Utilities

→ utils/

Tests

→ tests/

Never place unrelated functionality together.

---

# Before Creating New Code

Always ask yourself:

Does something similar already exist?

Can I reuse an existing class?

Can this become a utility?

Does this belong in another subsystem?

Avoid duplication.

---

# Architecture Rules

Never redesign the architecture without explicit approval.

Never rename core modules.

Never move major folders.

Never merge independent subsystems.

Architecture stability is more important than implementation convenience.

---

# Detector Rules

Each detector should detect exactly one thing.

Examples:

TitleDetector

AuthorDetector

YearDetector

DepartmentDetector

UniversityDetector

Do not create "UniversalDetector".

Small independent detectors are preferred.

---

# Feature Rules

Detectors should consume features.

They should not compute geometry.

If a detector needs new information:

Add a feature.

Do not duplicate calculations.

---

# AI Collaboration Rules

AI assistants are collaborators.

They are not project owners.

AI should improve the project incrementally.

AI should preserve existing architecture.

AI should not redesign working systems without approval.

---

# Pull Request Philosophy

Every contribution should answer:

Why is this needed?

What problem does it solve?

Does it preserve architecture?

Can it be tested?

Will it still make sense in five years?

If the answer is no,

reconsider the implementation.

---

# Testing

Every important subsystem should eventually have tests.

Suggested test categories:

Unit Tests

Integration Tests

Regression Tests

Performance Tests

Real-world Document Tests

---

# Sample Documents

New features should be validated against multiple document types.

Examples:

Academic Thesis

Book

Report

Article

Scanned PDF

Arabic Documents

English Documents

Mixed-language Documents

---

# Documentation

When adding a subsystem:

Update the documentation.

If architecture changes:

Document the reason.

Documentation is considered part of the implementation.

---

# Git Guidelines

Prefer small commits.

One feature per commit.

Meaningful commit messages.

Never commit broken code.

---

# AI Prompting Guidelines

If an AI assistant contributes to the project, it should:

Read all project documentation first.

Understand the current architecture.

Avoid assumptions.

Avoid creating unnecessary files.

Avoid renaming existing files.

Avoid changing project philosophy.

When uncertain,

ask for clarification instead of guessing.

---

# Long-Term Objective

This project is expected to evolve over many years.

Every contribution should help create a stable foundation for future growth.

Short-term shortcuts that increase long-term complexity should be avoided.

---

# Final Reminder

This project is not simply about processing documents.

It is about teaching software to understand documents.

Every line of code should contribute to that objective.