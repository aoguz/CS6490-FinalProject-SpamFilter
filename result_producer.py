
def generate_results(algo, data_sets):
    mistakes_num = 0
    prediction_vec = []
    for i, el in enumerate(data_sets['test_set']['examples']):
        prediction = algo.predict(el)[0]
        prediction_vec.append(prediction)
        actual     = data_sets['test_set']['labels'][i]

        if prediction != actual:
            mistakes_num += 1
        #print 'prediction ' + str(prediction)
        #print 'actual '     + str(actual)
    print "accuracy: " + str(float(len(data_sets['test_set']['examples']) - mistakes_num) / float(len(data_sets['test_set']['examples'])))
    return prediction_vec
