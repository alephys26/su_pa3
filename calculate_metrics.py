"""
Script to compute pooled EER for ASVspoof2021 DF. 
Usage:
$: python PATH_TO_SCORE_FILE PATH_TO_GROUDTRUTH_DIR phase
 
 -PATH_TO_SCORE_FILE: path to the score file 
 -PATH_TO_GROUNDTRUTH_DIR: path to the directory that has the CM protocol.
    Please follow README, download the key files, and use ./keys
 -phase: either progress, eval, or hidden_track
Example:
$: python evaluate.py score.txt ./keys eval
"""
import sys
import numpy as np
import pandas
import auc_eer as em
from glob import glob

submit_file = sys.argv[1]
truth_file = sys.argv[2]

def eval_to_score_file(score_file, cm_key_file):
    
    cm_data = pandas.read_csv(cm_key_file, sep=':', header=None)
    submission_scores = pandas.read_csv(score_file, sep=':', header=None, skipinitialspace=True)
    if len(submission_scores) != len(cm_data):
        print('CHECK: submission has %d of %d expected trials.' % (len(submission_scores), len(cm_data)))
        exit(1)

    if len(submission_scores.columns) > 2:
        print('CHECK: submission has more columns (%d) than expected (2). Check for leading/ending blank spaces.' % len(submission_scores.columns))
        exit(1)
            
    cm_scores = submission_scores.merge(cm_data, left_on=0, right_on=0, how='inner')
    bona_cm = cm_scores[cm_scores['1_y'] == 'bonafide']['1_x'].values
    spoof_cm = cm_scores[cm_scores['1_y'] == 'spoof']['1_x'].values
    eer_cm = em.compute_eer(bona_cm, spoof_cm, submit_file)
    auc_cm = em.compute_auc(bona_cm, spoof_cm, submit_file)
    out_data = "eer: %.2f\n" % (100*eer_cm)
    out_data += "auc: %.2f\n" % (auc_cm)
    print(out_data)

if __name__ == "__main__":
    eval_to_score_file(submit_file, truth_file)
