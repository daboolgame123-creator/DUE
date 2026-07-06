# ARCHITECTURE.md

# Intelligent Document Intelligence Engine (IDIE)

Version: 1.0

---

# Overview

The Intelligent Document Intelligence Engine (IDIE) is a modular document understanding system designed to analyze documents at multiple levels.

Unlike traditional PDF parsers or OCR tools, IDIE aims to understand the logical structure and semantic content of documents.

The engine separates every responsibility into independent subsystems to ensure scalability, maintainability, and explainability.

---

# Project Vision

The long-term goal is to transform documents into structured knowledge.

Instead of asking:

"What text exists in this PDF?"

The engine should answer:

"What does this document contain?"

It should understand:

- document structure
- document hierarchy
- metadata
- layout
- semantic sections
- tables
- figures
- images
- references
- entities
- relationships
- knowledge

---

# High-Level Architecture

```
                +--------------------+
                |   Input Document   |
                +--------------------+
                          |
                          ▼
                +--------------------+
                |      Readers       |
                +--------------------+
                          |
                          ▼
                +--------------------+
                | Document Model     |
                +--------------------+
                          |
                          ▼
                +--------------------+
                | Layout Analyzer    |
                +--------------------+
                          |
                          ▼
                +--------------------+
                | Feature Extraction |
                +--------------------+
                          |
                          ▼
                +--------------------+
                | Detection Engine   |
                +--------------------+
                          |
                          ▼
                +--------------------+
                | Extraction Engine  |
                +--------------------+
                          |
                          ▼
                +--------------------+
                | Knowledge Engine   |
                +--------------------+
                          |
                          ▼
                +--------------------+
                | Inference Engine   |
                +--------------------+
                          |
                          ▼
                +--------------------+
                | Final Output       |
                +--------------------+
```

---

# Pipeline

The pipeline is strictly sequential.

Each stage consumes the output of the previous stage.

No stage should depend on future stages.

```
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
```

---

# Core Data Flow

Input PDF

↓

Reader loads pages

↓

Reader extracts raw objects

↓

Document model is created

↓

Layout analyzer understands page geometry

↓

Feature extractor computes block features

↓

Detection engine finds metadata

↓

Extraction engine extracts structured information

↓

Knowledge engine validates and enriches results

↓

Inference engine performs reasoning

↓

Structured document is produced

---

# Folder Responsibilities

## core/

Contains shared models and interfaces.

Examples:

- Document
- Page
- BoundingBox
- Metadata
- Statistics
- Interfaces

The core package should remain lightweight.

Business logic does not belong here.

---

## readers/

Responsible for reading files.

Examples:

PDFReader

ImageReader

DOCXReader

Future:

EPUBReader

HTMLReader

PowerPointReader

Readers never perform document understanding.

Their only responsibility is converting files into Document objects.

---

## layout/

Responsible for visual document understanding.

Includes:

Header detection

Footer detection

Column detection

Reading order

Page regions

Layout statistics

Block classification

The layout module never extracts metadata.

---

## detectors/

Responsible for detecting metadata candidates.

Examples:

TitleDetector

AuthorDetector

UniversityDetector

DepartmentDetector

YearDetector

KeywordDetector

Each detector detects one thing.

Nothing more.

---

## extractors/

Responsible for extracting structured information.

Examples:

Abstract extraction

Table extraction

Image extraction

Reference extraction

TOC extraction

Extractors convert detected regions into structured data.

---

## knowledge/

Responsible for reasoning.

Examples:

Normalization

Validation

Conflict resolution

Ontology

Entity linking

Knowledge graph

Knowledge enrichment

---

## pipeline/

Coordinates all stages.

The pipeline controls execution order.

Pipeline stages remain independent.

---

## utils/

Contains reusable helper functions.

Avoid placing business logic here.

---

## tests/

Contains all automated tests.

Every subsystem should eventually have tests.

---

# Core Models

The Document model is the heart of the engine.

Everything revolves around it.

```
Document

├── Metadata

├── Pages

├── Layout

├── Statistics

├── Sections

├── Images

├── Tables

└── Properties
```

No subsystem should duplicate this information.

---

# Layout Model

Each page contains:

Header

Body

Footer

Columns

Reading Order

Text Blocks

Images

Tables

Drawings

The Layout module is purely geometric.

---

# Detection Model

Detection is evidence-based.

Detectors analyze features generated earlier.

Future versions will use:

Candidate scoring

Confidence

Voting

Multi-detector agreement

Detectors should never directly analyze raw PDF geometry.

---

# Knowledge Model

Knowledge Engine transforms extracted information into meaningful knowledge.

Examples:

Detect duplicate authors.

Normalize university names.

Infer publication year.

Resolve conflicting metadata.

Build semantic relationships.

Knowledge is not extraction.

Knowledge is reasoning.

---

# Inference Model

Inference is the highest reasoning layer.

Examples:

Infer missing metadata.

Classify document type.

Predict document language.

Determine academic discipline.

Estimate confidence.

Future versions may integrate AI models.

---

# Future Architecture

The engine is designed for gradual expansion.

Future modules include:

OCR Engine

Vision Engine

Search Engine

Embedding Engine

Knowledge Graph

LLM Integration

Citation Engine

Document Comparison

Question Answering

Summarization

Translation

Entity Recognition

Relationship Extraction

---

# Design Principles

The architecture follows:

Single Responsibility Principle

Modular Design

Composition over Inheritance

Deterministic Algorithms First

Explainability

Scalability

Maintainability

Low Coupling

High Cohesion

---

# AI Integration Philosophy

Artificial Intelligence is an enhancement layer.

AI should consume structured information produced by the engine.

AI should not replace deterministic processing.

The engine should always remain explainable.

---

# Ultimate Objective

The final objective is not to parse documents.

The objective is to understand documents.

Every subsystem should contribute to that single goal.