from sklearn.ensemble import AdaBoostClassifier
import sets_creator
from result_producer import *

data_sets = sets_creator.get_data(ratio = 0.7, files = ['features/features_spam.txt', 'features/features_ham.txt'], max_ex = 12500)



algo = AdaBoostClassifier()
algo.fit(data_sets['training_set']['examples'], data_sets['training_set']['labels'])

generate_results(algo, data_sets)
