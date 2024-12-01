import pandas as pd

def optimize_delivery(return_data=False):
    # Läs in data från CSV-filen
    data = pd.read_csv('data/lagerstatus.csv')
    # Beräkna straffavgifter för paket som är efter deadline
    data['Straffavgift'] = data['Deadline'].apply(lambda x: -(x**2) if x < 0 else 0)

    # Sortera paket efter högst förtjänst per kg (eller annan prioritering)
    data = data.sort_values(by='Förtjänst', ascending=False)

    # Skapa 10 budbilar
    vehicles = {f'Bil_{i+1}': {'packages': [], 'total_weight': 0} for i in range(10)}

    # Maxkapacitet per budbil
    max_capacity = 800.0

    # Tilldela paket till budbilar
    for index, row in data.iterrows():
        # Försök att tilldela paketet till en av budbilarna
        for vehicle in vehicles.values():
            if vehicle['total_weight'] + row['Vikt'] <= max_capacity:
                vehicle['packages'].append(row.to_dict())  # Konvertera raden till dict
                vehicle['total_weight'] += row['Vikt']
                data.at[index, 'Assigned'] = True
                break
        else:
            # Om paketet inte får plats i någon bil, markera det som kvar i lager
            data.at[index, 'Assigned'] = False

    # Beräkna total förtjänst för levererade paket
    delivered_packages = data[data['Assigned'] == True]
    total_profit = delivered_packages['Förtjänst'].sum()

    # Beräkna total straffavgift för paket kvar i lager
    undelivered_packages = data[data['Assigned'] == False]
    total_penalty = undelivered_packages['Straffavgift'].sum()

    # Antal paket kvar i lager
    packages_left = len(undelivered_packages)

    # Total förtjänst kvar i lager (exklusive straffavgift)
    remaining_profit = undelivered_packages['Förtjänst'].sum()

    # Omvandla vehicles till en lista för enklare iteration i templates
    vehicles_list = []
    for name, info in vehicles.items():
        vehicles_list.append({
            'name': name,
            'packages': info['packages'],
            'total_weight': info['total_weight']
        })

    if return_data:
        return vehicles_list, total_profit, total_penalty, packages_left, remaining_profit, data
    else:
        return vehicles_list, total_profit, total_penalty, packages_left, remaining_profit
