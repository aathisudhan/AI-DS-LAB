import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix


# Sample Dataset (Spam / Not Spam emails) data = {
"email": [
"Win money now",
"Lowest price for your medicines", "Hi friend how are you",
"Let’s catch up for lunch", "Congratulations you won a prize", "Cheap loans available",
"Are you coming tomorrow", "Meeting is scheduled at 5pm", "Get free coupons now", "Dinner plan tonight?"
],
"label": [
"spam", "spam", "ham", "ham", "spam",
"spam", "ham", "ham", "spam", "ham"
]
}
 
# Convert to DataFrame df = pd.DataFrame(data)
# Step 1: Feature Extraction (Bag of Words) vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["email"])


y = df["label"]
# Step 2: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Step 3: Apply Naïve Bayes Classifier model = MultinomialNB() model.fit(X_train, y_train)
# Step 4: Predictions
y_pred = model.predict(X_test)


# Step 5: Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred)) print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Step 6: Test on New Emails
new_emails = ["Win a lottery now", "Can we meet tomorrow?"] new_X = vectorizer.transform(new_emails)
predictions = model.predict(new_X) print("\nNew Email Predictions:")
for email, label in zip(new_emails, predictions): print(f"'{email}' --> {label}")
