from sklearn.metrics import classification_report

def generate_results(algo, data_sets):
    prediction_vec = []
    for i, el in enumerate(data_sets['test_set']['examples']):
        prediction = algo.predict(el)[0]
        prediction_vec.append(prediction)
        actual     = data_sets['test_set']['labels'][i]
    print classification_report(data_sets['test_set']['labels'], prediction_vec)
    return prediction_vec
