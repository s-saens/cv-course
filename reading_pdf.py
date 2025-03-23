import fitz  # PyMuPDF
import numpy as np
import cv2

# PDF 열기
pdfName = "MercadanteFluteConcerto.pdf"
doc = fitz.open(pdfName)

page_index = 0

while True:
    page: fitz.Page = doc[page_index]
    pix = fitz.Page.get_pixmap(page)

    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)  # n은 채널 수

    if pix.n == 3:  # RGB
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    cv2.imshow(pdfName, img)

    key = cv2.waitKey(0)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('a'):
        page_index -= 1
        if page_index < 0:
            page_index = len(doc) - 1
    elif key & 0xFF == ord('d'):
        page_index = (page_index + 1) % len(doc)

doc.close()
cv2.destroyAllWindows()