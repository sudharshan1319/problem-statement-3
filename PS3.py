#Load and preprocess the data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset from the CSV file
data = pd.read_csv("https://github.com/DespCAP/APV_2023/raw/main/star_classification.csv")

# Split the dataset into features (X) and labels (y)
X = data.drop(columns=["class"])  # Features
y = data["class"]  # Labels

# Split the data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



#Train a machine learning model
# Initialize the Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model on the training data
clf.fit(X_train, y_train)



#Evaluate the model
# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate accuracy and print classification report
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Print classification report
print(classification_report(y_test, y_pred))
