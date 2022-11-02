import numpy as np
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score


def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''

    tp = sum((ground_truth == True) & (prediction == True))
    tn = sum((ground_truth == False) & (prediction == False))
    fn = sum((ground_truth == True) & (prediction == False))
    fp = sum((ground_truth == False) & (prediction == True))

    precision = tp / float(tp + fp)
    recall = tp / float(tp + fn)
    accuracy = (tp + tn) / float(tp + tn + fn + fp)
    f1 = (2 * precision * recall) / (precision + recall)

    print('sklearn test')
    print(f"Accuracy: {accuracy_score(prediction, ground_truth)}")
    print(f"Precision: {precision_score(ground_truth, prediction)}")
    print(f"Recall: {recall_score(ground_truth, prediction)}")
    print(f"F1-score: {f1_score(ground_truth, prediction)}")
    print()

    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''

    for k in range(self.k):
        knn_classifier = KNN(k=1, metric='manhattan')
        knn_classifier.fit(binary_train_X, binary_train_y)
    return 0
