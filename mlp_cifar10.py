# -*- coding: utf-8 -*-
"""mlp-cifar10

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XE-htx8Hgz-83jLrTjkXuubTjlNTBPa9

# **Dataset and Classification Model**

**MNIST Training/Test Set**
"""

import ssl
import tensorflow as tf
import numpy as np
# from tensorflow import math
from tensorflow import keras
import matplotlib.pyplot as plt

lr = 0.001
n_epochs = 100

ssl._create_default_https_context = ssl._create_unverified_context
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

y_train = y_train.flatten()
y_test = y_test.flatten()

n_classes = 10
n_features = x_train[0, ...].size
n_train = x_train.shape[0]
batch_size = 128

x_train, x_test = x_train.reshape([-1, n_features]), x_test.reshape([-1, n_features])

x_train = (x_train / 255.).astype(dtype=np.float32)
x_test = (x_test / 255).astype(dtype=np.float32)

n_classes = 10
n_features = x_train[0,...].size
n_train = x_train.shape[0]
batch_size = 128

# criterion= tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
# optimizer = tf.keras.optimizers.Adam(lr)

model = keras.Sequential(
    [
        keras.layers.Dense(512, input_shape=(n_features,), activation="relu", name="layer1"),
        keras.layers.Dense(128, activation="relu", name="layer2"),
        # we need to add softmax to last layer,
        # because model.compile(loss='sparse_categorical_crossentropy'
        # assumes from_logits=False, i.e., takes probabilities
        keras.layers.Dense(n_classes, activation="softmax", name="layer3"),
    ]
)

# print(model.summary())

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              #optimizer=optimizer,
              #loss=criterion,
              metrics=['accuracy'])

test_loss, test_acc = model.evaluate(x_test, y_test)
print("Initial test accuracy:", test_acc)

