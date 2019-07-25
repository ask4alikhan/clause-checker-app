# clause-checker-app
  Is a proto-type built to diff legal clauses (having 'Section' headers) from input of two documents 
  (formats: docx/pdf/images/* supported by python-docx, pytessaract) & run predictions on simlar clauses 
  (using Siamese-LSTM), trained this model using 'Quora Question Pairs' dataset of about 350K rows & achieved 82% accuracy	

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
- Paper, Articles
    - [Siamese Recurrent Architectures for Learning Sentence Similarity](http://people.csail.mit.edu/jonasmueller/info/MuellerThyagarajan_AAAI16.pdf)
    - [How to predict Quora Question Pairs using Siamese Manhattan LSTM](https://medium.com/mlreview/implementing-malstm-on-kaggles-quora-question-pairs-competition-8b31b0b16a07)
    - [Medium: Text Similarity](https://medium.com/@adriensieg/text-similarities-da019229c894)
	- [Kaggle Quora Question Pairs Script](https://www.kaggle.com/lamdang/dl-models)
	- [Legal Document Retrival Paper](https://arxiv.org/pdf/1805.10685.pdf)
	- [PyData Amsterdam 2017: Siamese LSTM in Keras](https://www.youtube.com/watch?v=SWjIoRNTCdU)
	- [Duplicate Question Detection with Deep Learning on Quora Dataset](http://www.erogol.com/duplicate-question-detection-deep-learning/)
- Data
    - [GoogleNews-vectors-negative300.bin.gz](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing)
    - [Kaggle's Quora Question Pairs Dataset](https://www.kaggle.com/c/quora-question-pairs/data)
- References
	- [likejazz/Siamese-LSTM](https://github.com/likejazz/Siamese-LSTM)
    - [aditya1503/Siamese-LSTM](https://github.com/aditya1503/Siamese-LSTM)
    - [dhwajraj/deep-siamese-text-similarity](https://github.com/dhwajraj/deep-siamese-text-similarity)
    - [nikhilkumarsingh/tesseract-python](https://github.com/nikhilkumarsingh/tesseract-python)
    - [Dandelion API: Text Similarity](https://dandelion.eu/semantic-text/text-similarity-demo/?text1=My+name+is+Theia+Khan&text2=My+name+is+Aedan+Ali+Khan&lang=auto&exec=true)
	- [Twinword API: Text Similarity](https://www.twinword.com)


## results with this app
* **Actual:** Compared two legal documents (.docx) with four sections & only Section-2 had differing clause. 
* **Prediction:** Below is the 'extract-text => predict' run for a model thats trained on Quora Questions data-set.
![one](../master/images/clause-predict-app-run1.png)
![one](../master/images/clause-predict-app-run2.png)

## [twinword](https://www.twinword.com/api/text-similarity.php) Text Simlarity app prediction for Section-2
![one](../master/images/twinword_section2.png)

## [dandelion](https://dandelion.eu) Sentence Simlarity app prediction for Section-1
![one](../master/images/Dandelion_TextSimilarity.png)
