from sklearn import svm
import sets_creator
from result_producer import *

#data_set_files = ['features/forest_features.txt']
data_set_files = ['features/features_spam.txt', 'features/features_ham.txt']

data_sets = sets_creator.get_data(files = data_set_files, max_ex = 12500)

for gamma in [0.0001, 0.001, 0.01, 0.1]:
    for C in [1, 10, 100, 10000]:
        print "C = " + str(C)
        print "gamma = " + str(gamma)
        algo = svm.SVC(gamma=gamma, C=C)
        algo.fit(data_sets['training_set']['examples'], data_sets['training_set']['labels'])
        generate_results(algo, data_sets)
