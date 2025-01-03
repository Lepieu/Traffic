import cv2
import numpy as np
import os
import sys
import tensorflow as tf
import keras

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]: 
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])


    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    images = list()
    labels = list()
    for category in range(NUM_CATEGORIES):
        directory = os.path.join(sys.path[0], data_dir, str(category))
        for imgFile in os.listdir(directory):
            img = cv2.resize( 
                cv2.imread(os.path.join(directory, imgFile)), #load current image as an N dimensional array of its normal size
                (IMG_WIDTH, IMG_HEIGHT) #standardize size to IMG_WIDTH, IMG_HEIGHT
            )
            images.append(img)
            labels.append(category)
    
    return (images, labels)
    raise NotImplementedError


def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    model = keras.models.Sequential([
        keras.layers.Conv2D(64, (3,3), activation="relu", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
        keras.layers.MaxPool2D(),
        keras.layers.Flatten(),
        keras.layers.Dense(512, activation="relu"),
        keras.layers.Dropout(0.5),
        
        keras.layers.Dense(43, activation="softmax")
    ])
    model.compile(optimizer="adam",
                  loss="categorical_crossentropy",
                  metrics=["accuracy"])
    return model
    
    
    raise NotImplementedError


if __name__ == "__main__":
    main()
