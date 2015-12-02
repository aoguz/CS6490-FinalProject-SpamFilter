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
def get_data(ratio = 0.5):
    '''
    returns data in following format
    {
        'test_set':
            {
                'examples': [[feature1, feature2, ...],[feature1, feature2, ...], ...]
            }
        'training_set:
            {
                'examples': [[feature1, feature2, ...],[feature1, feature2, ...], ...]
                'labels'  : [label1, label2, ...]
            } 
    }
    '''
    #max number of examples to use from each file
    max_ex = 2
    ham_list  = load_raw(ham_filename, max_ex)  
    spam_list = load_raw(spam_filename, max_ex)
    all_examples = ham_list
    all_examples.extend(spam_list)
    random.shuffle(all_examples)
    len_training_set = int(float(len(all_examples)) * ratio)
    training_set    = [all_examples[i][:-1] for i in range(0,len_training_set)]
    training_labels = [all_examples[i][-1]  for i in range(0,len_training_set)]
    test_set        = [all_examples[i][:-1] for i in range(len_training_set,len(all_examples))]
    
    return {
                'test_set':
                    {
                        'examples': test_set
                    },
                'training_set':
                    {
                        'examples': training_set,
                        'labels'  : training_labels
                    } 
            }

print get_data()
