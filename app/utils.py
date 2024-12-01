import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from app.optimizer import optimize_delivery

def calculate_statistics():
    # Anropa optimize_delivery för att få data
    vehicles_list, total_profit, total_penalty, packages_left, remaining_profit, data = optimize_delivery(return_data=True)

    # Dela upp data i levererade och icke-levererade paket
    delivered = data[data['Assigned'] == True]
    undelivered = data[data['Assigned'] == False]

    stats = {}

    for dataset, name in zip([delivered, undelivered], ['delivered', 'undelivered']):
        if not dataset.empty:
            weights = dataset['Vikt']
            profits = dataset['Förtjänst']

            stats[f'{name}_weight_mean'] = weights.mean()
            stats[f'{name}_weight_variance'] = weights.var()
            stats[f'{name}_weight_std'] = weights.std()
            stats[f'{name}_profit_mean'] = profits.mean()
            stats[f'{name}_profit_variance'] = profits.var()
            stats[f'{name}_profit_std'] = profits.std()
        else:
            stats[f'{name}_weight_mean'] = 0
            stats[f'{name}_weight_variance'] = 0
            stats[f'{name}_weight_std'] = 0
            stats[f'{name}_profit_mean'] = 0
            stats[f'{name}_profit_variance'] = 0
            stats[f'{name}_profit_std'] = 0

    return stats

def generate_histograms():
    # Anropa optimize_delivery för att få data
    vehicles_list, total_profit, total_penalty, packages_left, remaining_profit, data = optimize_delivery(return_data=True)

    # Histogram för vikt
    plt.hist(data['Vikt'], bins=20)
    plt.title('Viktdistribution')
    plt.xlabel('Vikt (kg)')
    plt.ylabel('Antal paket')
    plt.savefig('app/static/weight_histogram.png')
    plt.close()

    # Histogram för förtjänst
    plt.hist(data['Förtjänst'], bins=10)
    plt.title('Förtjänstdistribution')
    plt.xlabel('Förtjänst')
    plt.ylabel('Antal paket')
    plt.savefig('app/static/profit_histogram.png')
    plt.close()
