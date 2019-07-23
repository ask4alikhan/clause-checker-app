import io
from PIL import Image
import pytesseract
from wand.image import Image as wi

base_pdf = wi(filename = "./data/input/kobe-sett-2001-04-27-shtml-file_.pdf", resolution = 500)
# to_validate_pdf = wi(filename = "./data/input/kobe-sett-kk-2001-04-27-shtml-file_.pdf", resolution = 300)


pdfImage_base = base_pdf.convert('jpeg')

imageBlobs = []

for img in pdfImage_base.sequence:
	imgPage = wi(image = img)
	imageBlobs.append(imgPage.make_blob('jpeg'))

recognized_text = []

for imgBlob in imageBlobs:
	im = Image.open(io.BytesIO(imgBlob))
	im = im.convert('L')
	text = pytesseract.image_to_string(im, lang = 'eng')
	recognized_text.append(text)

print(recognized_text)

# text = textract.process('kobe-sett-2001-04-27-shtml-file_.pdf')