# Train the model
history = model.fit(x_train, y_train, epochs=n_epochs, batch_size=batch_size, validation_data=(x_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print("Final test accuracy:", test_acc)

# Plotting the training and test data over epochs
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Test Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training and Test Accuracy over Epochs')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(1 - np.array(history.history['accuracy']), label='Training Error')
plt.plot(1 - np.array(history.history['val_accuracy']), label='Test Error')
plt.xlabel('Epoch')
plt.ylabel('Error')
plt.title('Training and Test Error over Epochs')
plt.legend()

plt.show()

"""**CIFAR10 Training/Test Set**"""

import ssl
import tensorflow as tf
import numpy as np
# from tensorflow import math
from tensorflow import keras
import matplotlib.pyplot as plt

lr = 0.001
n_epochs = 100

ssl._create_default_https_context = ssl._create_unverified_context
# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

y_train = y_train.flatten()
y_test = y_test.flatten()

n_classes = 10
n_features = x_train[0, ...].size
n_train = x_train.shape[0]
batch_size = 128

x_train, x_test = x_train.reshape([-1, n_features]), x_test.reshape([-1, n_features])

x_train = (x_train / 255.).astype(dtype=np.float32)
x_test = (x_test / 255).astype(dtype=np.float32)

n_classes = 10
n_features = x_train[0,...].size
n_train = x_train.shape[0]
batch_size = 128

# criterion= tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
# optimizer = tf.keras.optimizers.Adam(lr)

model = keras.Sequential(
    [
        keras.layers.Dense(512, input_shape=(n_features,), activation="relu", name="layer1"),
        keras.layers.Dense(128, activation="relu", name="layer2"),
        # we need to add softmax to last layer,
        # because model.compile(loss='sparse_categorical_crossentropy'
        # assumes from_logits=False, i.e., takes probabilities
        keras.layers.Dense(n_classes, activation="softmax", name="layer3"),
    ]
)

# print(model.summary())

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              #optimizer=optimizer,
              #loss=criterion,
              metrics=['accuracy'])

test_loss, test_acc = model.evaluate(x_test, y_test)
print("Initial test accuracy:", test_acc)

# Train the model
history = model.fit(x_train, y_train, epochs=n_epochs, batch_size=batch_size, validation_data=(x_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print("Final test accuracy:", test_acc)

# Plotting the training and test data over epochs
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Test Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training and Test Accuracy over Epochs')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(1 - np.array(history.history['accuracy']), label='Training Error')
plt.plot(1 - np.array(history.history['val_accuracy']), label='Test Error')
plt.xlabel('Epoch')
plt.ylabel('Error')
plt.title('Training and Test Error over Epochs')
plt.legend()

plt.show()

"""# **Experiments**

Varying the number of network layers between 0 (a linear classifier) and 5, while keeping ReLU activation function

**MNIST Set**
"""

import ssl
import tensorflow as tf
import numpy as np
# from tensorflow import math
from tensorflow import keras
import matplotlib.pyplot as plt

lr = 0.001
n_epochs = 100

ssl._create_default_https_context = ssl._create_unverified_context
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

y_train = y_train.flatten()
y_test = y_test.flatten()

n_classes = 10
n_features = x_train[0, ...].size
n_train = x_train.shape[0]
batch_size = 128

x_train, x_test = x_train.reshape([-1, n_features]), x_test.reshape([-1, n_features])

x_train = (x_train / 255.).astype(dtype=np.float32)
x_test = (x_test / 255).astype(dtype=np.float32)

n_classes = 10
n_features = x_train[0,...].size
n_train = x_train.shape[0]
batch_size = 128

layers_list = [0, 1, 2, 3, 4, 5]
all_histories = []
test_errors = []
colors = ['r', 'y', 'g', 'b', 'c', 'm']  # Colors for each line
j = 0 # track index of layers

for num_layers in layers_list:
  print(f"Number of Layers: {num_layers}")
  if num_layers == 0:
    model = keras.Sequential()
    model.add(keras.layers.Dense(n_classes, input_shape=(n_features,), activation="softmax"))
  else:
    model = keras.Sequential()
    model.add(keras.layers.Dense(512, input_shape=(n_features,), activation="relu"))
    for i in range(num_layers):
      if i == num_layers - 1:
        model.add(keras.layers.Dense(n_classes, activation="softmax"))
      else:
        model.add(keras.layers.Dense(256 // (2 ** i), activation="relu"))

  # Compile the model
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  print(model.summary())

  test_loss, test_acc = model.evaluate(x_test, y_test)
  print("Initial test error:", 1 - test_acc)

  # Train the model
  history = model.fit(x_train, y_train, epochs=n_epochs, batch_size=batch_size, validation_data=(x_test, y_test))

  all_histories.append(history)

  # Evaluate the model
  test_loss, test_acc = model.evaluate(x_test, y_test)
  print("Final test error:", 1 - test_acc)
  test_error = [1 - acc for acc in history.history['val_accuracy']]  # Computing test error over epochs
  plt.plot(test_error, linestyle='-', color=colors[j], label=f'{num_layers} Layers')  # Plotting test error for each layer
  j += 1

plt.xlabel('Epoch')
plt.ylabel('Test Error')
plt.title('Test Error for Different Numbers of Layers over Epochs')
plt.legend()
plt.show()

"""**CIFAR10 Set**"""

import ssl
import tensorflow as tf
import numpy as np
# from tensorflow import math
from tensorflow import keras
import matplotlib.pyplot as plt

lr = 0.001
n_epochs = 100

ssl._create_default_https_context = ssl._create_unverified_context
# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

y_train = y_train.flatten()
y_test = y_test.flatten()

n_classes = 10
n_features = x_train[0, ...].size
n_train = x_train.shape[0]
batch_size = 128

x_train, x_test = x_train.reshape([-1, n_features]), x_test.reshape([-1, n_features])

x_train = (x_train / 255.).astype(dtype=np.float32)
x_test = (x_test / 255).astype(dtype=np.float32)

n_classes = 10
n_features = x_train[0,...].size
n_train = x_train.shape[0]
batch_size = 128

layers_list = [0, 1, 2, 3, 4, 5]
all_histories = []
test_errors = []
colors = ['r', 'y', 'g', 'b', 'c', 'm']  # Colors for each line
j = 0 # track index of layers

for num_layers in layers_list:
  print(f"Number of Layers: {num_layers}")
  if num_layers == 0:
    model = keras.Sequential()
    model.add(keras.layers.Dense(n_classes, input_shape=(n_features,), activation="softmax"))
  else:
    model = keras.Sequential()
    model.add(keras.layers.Dense(512, input_shape=(n_features,), activation="relu"))
    for i in range(num_layers):
      if i == num_layers - 1:
        model.add(keras.layers.Dense(n_classes, activation="softmax"))
      else:
        model.add(keras.layers.Dense(256 // (2 ** i), activation="relu"))

  # Compile the model
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  print(model.summary())

  test_loss, test_acc = model.evaluate(x_test, y_test)
  print("Initial test error:", 1 - test_acc)

  # Train the model
  history = model.fit(x_train, y_train, epochs=n_epochs, batch_size=batch_size, validation_data=(x_test, y_test))

  all_histories.append(history)

  # Evaluate the model
  test_loss, test_acc = model.evaluate(x_test, y_test)
  print("Final test error:", 1 - test_acc)
  test_error = [1 - acc for acc in history.history['val_accuracy']]  # Computing test error over epochs
  plt.plot(test_error, linestyle='-', color=colors[j], label=f'{num_layers} Layers')  # Plotting test error for each layer
  j += 1

plt.xlabel('Epoch')
plt.ylabel('Test Error')
plt.title('Test Error for Different Numbers of Layers over Epochs')
plt.legend()
plt.show()

"""Varying the activation function: no activation (i.e., linear), tanh, ReLU, for network with 5 layers.

**MNIST Set**
"""

import ssl
import tensorflow as tf
import numpy as np
# from tensorflow import math
from tensorflow import keras
import matplotlib.pyplot as plt

lr = 0.001
n_epochs = 5

ssl._create_default_https_context = ssl._create_unverified_context
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

y_train = y_train.flatten()
y_test = y_test.flatten()

n_classes = 10
n_features = x_train[0, ...].size
n_train = x_train.shape[0]
batch_size = 128

x_train, x_test = x_train.reshape([-1, n_features]), x_test.reshape([-1, n_features])

x_train = (x_train / 255.).astype(dtype=np.float32)
x_test = (x_test / 255).astype(dtype=np.float32)

n_classes = 10
n_features = x_train[0,...].size
n_train = x_train.shape[0]
batch_size = 128

activation_functions = ['linear', 'tanh', 'relu']  # Activation functions to experiment with
all_histories = []
test_errors = []
colors = ['r', 'g', 'b']
j = 0

for activation in activation_functions:
  print(f"Activation Function: {activation}")

  model = keras.Sequential()
  model.add(keras.layers.Dense(512, input_shape=(n_features,), activation=activation))
  for i in range(5):  # Ensuring 4 additional layers
    if i == 4:  # Adding the last layer with softmax
      model.add(keras.layers.Dense(n_classes, activation="softmax"))
    else:
      model.add(keras.layers.Dense(256 // (2 ** i), activation=activation))

  # Compile the model
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  print(model.summary())

  test_loss, test_acc = model.evaluate(x_test, y_test)
  print("Initial test error:", 1 - test_acc)

  # Train the model
  history = model.fit(x_train, y_train, epochs=n_epochs, batch_size=batch_size, validation_data=(x_test, y_test))

  all_histories.append(history)

  # Evaluate the model
  test_loss, test_acc = model.evaluate(x_test, y_test)
  print("Final test error:", 1 - test_acc)
  test_error = [1 - acc for acc in history.history['val_accuracy']]  # Computing test error over epochs
  plt.plot(test_error, linestyle='-', color=colors[j], label=f'{activation} Activation')  # Plotting test error for each layer
  j += 1

plt.xlabel('Epoch')
plt.ylabel('Test Error')
plt.title('Test Error for Different Activation Functions over Epochs')
plt.legend()
plt.show()

"""**CIFAR10 Set**"""

import ssl
import tensorflow as tf
import numpy as np
# from tensorflow import math
from tensorflow import keras
import matplotlib.pyplot as plt

lr = 0.001
n_epochs = 100

ssl._create_default_https_context = ssl._create_unverified_context
# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

y_train = y_train.flatten()
y_test = y_test.flatten()

n_classes = 10
n_features = x_train[0, ...].size
n_train = x_train.shape[0]
batch_size = 128

x_train, x_test = x_train.reshape([-1, n_features]), x_test.reshape([-1, n_features])

x_train = (x_train / 255.).astype(dtype=np.float32)
x_test = (x_test / 255).astype(dtype=np.float32)

n_classes = 10
n_features = x_train[0,...].size
n_train = x_train.shape[0]
batch_size = 128

activation_functions = ['linear', 'tanh', 'relu']  # Activation functions to experiment with
all_histories = []
test_errors = []
colors = ['r', 'g', 'b']
j = 0

for activation in activation_functions:
  print(f"Activation Function: {activation}")

  model = keras.Sequential()
  model.add(keras.layers.Dense(512, input_shape=(n_features,), activation=activation))
  for i in range(5):  # Ensuring 4 additional layers
    if i == 4:  # Adding the last layer with softmax
      model.add(keras.layers.Dense(n_classes, activation="softmax"))
    else:
      model.add(keras.layers.Dense(256 // (2 ** i), activation=activation))

  # Compile the model
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  print(model.summary())

  test_loss, test_acc = model.evaluate(x_test, y_test)
  print("Initial test error:", 1 - test_acc)

  # Train the model
  history = model.fit(x_train, y_train, epochs=n_epochs, batch_size=batch_size, validation_data=(x_test, y_test))

  all_histories.append(history)

  # Evaluate the model
  test_loss, test_acc = model.evaluate(x_test, y_test)
  print("Final test error:", 1 - test_acc)
  test_error = [1 - acc for acc in history.history['val_accuracy']]  # Computing test error over epochs
  plt.plot(test_error, linestyle='-', color=colors[j], label=f'{activation} Activation')  # Plotting test error for each layer
  j += 1

plt.xlabel('Epoch')
plt.ylabel('Test Error')
plt.title('Test Error for Different Activation Functions over Epochs')
plt.legend()
plt.show()