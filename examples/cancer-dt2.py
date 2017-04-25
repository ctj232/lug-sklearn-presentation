# How well did we do?
train_acc = tree.score(X_train, y_train)
test_acc = tree.score(X_test, y_test)
print("Training Accuracy: {:.3f}".format(train_acc))
print("Testing Accuracy: {:.3f}".format(test_acc))
# Training Accuracy: 1.000
# Testing Accuracy: 0.923
