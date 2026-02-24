# 🍽️ Waiter Tips Prediction with Machine Learning

A Flask web application that predicts waiter tips using **Linear Regression**. Enter bill details and get an instant tip prediction powered by a model trained on real restaurant data.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-F7931E?logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- **Tip Prediction** — Predict tip amount based on total bill, gender, smoker status, day, meal time, and party size
- **Model Metrics** — Displays R² Score, MAE, and RMSE evaluated on a held-out test set
- **Modern UI** — Dark glassmorphism design with animated gradients, icon-labelled form fields, and micro-interactions
- **Responsive** — Works on desktop and mobile

---

## 📂 Project Structure

```
├── app.py                  # Flask backend + model training
├── tips.csv                # Dataset (245 records)
├── templates/
│   └── index.html          # Jinja2 HTML template
├── static/
│   └── style.css           # Premium dark-themed stylesheet
├── Waiter Tips Prediction
│   with Machine Learning.ipynb  # Original Jupyter notebook
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/dhanish0711/Machine-Learning-Projects.git
   cd "Machine-Learning-Projects/1. Waiter Tips Prediction with Machine Learning"
   ```

2. **Install dependencies**
   ```bash
   pip install flask pandas numpy scikit-learn
   ```

3. **Run the app**
   ```bash
   python app.py
   ```

4. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 🧠 How It Works

### Dataset

The [tips dataset](https://github.com/mwaskom/seaborn-data/blob/master/tips.csv) contains **245 restaurant records** with the following features:

| Feature    | Type        | Description                     |
|------------|-------------|---------------------------------|
| total_bill | Numeric     | Total bill amount ($)           |
| sex        | Categorical | Male / Female                   |
| smoker     | Categorical | Yes / No                        |
| day        | Categorical | Thur / Fri / Sat / Sun          |
| time       | Categorical | Lunch / Dinner                  |
| size       | Numeric     | Party size (1–10)               |
| **tip**    | **Target**  | **Tip amount ($)**              |

### Model Pipeline

1. **Encode categoricals** — Map string values to integers
2. **Train/Test Split** — 80/20 split with `random_state=42`
3. **Train** — `LinearRegression` from scikit-learn
4. **Evaluate** — R² Score, Mean Absolute Error, Root Mean Squared Error

### Categorical Encoding

```python
sex:    Female → 0, Male → 1
smoker: No → 0, Yes → 1
day:    Thur → 0, Fri → 1, Sat → 2, Sun → 3
time:   Lunch → 0, Dinner → 1
```

---

## 🛠️ Tech Stack

| Layer     | Technology           |
|-----------|----------------------|
| Backend   | Flask (Python)       |
| ML Model  | scikit-learn         |
| Frontend  | HTML, CSS, Jinja2    |
| Data      | pandas, NumPy        |

---

## 📊 Model Performance

Metrics are computed on a 20% held-out test set and displayed on the web UI.

| Metric | Description                        |
|--------|------------------------------------|
| R²     | Proportion of variance explained   |
| MAE    | Average absolute prediction error  |
| RMSE   | Root mean squared error             |

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/dhanish0711">dhanish0711</a>
</p>
