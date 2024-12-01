from flask import render_template, request, redirect, url_for
from app import app
from app.optimizer import optimize_delivery
from app.utils import calculate_statistics

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/optimize')
def optimize():
    vehicles, total_profit, total_penalty, packages_left, remaining_profit, data = optimize_delivery(return_data=True)
    total_packages_delivered = len(data[data['Assigned'] == True])
    undelivered_packages = data[data['Assigned'] == False].to_dict('records')
    return render_template('results.html', vehicles=vehicles, total_profit=total_profit,
                           total_penalty=total_penalty, packages_left=packages_left,
                           remaining_profit=remaining_profit,
                           total_packages_delivered=total_packages_delivered,
                           undelivered_packages=undelivered_packages)

@app.route('/statistics')
def statistics():
    stats = calculate_statistics()
    return render_template('statistics.html', stats=stats)

@app.route('/track', methods=['GET', 'POST'])
def track():
    if request.method == 'POST':
        tracking_id = request.form.get('tracking_id')
        # Här skulle du lägga till logik för att spåra paketet
        # För nu kan vi bara skicka användaren till en sida med ett exempelresultat
        return render_template('track_result.html', tracking_id=tracking_id)
    return render_template('track.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/legal_notice')
def legal_notice():
    return render_template('legal_notice.html')
