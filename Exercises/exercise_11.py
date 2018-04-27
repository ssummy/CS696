"""Exercise 11 - sklearn and pickle

For this exercise you will be writing a class for several different generator functions.

1) Write a definition called "forest_predictor". This definition should:
    - accept one mandatory string argument, a string corresponding to the file path of the CSV file to be read
    - accept one mandatory integer argument, the column containing the classification values (0 based),
            this column should be removed from your training data and stored in its own list
    - accept **kwargs for the cases:
        - header = bool   -> if True: remove the first row after reading the CSV file
        - save = string   -> check if a file with the name exists, if so, load it with pickle and do not train
            a new classifier, if the file does not exist, train a classifier and save it to this location with pickle
        - test = 2d list  -> predict the classifications of this test data set and print the resulting list
    - always return the classifier object
    - check for **kwargs using kwargs.get() and default to False or None!
        EX: header_exists = kwargs.get('header', False)
        NOT: header_exists = kwargs['header']  # crashes if header was not specified"""

def forest_predictor(filePath, labelCol, **kwargs):
    s = kwargs
    header_exists = kwargs.get('header', False)
    save = kwargs.get('save', False)
    test = kwargs.get('test', False)

    # "I wish there was a way to save and load variables so I wouldn't have to train a new classifier every time"
    import pickle
    import os
    import scipy
    if os.path.exists(save):  # (item in os.listdir(self.saveSpot)):
        with open(save, 'rb') as infile:
            clf = pickle.load(infile)
    else:
        from sklearn.ensemble import RandomForestClassifier
        clf = RandomForestClassifier(n_estimators=500)
        with open(filePath, 'r') as infile:
            data = [line.replace('\n', '').split(',') for line in infile]

        #my_list2, my_list1 = map(list, zip(*data))
        y = []
        x = []
        #[x.append(filter(None, [item if not index == labelCol else y.append(item) for index, item in enumerate(column)])) for column in data]
        #new_x = [[i for i in column if not i is None] for column in x]
        x = [[item for index, item in enumerate(column) if not index == labelCol] for column in data][1:]
        [[y.append(item) for index, item in enumerate(column) if index == labelCol] for column in data[1:]]
        clf = clf.fit(x, y)
        with open(save, 'wb') as outfile:
            pickle.dump(clf, outfile)
    print(clf.predict(test))

    return clf


if __name__ == '__main__':
    #This example uses the training and testing data from lecture_11, a 'large_dataset.csv' is also available, but not required
    clf = forest_predictor('test_files/simple_data.csv', 2, header=True, save='saves/random_forest.p', test=[[15,0], [18,60000], [80,30000]])
    # should print ['0', '1', '1'] and return the classifier so that feature_importances_ can be printed
    print(clf.feature_importances_)