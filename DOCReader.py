'''
  DOCReader.py does following: 
		- extracts text from .docx format
		- return list of extracted sections
'''

import sys
import docx


CLAUSE_HEADER_PREFIX = "section"
CLAUSE_HEADER_PREFIX_LEN = 10


class DOCReader: 

	def __init__(self, filename):
		self.filename=filename  # path + filename
		self.doc = None
		self.sections = None
		self.__read__() # eager run

	def __read__(self): 
		try: 
			self.doc = docx.Document(self.filename)
			self.sections = [p.text.replace(u'\xa0', u' ') for p in self.doc.paragraphs if CLAUSE_HEADER_PREFIX in p.text.lower()]
		except: 
			print("Oh oh! something went wrong. Error:", sys.exc_info()[0])
			raise

	def get_sections(self):
		return self.sections

if __name__ == "__main__":
    pass