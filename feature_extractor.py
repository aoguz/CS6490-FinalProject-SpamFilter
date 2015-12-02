from email_iter import *

#bag-of-words feature extractor
class feature_extractor:
    def __init__(self, features):
        #features should be a list of strings
        self.features = features

    #is_spam is a boolean that indicates whether 
    #the provided email_terator corresponds to spam or ham
    def extract(self, email_iterator, output_file, is_spam):
        with open(output_file, 'w') as f:
            for email in email_iterator: 
                feature_vec = [0.0]*len(self.features)
                for i in range(len(self.features)):
                    if " " + self.features[i] + " " in email.lower():
                        feature_vec[i] = 1.0
                f.write(str(feature_vec + [(1.0 if is_spam else 0.0)]) + "\n")
features = ['free', 
            'unsubscribe', 
            'news', 
            'won', 
            'winner', 
			'viagra',
			'sex', 
			'milf', 
			'fuck',
			'toy', 
			'bigger', 
			'desperate',
			'single',
			'miles',
			'tonight',
			'immigration',
			'gratz',
			'blessed']
'''
features = ['free', 
            'unsubscribe', 
            'news', 
            'won', 
            'winner']'''
f = feature_extractor(features)
e_ham = email_iter('enron1/ham')
e_spam = email_iter('enron1/spam')
f.extract(e_ham, 'features/features_ham.txt', False)
f.extract(e_spam, 'features/features_spam.txt', True)
