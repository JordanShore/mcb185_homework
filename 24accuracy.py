# 24accuracy.py by Jordan Shore
#
# This program contains a function that calculates accuracy and F1 score. 

#Parameters are values for true positives, false positives, true negatives, false negatives.
#Returns accuracy,F1 score
def accuracy_f1(tp,fp,tn,fn):
	accuracy = (tp+tn)/(tp+fp+tn+fn)
	f1 = tp/(tp+0.5*(fp+fn))
	return accuracy,f1

acc1,f11 = accuracy_f1(5,5,5,5)
print("Test 1; True+:5 , False+:5 , True-:5 , False-:5")
print("Accuracy:", acc1, "F1 Score:", f11)
acc2,f12 = accuracy_f1(1000,20,1000,20)
print("Test 2; True+:1000 , False+:20 , True-:1000 , False-:20")
print("Accuracy:", acc2, "F1 Score:", f12)
acc3,f13 = accuracy_f1(60000,314,2000,16)
print("Test 2; True+:60000 , False+:314 , True-:2000 , False-:16")
print("Accuracy:", acc3, "F1 Score:", f13)