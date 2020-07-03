# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import tensorflow_hub as hub
# import tensorflow_datasets as tfds

# print("Version: ", tf.__version__)
# print("Eager mode: ", tf.executing_eagerly())
# print("Hub version: ", hub.__version__)
# print("GPU is", "available" if tf.config.experimental.list_physical_devices(
#     "GPU") else "NOT AVAILABLE")

# --------------------------------------------------------------
# Importing dataset using pandas dataframe
# --------------------------------------------------------------
df = pd.read_csv("fake_or_real_news.csv")

# Print first lines of `df`
df.head()
