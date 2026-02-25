from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Train model on startup (matches the notebook exactly)
# ---------------------------------------------------------------------------
data = pd.read_csv("advertising.csv")

x = np.array(data.drop(["Sales"], axis=1))
y = np.array(data["Sales"])

xtrain, xtest, ytrain, ytest = train_test_split(
    x, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(xtrain, ytrain)

# Compute accuracy metrics on the test set
y_pred = model.predict(xtest)
metrics = {
    "r2": round(r2_score(ytest, y_pred) * 100, 2),
    "mae": round(mean_absolute_error(ytest, y_pred), 2),
    "rmse": round(np.sqrt(mean_squared_error(ytest, y_pred)), 2),
}


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html", metrics=metrics)


@app.route("/predict", methods=["POST"])
def predict():
    tv = float(request.form["tv"])
    radio = float(request.form["radio"])
    newspaper = float(request.form["newspaper"])

    features = np.array([[tv, radio, newspaper]])
    prediction = model.predict(features)[0]

    return render_template(
        "index.html",
        prediction=round(prediction, 2),
        tv=tv,
        radio=radio,
        newspaper=newspaper,
        metrics=metrics,
    )


if __name__ == "__main__":
    app.run(debug=True)
