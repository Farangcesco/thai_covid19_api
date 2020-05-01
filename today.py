#! /usr/local/bin/python3
import requests
import re
from datetime import date

d_today = date.today()

url = 'https://covid19.th-stat.com/api/open/today'
response = requests.get(url)
response_json = response.json()

def f_number(n):
    return str(f'{n:,}')

def get_data(variable):
    return f_number(response_json[variable])

# Short version
#for k, v in response_json.items():
#    if isinstance(v, int):
#        keys = (re.sub(r"(\w)([A-Z])", r"\1 \2", k))
#        print(keys + ': ' + f_number(v))

# Long version
confirmed_today = get_data('Confirmed')
recovered = get_data('Recovered')
hospitalized = get_data('Hospitalized')
deaths = get_data('Deaths')
newConfirmed = get_data('NewConfirmed')
newRecovered = get_data('NewRecovered')
newHospitalized = get_data('NewHospitalized')
newDeaths = get_data('NewDeaths')
fatality_rate = str(round(response_json['Deaths']/response_json['Confirmed']*100, 2))

print(f'\nDate: {d_today:%B %d, %Y}\n')
print(f'Infections: {confirmed_today} (+{newConfirmed})')
print(f'Recovered: {recovered} (+{newRecovered})')
print(f'Hospitalized: {hospitalized} ({newHospitalized})')
print(f'Deaths: {deaths} (+{newDeaths})')
print(f'Fatality Rate: {fatality_rate}%')
