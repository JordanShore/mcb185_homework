# 24accuracy.py by Jordan Shore
#
# This program contains a function that calculates accuracy and F1 score. 

#Parameters are values for true positives, false positives, true negatives, false negatives.
#Returns accuracy, F1 score
def accuracy_f1(tp, tn, fp, fn):
	accuracy = (tp + tn) / (tp + tn + fp + fn)
	f1 = tp / (tp + 0.5*(fp + fn))
	return accuracy, f1


print("Test 1; True+:5 , True-:5 , False+:5 , False-:5")
print("Accuracy, F1 Score =", accuracy_f1(5, 5, 5, 5))
print("Test 2; True+:1000 , True-:20 , False+:1000 , False-:20")
print("Accuracy, F1 Score =", accuracy_f1(1000, 20, 1000, 20))
print("Test 3; True+:60000 , True-:2000 , False+:314 , False-:16")
print("Accuracy, F1 Score =", accuracy_f1(60000, 2000, 314, 16))