# clause-checker-app
  Is a proto-type built to extract legal clauses (having 'Section' headers) from couple of documents 
  (formats: docx/pdf/images/* supported by python-docx, pytessaract) & run predictions on simlar clauses 
  (using Siamese-LSTM), trained using 'Quora Question Pairs' dataset & achieved 82% accuracy	

### how to run
```shellscript
$ python3 clause_checker.py 
    -b './data/input/kobe-sett-2001-04-27-shtml-file_html.docx'
    -d './data/input/kobe-sett-kk-2001-04-27-shtml-file_html.docx'
```
### assumptions
* Comparing only clauses in 'Section' headers
* Sections should be present on both documents, currently missing sections not handled
     
### suggested enhancements
* Training the Siamese-LSTM model with legal clauses will improve prediction accuracy. This will also help with both extracting the clauses (from documents) & predicting simlarities.
* Provide UI / Webservices to invoke this from anywhere.
* Need to add another layer to track all referential legal clauses as a base & probably add search engine capabilities (using Elasticsearch/Solr)
* tech debt: 
    - text extraction bit is fragile & buggy, needs to be optimized
    - Move this to Docker/Cloud implementation
    - Add Configurations (paths, constants & likes)
    - Code modularizations
    - Add Test Coverage

### references 
* [Siamese LSTM](https://github.com/likejazz/Siamese-LSTM) for evaluating semantic similarity between sentences of the Quora Question Pairs Dataset.

## results with this app ##
* **Actual:** Compared two legal documents (.docx) with four sections & only Section-2 had differing clause. 
* **Prediction:** Below is the 'extract-text => predict' run for a model thats trained on Quora Questions data-set.
![one](../master/images/clause-predict-app-run1.png)
![one](../master/images/clause-predict-app-run2.png)

## [twinword](https://www.twinword.com/api/text-similarity.php) Text Simlarity app prediction for Section-2##
![one](../master/images/twinword_section2.png)

## [dandelion](https://dandelion.eu) Sentence Simlarity app prediction for Section-1##
![one](../master/images/Dandelion_TextSimilarity.png)
