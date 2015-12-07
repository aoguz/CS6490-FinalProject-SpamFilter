from sklearn.tree import DecisionTreeClassifier
import sets_creator
from result_producer import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score

num_trees = 15

features_filename = 'features/forest_features.txt'

data_sets = sets_creator.get_data(files = ['features/features_spam.txt', 'features/features_ham.txt'], max_ex = 12500)

def write_features(filename, predictions, labels):
    with open(filename, 'w') as f:
        for i in range(len(predictions)):
            f.write(str(predictions[i] + [labels[i]])  + '\n')

#predictions is a matrix of precitions
def transpose(predictions):
    return map(list, zip(*predictions))

def random_forest():
    algo = RandomForestClassifier(n_estimators=num_trees, min_samples_split=2)
    algo.fit(data_sets['training_set']['examples'], data_sets['training_set']['labels'])
    generate_results(algo, data_sets)

def generate_forest():
    prediction_mat = []
    for i in range(num_trees):
        algo = DecisionTreeClassifier(random_state = None, max_depth = 10, splitter='random', min_samples_split=1)
        algo.fit(data_sets['training_set']['examples'], data_sets['training_set']['labels'])
        prediction_mat.append(generate_results(algo, data_sets))
    prediction_mat = transpose(prediction_mat)
    return prediction_mat


predictions = generate_forest()
write_features(features_filename, predictions, data_sets['test_set']['labels'])

#random_forest()
