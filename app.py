from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# Load dataset
dataset = "Crop_recommendation.csv"
data = pd.read_csv(dataset)

# Split into features and labels
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Encode the labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train / Validation / Test Split (70/15/15)
X_train_full, X_test, y_train_full, y_test = train_test_split(
    X, y_encoded, test_size=0.15, random_state=42, stratify=y_encoded
)
X_train, X_val, y_train, y_val = train_test_split(
    X_train_full, y_train_full, test_size=0.1765, random_state=42, stratify=y_train_full
)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

# Train model
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Accuracy scores
train_acc = accuracy_score(y_train, model.predict(X_train))
val_acc = accuracy_score(y_val, model.predict(X_val))
test_acc = accuracy_score(y_test, model.predict(X_test))

# Routes


@app.route("/")
def home():
    return render_template("index.html",
                           train_acc=f"{train_acc*100:.2f}%",
                           val_acc=f"{val_acc*100:.2f}%",
                           test_acc=f"{test_acc*100:.2f}%"
                           )


@app.route("/predict", methods=["POST"])
def predict():
    n = float(request.form.get("n"))
    p = float(request.form.get("p"))
    k = float(request.form.get("k"))
    temp = float(request.form.get("temperature"))
    hum = float(request.form.get("humidity"))
    ph = float(request.form.get("ph"))
    rain = float(request.form.get("rainfall"))

    input_features = np.array([[n, p, k, temp, hum, ph, rain]])
    input_scaled = scaler.transform(input_features)

    prediction_encoded = model.predict(input_scaled)[0]
    prediction_label = le.inverse_transform([prediction_encoded])[0]

    return render_template("index.html",
                           data=prediction_label,
                           train_acc=f"{train_acc*100:.2f}%",
                           val_acc=f"{val_acc*100:.2f}%",
                           test_acc=f"{test_acc*100:.2f}%"
                           )


if __name__ == '__main__':
    app.run(debug=True)
