# 📈 Future Sales Prediction with Machine Learning

A Flask web application that predicts future product sales based on advertising spend across **TV**, **Radio**, and **Newspaper** channels using **Linear Regression**.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-F7931E?logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- **Sales Prediction** — Predict sales based on TV, Radio, and Newspaper advertising budgets
- **Model Metrics** — Displays R² Score, MAE, and RMSE on the UI
- **Modern UI** — Dark emerald-themed design with animated gradients and glassmorphism
- **Responsive** — Works on desktop and mobile

---

## 📂 Project Structure

```
├── app.py                  # Flask backend + model training
├── advertising.csv         # Dataset (200 records)
├── templates/
│   └── index.html          # Jinja2 HTML template
├── static/
│   └── style.css           # Premium dark-themed stylesheet
├── requirements.txt        # Python dependencies
├── .gitignore
├── LICENSE
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
   cd "Machine-Learning-Projects/2. Future Sales Prediction with Machine Learning"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
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

The advertising dataset contains **200 records** with the following features:

| Feature   | Type    | Description                             |
|-----------|---------|-----------------------------------------|
| TV        | Numeric | TV advertising spend (in $1000s)        |
| Radio     | Numeric | Radio advertising spend (in $1000s)     |
| Newspaper | Numeric | Newspaper advertising spend (in $1000s) |
| **Sales** | **Target** | **Product sales (in 1000s of units)** |

### Model Pipeline

1. **Load data** — Read `advertising.csv`
2. **Train/Test Split** — 80/20 split with `random_state=42`
3. **Train** — `LinearRegression` from scikit-learn
4. **Evaluate** — R² Score, Mean Absolute Error, Root Mean Squared Error

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
| RMSE   | Root mean squared error            |

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
