from core.models.document import Document
from core.models.page import Page
from pipeline.document_pipeline import DocumentPipeline


def test_pipeline_returns_success():
    document = Document(
        filename="sample.pdf",
        file_path="samples/sample.pdf",
        file_type="pdf",
    )

    pipeline = DocumentPipeline()
    result = pipeline.analyze(document)

    assert result.success is True
    assert result.document == document


def test_cover_section_detected_when_pages_exist():
    document = Document(
        filename="sample.pdf",
        file_path="samples/sample.pdf",
        file_type="pdf",
        pages=[Page(number=1, text="عنوان الرسالة\nجامعة بغداد")],
    )

    pipeline = DocumentPipeline()
    result = pipeline.analyze(document)

    section_types = [section.section_type for section in result.document.sections]

    assert "cover" in section_types


def test_no_cover_section_when_no_pages():
    document = Document(
        filename="sample.pdf",
        file_path="samples/sample.pdf",
        file_type="pdf",
        pages=[],
    )

    pipeline = DocumentPipeline()
    result = pipeline.analyze(document)

    assert result.document.sections == []


def test_abstract_detected_and_extracted_arabic():
    document = Document(
        filename="sample.pdf",
        file_path="samples/sample.pdf",
        file_type="pdf",
        pages=[
            Page(number=1, text="عنوان الرسالة"),
            Page(number=2, text="الملخص\nهذا هو نص الملخص التجريبي."),
        ],
    )

    pipeline = DocumentPipeline()
    result = pipeline.analyze(document)

    section_types = [section.section_type for section in result.document.sections]

    assert "abstract" in section_types
    assert result.document.metadata.abstract == "هذا هو نص الملخص التجريبي."


def test_abstract_detected_english():
    document = Document(
        filename="sample.pdf",
        file_path="samples/sample.pdf",
        file_type="pdf",
        pages=[
            Page(number=1, text="Thesis Title"),
            Page(number=2, text="Abstract\nThis is a sample abstract text."),
        ],
    )

    pipeline = DocumentPipeline()
    result = pipeline.analyze(document)

    section_types = [section.section_type for section in result.document.sections]

    assert "abstract" in section_types
    assert result.document.metadata.abstract == "This is a sample abstract text."


def test_toc_detected_arabic():
    document = Document(
        filename="sample.pdf",
        file_path="samples/sample.pdf",
        file_type="pdf",
        pages=[
            Page(number=1, text="عنوان الرسالة"),
            Page(number=2, text="الفهرس\nالفصل الأول ... 1\nالفصل الثاني ... 10"),
        ],
    )

    pipeline = DocumentPipeline()
    result = pipeline.analyze(document)

    section_types = [section.section_type for section in result.document.sections]

    assert "toc" in section_types


def test_toc_detected_english():
    document = Document(
        filename="sample.pdf",
        file_path="samples/sample.pdf",
        file_type="pdf",
        pages=[
            Page(number=1, text="Thesis Title"),
            Page(number=2, text="Table of Contents\nChapter 1 ... 1\nChapter 2 ... 10"),
        ],
    )

    pipeline = DocumentPipeline()
    result = pipeline.analyze(document)

    section_types = [section.section_type for section in result.document.sections]

    assert "toc" in section_types


def test_no_toc_when_not_present():
    document = Document(
        filename="sample.pdf",
        file_path="samples/sample.pdf",
        file_type="pdf",
        pages=[
            Page(number=1, text="Thesis Title"),
            Page(number=2, text="Chapter 1: Introduction\nSome content here."),
        ],
    )

    pipeline = DocumentPipeline()
    result = pipeline.analyze(document)

    section_types = [section.section_type for section in result.document.sections]

    assert "toc" not in section_types


def test_author_detected_english_by_marker_next_line():
    document = Document(
        filename="sample.pdf",
        file_path="samples/sample.pdf",
        file_type="pdf",
        pages=[
            Page(number=1, text="Thesis Title\nby\nJohn Smith\nJune 2026"),
            Page(number=2, text="Table of Contents\nChapter 1 ... 1"),
        ],
    )

    pipeline = DocumentPipeline()
    result = pipeline.analyze(document)

    assert result.document.metadata.author == "John Smith"


def test_author_detected_arabic_marker_same_line():
    document = Document(
        filename="sample.pdf",
        file_path="samples/sample.pdf",
        file_type="pdf",
        pages=[
            Page(number=1, text="عنوان الرسالة\nإعداد: أحمد محمد\nجامعة بغداد"),
            Page(number=2, text="الفهرس\nالفصل الأول ... 1"),
        ],
    )

    pipeline = DocumentPipeline()
    result = pipeline.analyze(document)

    assert result.document.metadata.author == "أحمد محمد"


def test_university_detected_english():
    document = Document(
        filename="sample.pdf",
        file_path="samples/sample.pdf",
        file_type="pdf",
        pages=[
            Page(number=1, text="Thesis Title\nUniversity of Example\nby\nJohn Smith"),
            Page(number=2, text="Table of Contents\nChapter 1 ... 1"),
        ],
    )

    pipeline = DocumentPipeline()
    result = pipeline.analyze(document)

    assert result.document.metadata.university == "University of Example"


def test_university_detected_arabic():
    document = Document(
        filename="sample.pdf",
        file_path="samples/sample.pdf",
        file_type="pdf",
        pages=[
            Page(number=1, text="عنوان الرسالة\nجامعة بغداد\nإعداد: أحمد محمد"),
            Page(number=2, text="الفهرس\nالفصل الأول ... 1"),
        ],
    )

    pipeline = DocumentPipeline()
    result = pipeline.analyze(document)

    assert result.document.metadata.university == "جامعة بغداد"


def test_department_detected_english():
    document = Document(
        filename="sample.pdf",
        file_path="samples/sample.pdf",
        file_type="pdf",
        pages=[
            Page(
                number=1,
                text="Thesis Title\nDepartment of Computer Science\nby\nJohn Smith",
            ),
            Page(number=2, text="Table of Contents\nChapter 1 ... 1"),
        ],
    )

    pipeline = DocumentPipeline()
    result = pipeline.analyze(document)

    assert result.document.metadata.department == "Department of Computer Science"


def test_department_detected_arabic():
    document = Document(
        filename="sample.pdf",
        file_path="samples/sample.pdf",
        file_type="pdf",
        pages=[
            Page(number=1, text="عنوان الرسالة\nقسم علوم الحاسوب\nإعداد: أحمد محمد"),
            Page(number=2, text="الفهرس\nالفصل الأول ... 1"),
        ],
    )

    pipeline = DocumentPipeline()
    result = pipeline.analyze(document)

    assert result.document.metadata.department == "قسم علوم الحاسوب"


def test_no_author_university_department_when_absent():
    document = Document(
        filename="sample.pdf",
        file_path="samples/sample.pdf",
        file_type="pdf",
        pages=[
            Page(number=1, text="Thesis Title\nJune 2026"),
            Page(number=2, text="Table of Contents\nChapter 1 ... 1"),
        ],
    )

    pipeline = DocumentPipeline()
    result = pipeline.analyze(document)

    assert result.document.metadata.author is None
    assert result.document.metadata.university is None
    assert result.document.metadata.department is None