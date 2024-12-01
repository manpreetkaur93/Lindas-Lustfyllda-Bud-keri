from flask import render_template, redirect, url_for
from app import app
from app.optimizer import optimize_delivery
from app.utils import calculate_statistics, generate_histograms

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/optimize')
def optimize():
    vehicles, total_profit, total_penalty, packages_left, remaining_profit = optimize_delivery()
    return render_template('results.html', vehicles=vehicles, total_profit=total_profit,
                           total_penalty=total_penalty, packages_left=packages_left,
                           remaining_profit=remaining_profit)

@app.route('/statistics')
def statistics():
    stats = calculate_statistics()
    return render_template('statistics.html', stats=stats)
