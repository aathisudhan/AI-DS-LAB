import pandas as pd
from sklearn.model_selection import train_test_split from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score


#
# Sample Dataset #
balance_data = pd.DataFrame({
'Purchase': ['Yes','No','Yes','No','Yes','Yes','No','Yes','No','No'], 'Age': [25, 35, 45, 20, 55, 65, 35, 50, 40, 30],
'Income': [50000, 60000, 80000, 20000, 90000, 120000, 70000, 100000, 85000, 45000]
})


# Features (X) and Target (y)
X = balance_data[['Age', 'Income']] y = balance_data['Purchase']

# Split data (train 70%, test 30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)


#
# Decision Tree using Gini Index #
clf_gini = DecisionTreeClassifier(criterion="gini", random_state=1) clf_gini.fit(X_train, y_train)
 


y_pred_gini = clf_gini.predict(X_test) print("Results Using Gini Index:") print("Predicted values:", y_pred_gini.tolist())
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_gini)) print("Accuracy:", round(accuracy_score(y_test, y_pred_gini)*100, 2), "%") print("Report:\n", classification_report(y_test, y_pred_gini))

#
# Decision Tree using Entropy #
clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=1) clf_entropy.fit(X_train, y_train)
y_pred_entropy = clf_entropy.predict(X_test) print("\nResults Using Entropy:") print("Predicted values:", y_pred_entropy.tolist())
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_entropy)) print("Accuracy:", round(accuracy_score(y_test, y_pred_entropy)*100, 2), "%") print("Report:\n", classification_report(y_test, y_pred_entropy))
