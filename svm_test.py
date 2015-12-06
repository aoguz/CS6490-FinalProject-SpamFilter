from sklearn import svm
import sets_creator
from result_producer import *

data_sets = sets_creator.get_data(files = ['features/forest_features.txt'])

algo = svm.SVC(gamma=0.01, C=100)
algo.fit(data_sets['training_set']['examples'], data_sets['training_set']['labels'])

generate_results(algo, data_sets)
