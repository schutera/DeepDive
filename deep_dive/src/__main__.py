# system/standard lib imports
import time
import math
import argparse

# 3rd party imports
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd
import tensorflow as tf

# internal modules imports
import generator

def normalize(samples):
    # potentially a task for the student to fill this one!
    min_value = samples.min()
    max_value = samples.max()
    print(f"normalizing values from interval <{min_value}, {max_value}>")
    new_max_value = max_value - min_value
    new_min_value = 0
    print(f"same interval, shifted into the positive domain <{new_min_value}, {new_max_value}>")
    new_samples = samples / new_max_value
    return new_samples

def hello_mnist():
    # Loading the MNIST dataset in one line
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    # Printing the shape
    print('x_train:', x_train.shape)
    print('y_train:', y_train.shape)
    print('x_test:', x_test.shape)
    print('y_test:', y_test.shape)

    # Plotting data samples
    print('\n Plot of the first 25 samples in the MNIST training set')
    numbers_to_display = 25
    num_cells = math.ceil(math.sqrt(numbers_to_display))
    plt.figure(figsize=(10,10))
    for i in range(numbers_to_display):
        plt.subplot(num_cells, num_cells, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(x_train[i], cmap=plt.cm.binary)
        plt.xlabel(y_train[i])
    plt.show()

    normalize(x_train)

    x_train_normalized = x_train/255 
    x_test_normalized = x_test/255 

    # in the next step, we also need to reshape our input to fit our input layer later on. 
    # This is due to keras expecting a definition for how many channels your input sample has, as we 
    # deal with gray scale this is 1.
    x_train= x_train_normalized.reshape(-1, 28, 28, 1)
    x_test = x_test_normalized.reshape(-1, 28, 28, 1)
    print('x_test:', x_test)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', help="Module of the course to run", choices=['hello_mnist'], type=str, required=True)
    args = parser.parse_args()

    modules = {
        "hello_mnist": hello_mnist
    }
    modules[args.module]()