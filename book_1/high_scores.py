import os
import csv

path = '/home/dennis/Desktop/All/Real Python Course/book1/chp09/practice_files'

scores_file = os.path.join(path, 'scores.csv')

with open(scores_file, 'r') as scores:
    scores_reader = csv.reader(scores)
    high_scores = {}

    for score in scores_reader:
        if score[0] in high_scores.keys():
            if high_scores[score[0]] < score[1]:
                high_scores[score[0]] = score[1]
        else:
            high_scores[score[0]] = score[1]

    for name in sorted(high_scores):
        print(name, high_scores[name])
        
    
    #print(high_scores)
    #print(len(high_scores))
