import numpy as np

def accuracy_score(y_true, y_pred):
	num = 0
	length = len(y_pred)
	for i in range(length):
		if (y_pred[i] == 0 and y_true[i] == 0) or (y_pred[i] == 1 and y_true[i] == 1):
			num += 1
		else:
			continue

	return num/length
