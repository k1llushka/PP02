from app.ocr_wrapper import recognize_document

text = recognize_document("documents/TEST.jpg")

print(text)
