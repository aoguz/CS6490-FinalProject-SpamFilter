from email_iter import *
import re

#bag-of-words feature extractor
class feature_extractor:
    def __init__(self, features_filename):
        #features should be a list of strings
        self.features = self.load_features(features_filename)

    #loads a list of features from a provided filename
    def load_features(self, filename):
        result = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                result.append(line.strip())
        print result
        return result

    #is_spam is a boolean that indicates whether 
    #the provided email_terator corresponds to spam or ham
    #when count is True, the number of a particular word as used in the feature vec
    #else element in feature vec is set to 1 if word exists, else 0
    def extract(self, email_iterator, output_file, is_spam, count = False):
        with open(output_file, 'w') as f:
            for email in email_iterator: 
                feature_vec = [0.0]*len(self.features)
                for i in range(len(self.features)):
                     if count:
                        feature_vec[i] = float(len(re.findall(r"[^a-z]"+ self.features[i] + "[^a-z]", email.lower())))
                     elif self.features[i] in email.lower():
                        feature_vec[i] = 1.0
                f.write(str(feature_vec + [(1.0 if is_spam else -1.0)]) + "\n")

f      = feature_extractor('features/features.txt')
e_ham  = email_iter('enron1/ham')
e_spam = email_iter('enron1/spam')
f.extract(e_ham, 'features/features_ham.txt', False, count = True)
f.extract(e_spam, 'features/features_spam.txt', True, count = True)
