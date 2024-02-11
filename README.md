# Multi-Layer Perceptron (MLP) for CIFAR10 Classification
This repository contains a basic implementation of a Multi-Layer Perceptron (MLP) neural network trained on the MNIST, CIFAR10 datasets using TensorFlow. <br><br>
The model is trained using gradient descent and cross-entropy loss.

## Experiments
A series of experiments were conducted to analyze the impact of several factors on the final test error. These experiments include:

- **Varying the number of network layers** between 0 (a linear classifier) and 5 while keeping the ReLU activation function constant.
- **Varying the activation function** between none, tanh, and ReLU for a network with 5 layers.

## Results

The results of the experiments (including output and plots) on both datasets can be found in the `mlp_cifar10.ipynb` file.
___
Trang Ly <br>
lytt6@vcu.edu
