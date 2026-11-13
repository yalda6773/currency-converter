# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    converted_amount = None
    error = None
    amount = ""
    from_currency = "USD"
    to_currency = "EUR"

    if request.method == 'POST':
        try:
            amount = float(request.form.get('amount', 0))
            from_currency = request.form.get('from_currency')
            to_currency = request.form.get('to_currency')

            url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
            response = requests.get(url)
            data = response.json()

            if 'rates' in data:
                converted_amount = data['rates'][to_currency]
            else:
                error = "خطا در دریافت نرخ ارز."
        except Exception as e:
            error = "لطفاً یک عدد معتبر وارد کنید."

    return render_template('index.html', 
                           converted_amount=converted_amount, 
                           error=error, 
                           amount=amount,
                           from_currency=from_currency,
                           to_currency=to_currency)

if __name__ == '__main__':
    app.run(debug=True)
