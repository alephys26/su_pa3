import numpy as np
from sklearn.metrics import auc
import matplotlib.pyplot as plt
def compute_det_curve(target_scores, nontarget_scores):

    n_scores = target_scores.size + nontarget_scores.size
    all_scores = np.concatenate((target_scores, nontarget_scores))
    labels = np.concatenate((np.ones(target_scores.size), np.zeros(nontarget_scores.size)))

    # Sort labels based on scores
    indices = np.argsort(all_scores, kind='mergesort')
    labels = labels[indices]

    # Compute false rejection and false acceptance rates
    tar_trial_sums = np.cumsum(labels)
    nontarget_trial_sums = nontarget_scores.size - (np.arange(1, n_scores + 1) - tar_trial_sums)

    frr = np.concatenate((np.atleast_1d(0), tar_trial_sums / target_scores.size))  # false rejection rates
    far = np.concatenate((np.atleast_1d(1), nontarget_trial_sums / nontarget_scores.size))  # false acceptance rates
    thresholds = np.concatenate((np.atleast_1d(all_scores[indices[0]] - 0.001), all_scores[indices]))  # Thresholds are the sorted scores

    return frr, far, thresholds


def compute_eer(target_scores, nontarget_scores, file_name):
    """ Returns equal error rate (EER) and the corresponding threshold. """
    frr, far, thresholds = compute_det_curve(target_scores, nontarget_scores)
    abs_diffs = np.abs(frr - far)
    min_index = np.argmin(abs_diffs)
    eer = np.mean((frr[min_index], far[min_index]))
        # Plot ROC curve
    plt.figure(figsize=(8, 6))
    plt.plot(thresholds, frr, 'b', label='FRR')
    plt.plot(thresholds, far, 'r', label='FAR')
    plt.scatter(x=thresholds[min_index], y=eer, color='black', label='EER %.2f'%(100*eer))
    plt.xticks([])
    plt.ylim([0, 1])
    plt.xlabel('Thresholds')
    plt.title('FAR & FRR Curve')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.savefig(file_name+'_EER.png')
    return eer

def compute_auc(target_scores, nontarget_scores, file_name):
    """ Compute AUC and plot ROC curve with EER. """
    frr, far, thresholds = compute_det_curve(target_scores, nontarget_scores)
    tpr = 1 - frr
    auc_value = auc(far, tpr)

    # Plot ROC curve
    plt.figure(figsize=(8, 6))
    plt.plot(far, tpr, 'b', label='AUC = %0.2f' % auc_value)
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.xlabel('False Positive Rate (FPR)')
    plt.ylabel('True Positive Rate (TPR)')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.savefig(file_name+'_ROC.png')

    return auc_value
