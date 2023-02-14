# glasses_or_no_glasses

Project for "Distributed and pervasive systems" course - University of Milan - Year 2020/21

Authors: [Marco Ghezzi](https://github.com/marcoghezzi1) - [Matteo Limoncini](https://github.com/matteolimoncini)

This project analyses and compares different solutions to tackle the problem of image classification for the [Glasses or No Glasses dataset](https://www.kaggle.com/datasets/jeffheaton/glasses-or-no-glasses). We start from a simple neural network up to more complex Convolutional Neural Networks with multiple layers.
The goal of this project is to implement an artificial neural network in order to identify if a person is wearing glasses or not. We used the [TensorFlow API](https://www.tensorflow.org) to build and train our models and the Keras Tuner framework for a better hyperparameters optimization. 
This project identified the best suited model to solve this problem: a convolutional neural network with 3 convolutional layers and 2 dense layers that reach an accuracy of 0.99 and a loss of 0.10
