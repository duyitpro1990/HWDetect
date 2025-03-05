from flask import render_template, request, redirect, url_for, flash

from flask import Flask
import ai.HW as ai
app = Flask(__name__)
app.secret_key = "super secret key"
@app.route('/')
def home():
    return 'Hello, world!'
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Here you would typically check the username and password against a database
        if username == 'admin' and password == '12345':  # Example check
            flash('Login successful!', 'success')
            return redirect(url_for('painting'))  # Redirect to a home page or dashboard
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')
@app.route('/paint', methods=['GET'])
def painting():
    return render_template('painting.html')
@app.route('/predict', methods=['POST'])
def predict():
    print('Predicting...')
    image = request.form.get('imgBase64')
    result = ai.detectHW(image)
    return str(result)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)