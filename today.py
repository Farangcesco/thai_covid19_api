#! /usr/local/bin/python3
import requests
from datetime import date

d_today = date.today()
d_today = d_today.strftime('%d %B, %Y')

url = 'https://covid19.th-stat.com/api/open/today'
response = requests.get(url)
response_json = response.json()

def f_number(n):
    return str(f'{n:,}')

def get_data(variable):
    return f_number(response_json[variable])

confirmed_today = get_data('Confirmed')
recovered = get_data('Recovered')
hospitalized = get_data('Hospitalized')
deaths = get_data('Deaths')
newConfirmed = get_data('NewConfirmed')
newRecovered = get_data('NewRecovered')
newHospitalized = get_data('NewHospitalized')
newDeaths = get_data('NewDeaths')

print(f'\nDate: {d_today}\n')
print(f'Infections: {confirmed_today} (+{newConfirmed})')
print(f'Recovered: {recovered} (+{newRecovered})')
print(f'Hospitalized: {hospitalized} ({newHospitalized})')
print(f'Deaths: {deaths} (+{newDeaths})')
