#!/usr/bin/env python3
"""
Simple Flask application with Selenium support for progalused repository.
This provides a web interface for the programming exercises.
"""

import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

@app.route('/')
def home():
    """Home page showing available programming exercises."""
    return jsonify({
        'message': 'Progalused - Programming Exercises Web Interface',
        'status': 'running',
        'browser_mode': 'headless' if os.environ.get('SHOW_BROWSER', 'false').lower() == 'false' else 'visible'
    })

@app.route('/health')
def health_check():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'service': 'progalused-web'})

@app.route('/selenium-test')
def selenium_test():
    """Test endpoint to verify Selenium functionality."""
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        
        # Configure Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        
        # Create webdriver instance
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://httpbin.org/html')
        title = driver.title
        driver.quit()
        
        return jsonify({
            'selenium_status': 'working',
            'test_page_title': title,
            'browser_mode': 'headless'
        })
    except Exception as e:
        return jsonify({
            'selenium_status': 'error',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    # Get configuration from environment variables
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    
    print(f"Starting Flask application on {host}:{port}")
    print(f"Debug mode: {debug}")
    print(f"Browser mode: {'headless' if os.environ.get('SHOW_BROWSER', 'false').lower() == 'false' else 'visible'}")
    
    app.run(host=host, port=port, debug=debug)