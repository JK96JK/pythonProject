import os
import sys
import numpy as np

os.environ["SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL"] = "true"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

from scipy.stats import multivariate_normal
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
    cov_matrices = np.zeros((num_classes, x_train.shape[1], x_train.shape[1]))

    for c in range(num_classes):
        class_samples = x_train[y_train == c]
        mean_vectors[c] = np.mean(class_samples, axis=0)
        variances = np.var(class_samples, axis=0)

        # Stabilize covariance matrices by adding a small value to the diagonal

        cov_matrices[c] = np.diag(variances) + 0.001 * np.eye(x_train.shape[1])

    return mean_vectors, cov_matrices


def multivariate(x, mean, cov):
    #multivariate_normal.pdf will overflow because it gets too big or too big negative values. Logarithmic value is better because of that.
    #return multivariate_normal.pdf(x, mean=mean, cov=cov)
    return multivariate_normal.logpdf(x, mean=mean, cov=cov)


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

    # Calculate mean and covariance for each class
    mean_vectors, cov_matrices = calculate_class_stats(x_train, y_train)

    # Classify test samples
    num_test_samples = x_test.shape[0]
    num_classes = 10
    # Prepare a likelihoods matrix
    likelihoods = np.zeros((num_test_samples, num_classes))
    # Compute likelihoods for all classes
    for c in range(10):
        # Compute the likelihood for all test samples for class c
        likelihoods[:, c] = multivariate(x_test, mean_vectors[c], cov_matrices[c])

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
