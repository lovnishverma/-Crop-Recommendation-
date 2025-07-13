## 📄 Crop Recommendation Web App

# 🌾 Crop Recommendation System (Flask + ML)

> A machine learning web application built with **Flask** that predicts the most suitable crop based on soil nutrients, temperature, humidity, pH, and rainfall.

---

## 🎯 Objective

To recommend the best crop for cultivation based on soil and environmental conditions using a **Logistic Regression** model trained on the **Crop Recommendation Dataset**.

---

## 🚀 Features

✅ Clean and user-friendly UI (HTML form)
✅ Logistic Regression-based classification
✅ Data scaling using `StandardScaler`
✅ Label encoding for multi-class targets
✅ Performance metrics displayed (Train / Validation / Test Accuracy)
✅ Easily deployable via any Flask-supported server

---

## 🛠️ Tech Stack

| Technology       | Purpose                        |
| ---------------- | ------------------------------ |
| **Flask**        | Web framework (Python)         |
| **Pandas**       | Data handling and manipulation |
| **Scikit-Learn** | Model building, preprocessing  |
| **HTML / CSS**   | Frontend Form & Display        |

---

## 📂 Project Structure

```
├── app.py               # Main Flask app
├── templates/
│   └── index.html       # HTML UI
├── Crop_recommendation.csv  # Dataset
├── README.md            # Project Documentation
```

---

## 📊 Model Details

* **Algorithm:** Logistic Regression
* **Data Scaling:** StandardScaler
* **Train / Validation / Test Split:** 70% / 15% / 15%
* **Encoded Labels:** Multi-class crops

---

## 🔢 Input Features

| Feature     | Description                  |
| ----------- | ---------------------------- |
| Nitrogen    | Soil Nitrogen content (N)    |
| Phosphorous | Soil Phosphorous content (P) |
| Potassium   | Soil Potassium content (K)   |
| Temperature | Temperature (°C)             |
| Humidity    | Humidity (%)                 |
| pH          | Soil pH level                |
| Rainfall    | Rainfall (mm)                |

---

## 📈 Performance

| Dataset        | Accuracy |
| -------------- | -------- |
| **Train**      | \~XX%    |
| **Validation** | \~XX%    |
| **Test**       | \~XX%    |

*(Exact percentages displayed on app homepage)*

---

## 🌐 How to Run

### 1️⃣ Install Requirements

```bash
pip install flask pandas scikit-learn numpy
```

### 2️⃣ Run the App

```bash
python app.py
```

### 3️⃣ Visit in Browser

```
http://127.0.0.1:5000/
```

---

## 📷 UI Preview

**Homepage:**

* Accuracy stats
* Input form for prediction

**Prediction Result:**

* Displays recommended crop.

---

## 📜 License

This project is licensed under the **MIT License**.

---

---

## 🖥️ `index.html` (with basic CSS)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Crop Recommendation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eaf4f4;
            padding: 20px;
            max-width: 600px;
            margin: auto;
        }
        h1 {
            text-align: center;
            color: #2e7d32;
        }
        form {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
        }
        label {
            display: block;
            margin-top: 10px;
        }
        input {
            width: 100%;
            padding: 7px;
            margin-top: 5px;
        }
        .submit-btn {
            margin-top: 20px;
            padding: 10px;
            width: 100%;
            background-color: #4caf50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .submit-btn:hover {
            background-color: #45a049;
        }
        .accuracy, .result {
            background-color: #dcedc8;
            padding: 10px;
            border-radius: 5px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Crop Recommendation System</h1>
    <div class="accuracy">
        <p><b>Training Accuracy:</b> {{ train_acc }}</p>
        <p><b>Validation Accuracy:</b> {{ val_acc }}</p>
        <p><b>Test Accuracy:</b> {{ test_acc }}</p>
    </div>

    <form method="POST" action="/predict">
        <label>Nitrogen (N):</label>
        <input type="number" step="any" name="n" required>

        <label>Phosphorous (P):</label>
        <input type="number" step="any" name="p" required>

        <label>Potassium (K):</label>
        <input type="number" step="any" name="k" required>

        <label>Temperature (°C):</label>
        <input type="number" step="any" name="temperature" required>

        <label>Humidity (%):</label>
        <input type="number" step="any" name="humidity" required>

        <label>pH Level:</label>
        <input type="number" step="any" name="ph" required>

        <label>Rainfall (mm):</label>
        <input type="number" step="any" name="rainfall" required>

        <button class="submit-btn" type="submit">Predict Crop</button>
    </form>

    {% if data %}
    <div class="result">
        <h3>Recommended Crop:</h3>
        <p>{{ data }}</p>
    </div>
    {% endif %}
</body>
</html>
```

---
