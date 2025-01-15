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



def main(dataset_name):
    #call the load_dataset to get correct data set mnist or mnist_fashion
    (x_train, y_train), (x_test, y_test) = load_dataset(dataset_name)
    # Reshape data (28x28 images -> 784 pixel vectors)
    x_train = x_train.reshape(x_train.shape[0], -1)
    x_test = x_test.reshape(x_test.shape[0], -1)

    # Normalize data (optional but helps with performance)
    x_train = x_train.astype("float32") / 255
    x_test = x_test.astype("float32") / 255

    # 1-NN Classifier
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(x_train, y_train)

    # Predict and calculate accuracy
    y_pred = knn.predict(x_test)
    accuracy = class_acc(y_pred, y_test)
    print(f"Classifier accuracy: {accuracy}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    dataset_name = sys.argv[1].lower()
    main(dataset_name)
