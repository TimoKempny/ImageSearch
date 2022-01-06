import pyflann
import numpy as np
import mobilenet_extractor as mobile
import time

def similiarImgPaths(query_vector, feature_dir):
    features, img_paths = mobile.loadSavedFeatures(feature_dir)

    dataset = np.array(features, dtype=np.float32)

    flann = pyflann.FLANN()
    pyflann.set_distance_type("chi_square")
    # according to the dataset and desired precision a NN search algorithm will be automatically chosen.
    # available algorithm: linear(brute force), KD-tree, kmeans, composite(mix of kd-tree and kmeans)
    # results, dists = flann.nn(dataset, query_vec, 10, target_precision=0.6, algorithm="autotuned", memory_weight=0)
    results, dists = flann.nn(dataset, query_vector, 10, algorithm="kmeans",branching=16, iteration=5)
    '''
     results: indexes of vectors in dataset
     dists: list of distances between query vector and vectors in dataset. The shortest distance will be stored
               at the top of the list
     Default distance function: euclidean distance
    '''

    similar_img_paths = [(dists[0][i], img_paths[results[0][i]]) for i in range(len(results[0]))]

    return similar_img_paths

if __name__ == "__main__":
    img_dir = "./static/images/cifar10_200/"
    feature_dir = "./static/features/m_features/cifar10_200"

    query_vec = mobile.extractImage(img_dir + "airplane40.jpg")
    start = time.time()
    print(similiarImgPaths(query_vec, feature_dir))
    end = time.time()
    print("runtime using kmeans:" + str(end-start))





