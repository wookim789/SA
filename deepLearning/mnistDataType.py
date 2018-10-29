import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

print("")
print("")
print("=========================")
print(mnist.train.images[0].shape)
print("=========================")
print("")
print("")