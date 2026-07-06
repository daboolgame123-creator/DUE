import shutil
import tempfile
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse

from pipeline.document_pipeline import DocumentPipeline
from readers.reader_manager import ReaderManager
from readers.pdf_reader import PDFReader

app = FastAPI(title="Intelligent Document Intelligence Engine")

UI_INDEX_PATH = Path(__file__).parent / "ui" / "index.html"


def build_reader_manager() -> ReaderManager:
    """Builds a ReaderManager with every supported reader registered.

    Only PDFReader exists for now — more readers will be registered
    here as they are built (Word, PowerPoint, Excel...).
    """
    manager = ReaderManager()
    manager.register(PDFReader())
    return manager


@app.get("/", response_class=HTMLResponse)
def index() -> HTMLResponse:
    html_content = UI_INDEX_PATH.read_text(encoding="utf-8")
    return HTMLResponse(content=html_content, media_type="text/html; charset=utf-8")


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)) -> JSONResponse:
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="يرجى رفع ملف PDF فقط في هذه المرحلة.")

    suffix = Path(file.filename).suffix or ".pdf"

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        shutil.copyfileobj(file.file, tmp_file)
        tmp_path = Path(tmp_file.name)

    try:
        manager = build_reader_manager()
        document = manager.read(str(tmp_path))

        pipeline = DocumentPipeline()
        result = pipeline.analyze(document)

        response_data = {
            "filename": file.filename,
            "file_type": document.file_type,
            "page_count": document.metadata.page_count,
            "title": result.document.metadata.title,
            "author": result.document.metadata.author,
            "university": result.document.metadata.university,
            "department": result.document.metadata.department,
            "abstract": result.document.metadata.abstract,
            "sections": [
                {
                    "type": section.section_type,
                    "start_page": section.start_page,
                    "end_page": section.end_page,
                    "confidence": section.confidence,
                }
                for section in result.document.sections
            ],
        }
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    finally:
        tmp_path.unlink(missing_ok=True)

    return JSONResponse(response_data)