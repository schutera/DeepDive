# system/standard lib imports
import time
import math

# 3rd party imports
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd
import tensorflow as tf

# internal modules imports
import generator


if __name__ == "__main__":
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