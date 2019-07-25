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

### Prerequisite
- Paper, Articles
    - [Siamese Recurrent Architectures for Learning Sentence Similarity](http://www.mit.edu/~jonasm/info/MuellerThyagarajan_AAAI16.pdf)
    - [How to predict Quora Question Pairs using Siamese Manhattan LSTM](https://medium.com/mlreview/implementing-malstm-on-kaggles-quora-question-pairs-competition-8b31b0b16a07)
- Data
    - [GoogleNews-vectors-negative300.bin.gz](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing)
    - [Kaggle's Quora Question Pairs Dataset](https://www.kaggle.com/c/quora-question-pairs/data)
- References
    - [aditya1503/Siamese-LSTM](https://github.com/aditya1503/Siamese-LSTM) Original author's GitHub
    - [dhwajraj/deep-siamese-text-similarity](https://github.com/dhwajraj/deep-siamese-text-similarity) TensorFlow based implementation

#### references #### 
  a. [Siamese LSTM](https://github.com/likejazz/Siamese-LSTM) for evaluating semantic similarity between sentences of the Quora Question Pairs Dataset.

### results
#### with this app: ####
* Actual: Compared two legal documents (.docx) with four sections & only Section-2 had differing clause. 
* Prediction: Below is the 'extract-text => predict' run for a model thats trained on Quora Questions data-set.
![one](../master/src/images/clause-predict-app-run1.png)
![one](../master/src/images/clause-predict-app-run2.png)

#### with twinword Text Simlarity app #### 
* results for Section-2
![one](../master/src/images/twinword_section2.png)

#### with Dandelion Sentence Simlarity app ####  
* results for Section-1 
![one](../master/src/images/Dandelion_TextSimilarity.png)
