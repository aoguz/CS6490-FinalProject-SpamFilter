from sklearn import svm
import sets_creator

data_sets = sets_creator.get_data()

algo = svm.SVC(gamma=0.01, C=100)
algo.fit(data_sets['training_set']['examples'], data_sets['training_set']['labels'])

mistakes_num = 0
for i, el in enumerate(data_sets['test_set']['examples']):
    prediction = algo.predict(el)
    actual     = data_sets['test_set']['labels'][i]

    if prediction != actual:
        mistakes_num += 1
    print 'prediction ' + str(prediction)
    print 'actual '     + str(actual)
print "accuracy: " + str(float(len(data_sets['test_set']['examples']) - mistakes_num) / float(len(data_sets['test_set']['examples'])))
