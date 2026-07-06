from pathlib import Path

from pipeline.document_pipeline import DocumentPipeline
from readers.reader_manager import ReaderManager
from readers.pdf_reader import PDFReader


def build_report(document, result) -> str:
    lines = []

    lines.append("=" * 50)
    lines.append(f"File      : {document.filename}")
    lines.append(f"Type      : {document.file_type}")
    lines.append(f"Pages     : {document.metadata.page_count}")
    lines.append(f"Title     : {result.document.metadata.title}")
    lines.append(f"Abstract  : {result.document.metadata.abstract}")

    lines.append("\nDetected sections:")
    if result.document.sections:
        for section in result.document.sections:
            lines.append(
                f"  - {section.section_type} "
                f"(pages {section.start_page}-{section.end_page}, "
                f"confidence {section.confidence})"
            )
    else:
        lines.append("  (none)")

    lines.append("=" * 50)

    for page in document.pages:
        lines.append(f"\n--- Page {page.number} ---")
        lines.append(page.text)

    return "\n".join(lines)


def main() -> None:
    manager = ReaderManager()
    manager.register(PDFReader())

    document = manager.read("samples/sample.pdf")

    total_images = sum(len(page.images) for page in document.pages)
    total_drawings = sum(len(page.drawings) for page in document.pages)

    print(f"Images    : {total_images}")
    print(f"Drawings  : {total_drawings}")

    pipeline = DocumentPipeline()
    result = pipeline.analyze(document)

    report = build_report(document, result)

    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"{Path(document.filename).stem}_analysis.txt"
    output_path.write_text(report, encoding="utf-8")

    # Print only a short summary to the terminal — the full report,
    # including every page's full text, is saved to a file instead.
    print("=" * 50)
    print(f"File      : {document.filename}")
    print(f"Type      : {document.file_type}")
    print(f"Pages     : {document.metadata.page_count}")
    print(f"Blocks    : {len(document.pages[0].text_blocks)}")
    print(f"Title     : {result.document.metadata.title}")
    print(f"Abstract  : {result.document.metadata.abstract}")

    if document.pages[0].text_blocks:
        block = document.pages[0].text_blocks[0]

    print("\nFirst Block")
    print("-" * 40)
    print(block.text)

    print("\nDetected sections:")
    if result.document.sections:
        for section in result.document.sections:
            print(
                f"  - {section.section_type} "
                f"(pages {section.start_page}-{section.end_page}, "
                f"confidence {section.confidence})"
            )
    else:
        print("  (none)")

    print("=" * 50)
    print(f"\nFull report saved to: {output_path}")


if __name__ == "__main__":
    main()