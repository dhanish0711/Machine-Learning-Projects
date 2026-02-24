from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Train model on startup (matches the notebook exactly)
# ---------------------------------------------------------------------------
data = pd.read_csv("tips.csv")

# Encode categoricals (same mapping as the notebook)
SEX_MAP = {"Female": 0, "Male": 1}
SMOKER_MAP = {"No": 0, "Yes": 1}
DAY_MAP = {"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3}
TIME_MAP = {"Lunch": 0, "Dinner": 1}

data["sex"] = data["sex"].map(SEX_MAP)
data["smoker"] = data["smoker"].map(SMOKER_MAP)
data["day"] = data["day"].map(DAY_MAP)
data["time"] = data["time"].map(TIME_MAP)

x = np.array(data[["total_bill", "sex", "smoker", "day", "time", "size"]])
y = np.array(data["tip"])

# Train-test split (same as notebook: test_size=0.2, random_state=42)
xtrain, xtest, ytrain, ytest = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Linear Regression (same as notebook)
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
    total_bill = float(request.form["total_bill"])
    sex = SEX_MAP[request.form["sex"]]
    smoker = SMOKER_MAP[request.form["smoker"]]
    day = DAY_MAP[request.form["day"]]
    time = TIME_MAP[request.form["time"]]
    size = int(request.form["size"])

    features = np.array([[total_bill, sex, smoker, day, time, size]])
    prediction = model.predict(features)[0]

    return render_template(
        "index.html",
        prediction=round(prediction, 2),
        total_bill=total_bill,
        sex=request.form["sex"],
        smoker=request.form["smoker"],
        day=request.form["day"],
        time=request.form["time"],
        size=size,
        metrics=metrics,
    )


if __name__ == "__main__":
    app.run(debug=True)

