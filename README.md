# clause-checker-app # 
  is a proto-type built to extract legal clauses (having 'Section' headers) from couple of documents 
  (formats: docx/pdf/images/* supported by python-docx, pytessaract) & run predictions on simlar clauses 
  (using Siamese-LSTM), trained using 'Quora Question Pairs' dataset & achieved 82% accuracy	

# how to run #
  $ python3 clause_checker.py 
	-b './data/input/kobe-sett-2001-04-27-shtml-file_html.docx' 
	-d './data/input/kobe-sett-kk-2001-04-27-shtml-file_html.docx'

# assumptions #
  a. Comparing only clauses in 'Section' headers
  b. Sections present on both documents 
     (currently missing sections not handled)

# suggested enhancements #
  a. Train ML model with actual legal clauses to improve legal clause smilarity accuracy. This will help with both extracting clauses & predicting simlarities
  b. Provide UI / Webservices to invoke this from anywhere.
  c. Need to add another layer to track all referential legal clauses as a base & probably add search engine capabilities (using Elasticsearch/Solr)
  d. tech debt: 
    - text extraction bit is fragile & buggy, needs to be optimized
    - Move this to Docker/Cloud implementation
    - Add Configurations (paths, constants & likes)
    - Code modularizations
    - Add Test Coverage

# results #
# this model achieved 8% accuracy:  
# with twinword Text Simlarity results for Section-2: 
# with Dandelion sentence simlarity results for Section-1: 


# references #
  a. Siamese LSTM for evaluating semantic similarity between sentences of the Quora Question Pairs Dataset.
    https://github.com/likejazz/Siamese-LSTM
      
