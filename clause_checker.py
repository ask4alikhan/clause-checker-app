#!/usr/bin/python3
'''
	clause-checker-app is a proto-type built to extract legal clauses 
	(having 'Section' headers) from couple of documents (formats: 
	docx/pdf/images/* supported by python-docx, pytessaract)  & run 
	predictions on simlar clauses (using Siamese-LSTM), trained using 
	'Quora Question Pairs' dataset & achieved 85% accuracy.

	how to run: 
    	$ python3 clause_checker.py 
			-b './data/input/kobe-sett-2001-04-27-shtml-file_html.docx' 
			-d './data/input/kobe-sett-kk-2001-04-27-shtml-file_html.docx'

	assumptions: 
		a. Comparing only clauses in 'Section' headers
		b. Sections present on both documents 
		   (currently missing sections not handled)

	suggested enhancements: 
		a. Train ML model with actual legal clauses to improve legal clause 
		smilarity accuracy. This will help with both extracting clauses 
		& predicting simlarities
		b. Provide UI / Webservices to invoke this from anywhere.
		c. Need to add another layer to track all referential legal clauses 
		as a base & probably add search engine capabilities 
		(using Elasticsearch/Solr)

	tech debt: 
		a. text extraction bit is fragile & buggy, needs to be optimized
		b. Move this to Docker/Cloud implementation
		c. Add Configurations (paths, constants & likes)
		d. Code modularizations
		e. Add Test Coverage

	results:  
	w/ Dandelion sentence simlarity results: 

	w/ this model achieved 85% accuracy:  

	Mention about you checked with your app & Dandelion APIs
  	85% accuracy on my proto-type.

	references: 
		a. Siamese LSTM for evaluating semantic similarity between sentences 
		of the Quora Question Pairs Dataset.
		   https://github.com/likejazz/Siamese-LSTM 
'''

import sys
import getopt


from DOCReader import DOCReader
from predict import Predict


def main(argv):

	# get base & to_diff filenames
	base_file, diff_file = get_filenames(argv)

	# get doc-readers for the 2 files...
	base_doc = DOCReader(base_file)
	diff_doc = DOCReader(diff_file)

	# process the sections into hash
	base_doc_sections_map = {}
	diff_doc_sections_map = {}

	for para in base_doc.sections: 
		para = para.strip()
		k = (para[:11]).strip()
		base_doc_sections_map[k] = para

	for para in diff_doc.sections: 
		para = para.strip()
		k = (para[:11]).strip()
		diff_doc_sections_map[k] = para

	# IMP BITs...
	# for k in base_doc_sections_map.keys(): 
	#   # print(base_doc_sections_map[k])
	#   # print("key:{}; baseSection:{}; diffSection:{}".format(k,base_doc_sections_map[k], diff_doc_sections_map[k]))
	#   logging.debug("key:{}; \nbaseSection:{}; \ndiffSection:{}".format(k,base_doc_sections_map[k], diff_doc_sections_map[k]))

	# zip 2 files sections
	zippedClauses = list(zip(base_doc_sections_map.keys(), base_doc_sections_map.values(), diff_doc_sections_map.values()))
	
	# call the predictor
	pred = Predict(zippedClauses)
	results = pred.run()
	for res in results: 
		print(res)
  
def get_filenames(argv): 
	USAGE = 'usage: clause_checker.py -b <base_file> -d <diff_file>'
	base = None
	diff = None

	try:
		opts, args = getopt.getopt(argv,"b:d:",["base=","diff="])
	except getopt.GetoptError:
		print(USAGE)
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print(USAGE)
			sys.exit()
		elif opt in ("-b", "--base"):
			base = arg
		elif opt in ("-d", "--diff"):
			diff = arg

	if not base or not diff:
		print(USAGE)
		sys.exit()   

	return base, diff

if __name__ == "__main__":
   main(sys.argv[1:])