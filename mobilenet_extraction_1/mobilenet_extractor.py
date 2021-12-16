import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.applications import imagenet_utils

tf.keras.applications.mobilenet.MobileNet()

mobile = tf.keras.applications.mobilenet.MobileNet(
    input_shape=None,
    alpha=1.0,
    depth_multiplier=1,
    dropout=0.001,
    include_top=False,
    weights="imagenet",
    input_tensor=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
)

def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return tf.keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)

#img -> 1D feature array with length = 1024
def extractImage(img_path):
    preprocessed_image = prepare_image(img_path)
    feature = mobile.predict(preprocessed_image)[0][0][0]
    print(np.shape(feature))
    return feature / np.linalg.norm(feature)

from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
import numpy as np
from pathlib import Path
import os
from os import listdir


def extractAllImg(img_dir, feature_dir):
    for img_name in listdir(img_dir):
        print(img_name)  # e.g., ./static/img/xxx.jpg
        feature = extractImage(img_dir + img_name)
        img_name = os.path.splitext(img_name)[0] #remove .jpg or jpeg
        np.save(feature_dir + img_name, feature)

#loads features in an array
#loads img names in an array
def loadSavedFeatures(feature_dir):
    featureList = listdir(feature_dir)
    #print(featureList)
    numberOfFeatures = len(featureList)
    features = []
    img_paths = []

    for i in range(numberOfFeatures):
        img_name = featureList[i]
        feature_path = os.path.join(feature_dir, img_name)
        feature = np.load(feature_path)
        
        features.append(feature) #save feature at position i
        img_paths.append("./static/images/" + os.path.splitext(img_name)[0] + ".jpg") #save img path at position i 
        
    return features, img_paths

def compareImages(img_feature, feature_dir):
    features, img_paths = loadSavedFeatures(feature_dir)

    dists = np.linalg.norm(features-img_feature, axis=1) #L2 distances to the features    
    ids = np.argsort(dists)[:15] #top 15 resulsts --> should give back which indices are the best 
    print(np.shape(ids))

    scores = [(dists[id], img_paths[id]) for id in ids]
    return scores


if __name__ == "__main__":

    img_dir = "./static/images/"
    feature_dir = "./static/features/"

    #extractAllImg(img_dir, feature_dir)

    samplequery = extractImage(img_dir + "horse22.jpg")

    list = compareImages(samplequery, feature_dir)
    print(list)
