import pandas as pd
import numpy as np
import copy


np.random.seed(7)

# input X: m * n numpy array
# input k: # of centers

def check_converge(center_cur, center_lag, epson):
    matrix = center_cur - center_lag
    distance = np.linalg.norm(matrix, ord=None, axis=1)
    max_dist = np.max(distance)
    is_converge = (max_dist < epson)
    return max_dist, is_converge

def get_initial_centers(X, k):
    '''
    args
        X: numpy.narray n*D
        k: int

    returns
        numpy.narray k*D
    '''
    n_sample = X.shape[0]
    center_ids = np.random.choice(n_sample, k, False)
    center_array = X[center_ids]
    center_array = np.unique(center_array, axis=0)
    n_unique = center_array.shape[0]
    while n_unique < k:
        makeup_center_ids = np.random.choice(n_sample, k - n_unique, False)
        makeup_center_array = X[makeup_center_ids]
        center_array = np.vstack((center_array, makeup_center_array))
        center_array = np.unique(center_array, axis=0) # unique rows
        n_unique = center_array.shape[0]
    return center_array

def assign_center(n_sample, X, center_array, center_idx):
    for i in range(n_sample):
        obs = X[i]
        distance_array = [np.linalg.norm(obs-center) for center in center_array]
        min_center_idx = np.argmin(distance_array)
        center_idx[i] = min_center_idx
    return

def update_center(X, k, center_array, center_idx):
    for i in range(k):
        center_array[i] = np.mean(X[center_idx == i], axis=0)
    return

def kmeans_fit(X, k, max_it, epson):

    center_array = get_initial_centers(X, k)
    is_converge = False
    it = 0
    n_sample = X.shape[0]
    center_idx = np.zeros(n_sample, dtype=int)
    while it < max_it and not is_converge:
        # assign the points to the clusters 
        # calculate the distance from each point to each center, choose the nearest center
        center_array_lag = copy.deepcopy(center_array)
        assign_center(n_sample, X, center_array, center_idx)
        
        # update the clusters
        update_center(X, k, center_array, center_idx)
        it+=1
        max_distance, is_converge = check_converge(center_array, center_array_lag, epson)
        print(max_distance)
    return (center_idx, center_array)


X = np.random.rand(100,5)
k = 3
epson = 0.01
n_iter = 20
cluster_idx, center_array = kmeans_fit(X, k,  n_iter, epson)

print(center_array)