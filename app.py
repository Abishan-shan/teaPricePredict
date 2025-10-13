import math

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from prophetModel.model import model
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = "wave_secret_123"

ADMIN_USER = "admin"
ADMIN_PASS = "1234"
TEA_TYPES = ['Ceylon Black', 'Green Tea', 'Herbal Tea']


def get_weekly_prices(tea_type):
    prices = []
    dates = []
    for i in range(7):
        date = (datetime.now() - timedelta(days=i)).date()
        predicted_price = float(model(tea_type, str(date)))
        prices.append(predicted_price)
        dates.append(str(date))
    return dates[::-1], prices[::-1]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == ADMIN_USER and password == ADMIN_PASS:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))

    tea_type = request.args.get('tea_type', TEA_TYPES[0])

    weekly_dates, weekly_prices = get_weekly_prices(tea_type)

    last_prediction_date = weekly_dates[-1]
    avg_price = sum(weekly_prices) / len(weekly_prices)

    return render_template('dashboard.html',
                           weekly_dates=weekly_dates,
                           weekly_prices=weekly_prices,
                           last_prediction_date=last_prediction_date,
                           avg_price=math.ceil(avg_price),
                           tea_types=TEA_TYPES,
                           selected_tea=tea_type)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'user' not in session:
        return redirect(url_for('login'))

    result = None
    picked_date = None
    tea_type = None
    if request.method == 'POST':
        tea_type = request.form['tea_type']
        picked_date = request.form['picked_date']

        result = model(tea_type, picked_date)

    return render_template('predict.html', result=result, picked_date=picked_date, tea_types=TEA_TYPES,
                           tea_type=tea_type)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
