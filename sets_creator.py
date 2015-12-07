import ast
import random

spam_filename = "features/features_ham.txt"
ham_filename  = "features/features_spam.txt"

#max_ex corresponds to the max number of example to extract
def load_raw(filename, max_ex):
    raw_data = []
    ex_count = 0
    with open(filename, 'r') as f:
        for el in f.readlines():
            if ex_count < max_ex:
                el_list = ast.literal_eval(el)
                raw_data.append(el_list)
            else:
                break
            ex_count += 1
    return raw_data


#ratio indicates the proportion of data in the training set vs the test set
#files represents which files to get the raw features from. These examples are shuffled together
#max_ex is the max number of examples to use from each file
def get_data(ratio = 0.5, files = [], max_ex = 1500):
    '''
    returns data in following format
    {
        'test_set':
            {
                'examples': [[feature1, feature2, ...],[feature1, feature2, ...], ...]
                'labels'  : [label1, label2, ...]
            }
        'training_set:
            {
                'examples': [[feature1, feature2, ...],[feature1, feature2, ...], ...]
                'labels'  : [label1, label2, ...]
            } 
    }
    '''
    all_examples = []
    for filename in files:
        all_examples.extend(load_raw(filename, max_ex))
    random.shuffle(all_examples)
    len_training_set = int(float(len(all_examples)) * ratio)
    training_set     = [all_examples[i][:-1] for i in range(0,len_training_set)]
    training_labels  = [all_examples[i][-1]  for i in range(0,len_training_set)]
    test_set         = [all_examples[i][:-1] for i in range(len_training_set,len(all_examples))]
    test_labels      = [all_examples[i][-1]  for i in range(len_training_set, len(all_examples))]
    
    return {
                'test_set':
                    {
                        'examples': test_set,
                        'labels'  : test_labels
                    },
                'training_set':
                    {
                        'examples': training_set,
                        'labels'  : training_labels
                    } 
            }
