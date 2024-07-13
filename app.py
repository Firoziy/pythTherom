from flask import Flask, request, render_template
import math as m
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    base = float(request.form['base'])
    perpendicular = float(request.form['perpendicular'])
    hypotenuse = round(m.sqrt(m.pow(base, 2) + m.pow(perpendicular, 2)), 2)
    
    # Save the data to CSV
    save_to_csv(base, perpendicular, hypotenuse)
    
    return render_template('result.html', hypotenuse=hypotenuse)

def save_to_csv(base, perpendicular, hypotenuse):
    with open('calculations.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), base, perpendicular, hypotenuse])

if __name__ == '__main__':
    app.run(debug=True)
