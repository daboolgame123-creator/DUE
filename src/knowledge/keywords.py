"""Bilingual keyword lists used by detectors to recognize document
sections and front-matter fields.

These lists are intentionally simple for this phase. They will move
into external resource files (JSON/YAML) once the knowledge layer
grows.
"""

ABSTRACT_KEYWORDS_AR = [
    "الملخص",
    "ملخص",
    "المستخلص",
    "مستخلص البحث",
    "ملخص البحث",
]

ABSTRACT_KEYWORDS_EN = [
    "abstract",
    "summary",
]

ABSTRACT_KEYWORDS = ABSTRACT_KEYWORDS_AR + ABSTRACT_KEYWORDS_EN


TOC_KEYWORDS_AR = [
    "الفهرس",
    "فهرس المحتويات",
    "المحتويات",
    "جدول المحتويات",
]

TOC_KEYWORDS_EN = [
    "table of contents",
    "contents",
]

TOC_KEYWORDS = TOC_KEYWORDS_AR + TOC_KEYWORDS_EN


# Markers that typically precede the author's name in a title/cover page.
# Order matters slightly: longer/more specific markers should be checked
# effectively the same way as shorter ones since matching is a simple
# "startswith", so no special ordering is required here.
AUTHOR_MARKERS_AR = [
    "من إعداد الطالب",
    "اعداد الطالب",
    "إعداد الطالب",
    "من إعداد",
    "إعداد",
    "اعداد",
    "الطالب",
    "الباحث",
]

AUTHOR_MARKERS_EN = [
    "presented by",
    "authors",
    "author",
    "by",
]

AUTHOR_MARKERS = AUTHOR_MARKERS_AR + AUTHOR_MARKERS_EN


UNIVERSITY_KEYWORDS_AR = [
    "جامعة",
]

UNIVERSITY_KEYWORDS_EN = [
    "university",
]

UNIVERSITY_KEYWORDS = UNIVERSITY_KEYWORDS_AR + UNIVERSITY_KEYWORDS_EN


DEPARTMENT_KEYWORDS_AR = [
    "قسم",
]

DEPARTMENT_KEYWORDS_EN = [
    "department of",
    "department",
]

DEPARTMENT_KEYWORDS = DEPARTMENT_KEYWORDS_AR + DEPARTMENT_KEYWORDS_EN