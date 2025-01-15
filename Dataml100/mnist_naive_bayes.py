import os
import sys
import numpy as np

os.environ["SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL"] = "true"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

from sklearn.neighbors import KNeighborsClassifier
from tensorflow.keras.datasets import mnist, fashion_mnist


def class_acc(pred, gt):
    """
    Calculate the accuracy of predictions.

    :param pred: predicted class labels
    :param gt: ground truth class labels
    :return: classification accuracy
    """
    correct = sum(p == g for p, g in zip(pred, gt))
    return correct / len(gt)


def load_dataset(dataset_name):
    """
    Load either MNIST or Fashion-MNIST dataset based on the argument.
    """
    if dataset_name == "mnist":
        return mnist.load_data()
    elif dataset_name == "fashion":
        return fashion_mnist.load_data()
    else:
        raise ValueError("Invalid dataset name. Use 'mnist' or 'fashion'.")


def calculate_class_stats(x_train, y_train):
    """
    Calculate mean and variance vectors for each class.

    :param x_train: Training data
    :param y_train: Training labels
    :return: mean and variance for each class
    """
    num_classes = 10
    mean_vectors = np.zeros((num_classes, x_train.shape[1]))
    var_vectors = np.zeros((num_classes, x_train.shape[1]))

    for c in range(num_classes):
        class_samples = x_train[y_train == c]
        mean_vectors[c] = np.mean(class_samples, axis=0)
        var_vectors[c] = np.var(class_samples, axis=0)
    var_vectors += 0.001
    return mean_vectors, var_vectors


def log_likelihood(x, mean, var):
    """
    Compute the log likelihood of the Gaussian distribution under the naive assumption.

    :param x: Data sample
    :param mean: Mean vector
    :param var: Variance vector
    :return: Log likelihood value
    """
    # Log-likelihood computation for Naive Bayes
    likelihood = -0.5 * np.sum(np.log(2 * np.pi * var)) - 0.5 * np.sum(
        ((x - mean) ** 2) / var, axis=1
    )
    return likelihood


def main(dataset_name):
    # call the load_dataset to get correct data set mnist or mnist_fashion
    (x_train, y_train), (x_test, y_test) = load_dataset(dataset_name)
    # Reshape data (28x28 images -> 784 pixel vectors)
    x_train = x_train.reshape(x_train.shape[0], -1)
    x_test = x_test.reshape(x_test.shape[0], -1)

    # Normalize data (optional but helps with performance)
    x_train = x_train.astype("float32") / 255
    x_test = x_test.astype("float32") / 255

    # adding the noice to training data
    noice = np.random.normal(loc=0.0, scale=0.1, size=x_train.shape)
    x_train += noice

    # Calculate mean and variance for each class
    mean_vectors, var_vectors = calculate_class_stats(x_train, y_train)

    # Classify test samples
    num_test_samples = x_test.shape[0]
    predictions = np.zeros(num_test_samples, dtype=int)

    num_classes = 10

    # Prepare likelihoods matrix
    likelihoods = np.zeros((num_test_samples, num_classes))

    # Compute likelihoods for all classes at once
    for c in range(num_classes):
        likelihoods[:, c] = log_likelihood(x_test, mean_vectors[c], var_vectors[c])

    # Assign the class with the highest log likelihood
    predictions = np.argmax(likelihoods, axis=1)

    # calculate accuracy
    accuracy = class_acc(predictions, y_test)
    print(f"Classifier accuracy: {accuracy}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    dataset_name = sys.argv[1].lower()
    main(dataset_name)
