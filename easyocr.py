import easyocr as ocr  #OCR

reader = ocr.Reader(['en'],model_storage_directory='.')

result = reader.readtext("/home/rohit/Pictures/license.jpeg")

for text in result:
    print(text[1])