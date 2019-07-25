'''
	predicty.py does following: 
		- Predicts sentence simlarity based on trained model stored in 
		  <filename>.h5 file.
		- Returns zip of Section + Result				
'''

import pandas as pd
import tensorflow as tf


from util import make_w2v_embeddings, split_and_zero_padding, ManDist


class Predict(object):

	def __init__(self, clauses, *args, **kwargs):
		self.clauses = clauses

	def run(self): 
		clause_df = pd.DataFrame(self.clauses)
		print("after:::", clause_df.head(5))

		# change column headers, for processing by Siamese-LSTM 
		clause_df.columns = ['no', 'question1', 'question2'] 
		for q in ['question1', 'question2']:
			clause_df[q + '_n'] = clause_df[q]

		# Make word2vec embeddings
		embedding_dim = 300
		max_seq_length = 20
		clause_df, embeddings = make_w2v_embeddings(clause_df, 
					embedding_dim=embedding_dim, empty_w2v=False
				)

		# Split to dicts and append zero padding.
		X_test = split_and_zero_padding(clause_df, max_seq_length)

		# Make sure everything is ok
		assert X_test['left'].shape == X_test['right'].shape

		model = tf.keras.models.load_model('./data/keras_model/SiameseLSTM.h5', 
					custom_objects={'ManDist': ManDist}
				)
		model.summary()

		# prediction = model.predict([X_test['left'], X_test['right']])
		prediction = model.predict([X_test['left'], X_test['right']], verbose=1)
		print(prediction)

		# zip section header w/ model-prediction, Ex: 'Section 1 : 0.54'
		result = zip([x[0] for x in self.clauses], prediction.tolist())
		
		return result
