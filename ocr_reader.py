'''
	THIS IS A WIP/INCOMPLETE file,was having issues extracting, REGEX 
	are ready but need to be plugged in to reader for text extraction.
	
	ocr_reader.py does following: 
		- pick any format document & extract legal clauses (ex: sections)
		- return list of extracted text

	BUILT REGEX: 
		This fetches the sections 
			=> (Section.*?\\n\\n)
		This fetches before + all sections w/positive lookahead
			=> .*?(?=(Section.*?\\n\\n))
		This fetches the after sections bit 
			=> \\n\\n\[.* \\n\\n\[.*						
'''

import io
import pytesseract
from PIL import Image
from wand.image import Image as wi


base_pdf = 	wi(filename = "./data/input/kobe-sett-2001-04-27-shtml-file_.pdf", 
				resolution = 500
			)
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
