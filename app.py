from flask import Flask, render_template
from datetime import datetime, timedelta
import random

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <head><title>Progalused</title></head>
    <body>
        <h1>Progalused</h1>
        <p>Programmeerimise alused</p>
        <ul>
            <li><a href="/hinnalugu">Hinnalugu (Price History)</a></li>
        </ul>
    </body>
    </html>
    '''

@app.route('/hinnalugu')
def hinnalugu():
    # Sample car listing data
    listing = {
        'title': 'BMW 320d Touring',
        'source': 'auto24.ee',
        'year': 2018,
        'km': 85000,
        'price_eur': 25500,
        'price': 25500,
        'currency': 'EUR',
        'url': 'https://www.auto24.ee/used/12345',
        'image': 'https://via.placeholder.com/480x320/0066cc/ffffff?text=BMW+320d',
        'engine_size': 2.0,
        'fuel_type': 'Diisel',
        'transmission': 'Automaat',
        'body_type': 'Universaal',
        'drivetrain': 'Tagumine',
        'fair_price_eur': 26000
    }
    
    # Generate sample price history data (last 30 days)
    labels = []
    values = []
    base_date = datetime.now() - timedelta(days=30)
    base_price = 25500
    
    for i in range(31):
        date = base_date + timedelta(days=i)
        labels.append(date.strftime('%Y-%m-%d'))
        # Add some random variation to the price
        price_variation = random.randint(-500, 300)
        price = base_price + price_variation
        values.append(price)
    
    return render_template('hinnalugu.html', listing=listing, labels=labels, values=values)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)