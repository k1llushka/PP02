import os

from rdoc.RussianDocsOCR.russian_docs_ocr.document_processing.pipeline.pipeline import Pipeline
from app.logger import log

pipeline = Pipeline()


def recognize_document(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError("Файл не найден")

    result = pipeline(file_path)

    try:
        if hasattr(result, "ocr") and isinstance(result.ocr, dict):
            texts = []

            for v in result.ocr.values():
                if isinstance(v, str) and v.strip():
                    texts.append(v)

                if isinstance(v, dict):
                    for sub in v.values():
                        if isinstance(sub, str) and sub.strip():
                            texts.append(sub)

            if texts:
                return "\n".join(texts)

        return repr(result)

    except Exception:
        return repr(result)

    log(f"OCR обработал файл: {file_path}")