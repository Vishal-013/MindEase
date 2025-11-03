# train_model.py
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# -----------------------------
# 1. Example Data
# -----------------------------
# Each row: [q1, q2, q3, q4, q5]
# Labels: 0 = Low risk, 1 = Moderate risk, 2 = High risk
X = np.array([
    [1, 1, 1, 1, 1],   # Very healthy
    [2, 2, 2, 2, 2],   # Mild issues
    [3, 3, 3, 3, 3],   # Moderate
    [4, 4, 4, 4, 4],   # Higher stress
    [5, 5, 5, 5, 5],   # Severe
    [5, 4, 5, 4, 5],   # Severe pattern
    [2, 3, 2, 3, 2],   # Mid-level
    [1, 2, 1, 2, 1],   # Mostly okay
])

y = np.array([
    0, 0, 1, 1, 2, 2, 1, 0
])

# -----------------------------
# 2. Train/Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------------
# 3. Train Model
# -----------------------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# 4. Save Model
# -----------------------------
joblib.dump(model, "models/mental_health_model.pkl")
print("✅ Model trained and saved as models/mental_health_model.pkl")
