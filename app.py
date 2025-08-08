from flask import Flask, render_template, request, jsonify
from currency_converter import CurrencyConverter
import json
import os
import logging

app = Flask(__name__)
# Basic structured logging setup
logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "INFO"),
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
converter = CurrencyConverter()

@app.route('/')
def index():
    """Main page with the currency converter interface."""
    currencies = converter.get_supported_currencies()
    return render_template('index.html', currencies=currencies)

@app.route('/convert', methods=['POST'])
def convert():
    """API endpoint for currency conversion."""
    try:
        data = request.get_json()
        amount = float(data.get('amount', 0))
        from_currency = data.get('from_currency', '')
        to_currency = data.get('to_currency', '')
        
        if amount <= 0:
            return jsonify({'error': 'Amount must be positive'}), 400
        
        result = converter.convert_currency(amount, from_currency, to_currency)
        
        if result is not None:
            formatted_from = converter.format_currency(amount, from_currency)
            formatted_to = converter.format_currency(result, to_currency)
            
            return jsonify({
                'success': True,
                'result': result,
                'formatted_from': formatted_from,
                'formatted_to': formatted_to,
                'exchange_rate': round(result / amount, 4)
            })
        else:
            return jsonify({'error': 'Conversion failed. Please check your input.'}), 400
            
    except (ValueError, KeyError) as e:
        return jsonify({'error': 'Invalid input data'}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/currencies')
def get_currencies():
    """API endpoint to get supported currencies."""
    currencies = converter.get_supported_currencies()
    return jsonify(currencies)

@app.route('/history')
def get_history():
    """API endpoint to get historical exchange rates for a pair.

    Query params:
      - from_currency
      - to_currency
      - days (optional, default 30)
    """
    from_currency = request.args.get('from_currency', '')
    to_currency = request.args.get('to_currency', '')
    try:
        days = int(request.args.get('days', '30'))
        days = max(2, min(days, 365))
    except ValueError:
        days = 30

    result = converter.get_historical_rates(from_currency, to_currency, days)
    if not result:
        return jsonify({'error': 'Could not fetch historical rates'}), 400

    dates, rates = result
    return jsonify({
        'from_currency': from_currency.upper(),
        'to_currency': to_currency.upper(),
        'days': days,
        'dates': dates,
        'rates': rates,
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
