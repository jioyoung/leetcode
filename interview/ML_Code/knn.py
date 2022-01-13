import numpy as np

def KNN_classifier(k, x_test, x_train, y_train):
    # y_train has values 0,1,2,...k-1 if there are k classes
    # y_train is one dimensional numpy array
    y_train = y_train.reshape(-1)
    train_data = x_train.reshape(-1,x_test.shape[1])
    num_test = x_test.shape[0]
    y_predict = np.zeros(num_test, dtype=y_train.dtype)
    for i in range(num_test):
        instance = x_test[i]
        diff = train_data - instance
        distance_arr = np.linalg.norm(diff, axis = 1)
        nearest_k_index = np.argpartition(distance_arr, k-1)[:k]
        votes = y_train[nearest_k_index]
        y_predict[i] = np.argmax(np.bincount(votes))
    return y_predict

def accuracy(y_predict, y_test):
    acc = np.sum(y_predict == y_test)/y_predict.shape[0]
    return acc