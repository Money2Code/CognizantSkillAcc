import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Sample Weather Dataset
data = {
    'Temperature': [30, 25, 28, 22, 32, 27, 26, 24, 29, 31],
    'Humidity': [70, 65, 80, 75, 60, 85, 90, 78, 67, 72],
    'Wind Speed': [5, 10, 15, 12, 8, 6, 7, 14, 9, 11],
    'Precipitation': [1, 0, 1, 0, 1, 1, 0, 1, 0, 0],  # 1 = Rain, 0 = No Rain
    'Weather': ['Rainy', 'Sunny', 'Rainy', 'Cloudy', 'Sunny', 'Rainy', 'Cloudy', 'Rainy', 'Sunny', 'Sunny']
}

df = pd.DataFrame(data)

# Encode categorical labels
label_encoder = LabelEncoder()
df['Weather'] = label_encoder.fit_transform(df['Weather'])

# Features and target
X = df.drop(columns=['Weather'])
y = df['Weather']

# Normalize numerical features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build Decision Tree Model
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# Make Predictions
y_pred = clf.predict(X_test)

# Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Display Results
print(f"Accuracy: {accuracy:.2f}")
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", report)
