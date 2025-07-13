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
