print("===================")
print("==  SYSTEM INFO  ==")
print("===================")
print()

import os
import platform
import socket

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "4"

import keras
import tensorflow as tf
import pandas as pd
import numpy as np

print("OS:", platform.platform())
print("IP:", socket.gethostbyname(socket.gethostname()))

gpus = tf.config.list_physical_devices("GPU")
if len(gpus) < 1:
    print("GPU: No GPU available!")
else:
    print("Num GPU available:", len(gpus))
    os.system("nvidia-smi -L")

print()
print("===================")
print("== ML/AI MODULES ==")
print("===================")
print()

print("TF version:", tf.__version__)
print("Keras version:", keras.__version__)
print("Pandas version:", pd.__version__)
print("Numpy version:", np.__version__)

print()

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "0"