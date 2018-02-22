from configparser import ConfigParser
from urllib.parse import quote_plus
import requests
import os
from multiprocessing import Pool
import logging

def get_config():
    print('def get_config():')
    cwd = os.getcwd()
    os.chdir(r'C:\Users\drose\Documents\GitHub\Data-Wrangling-and-Analysis')
    conf = ConfigParser()
    conf.read('prod.cfg')
    print('conf.read success')
    os.chdir(cwd)
    print('cwd change back success')
    return conf

def get_lat_long(config, address):
    print('def get_lat_long(config, address')
    qs_dict = {'address': quote_plus(address), 'key': config.get('google', 'api_key'),}
    logging.ddebug('Requesting weather data from google for %s', address)
    resp = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=qs_dict)

    try:
        lat, lon = resp.json().get('result')[0].get('geometry').get('location').values()
    except KeyError:
        raise Exception('Could not find address: %s', address)
    return lat, lon

def upcoming_forecast(args):
    print('def upcoming_forecast(args):')
    config, address = args
    lat, lon = get_lat_long(config, address)
    logging.debug('Have lat and long for %s', address)
    resp  =requests.get('http://api.openweathermap.org/data/2.5/forecast', params={'lat':lat, 'lon':lon, 'appid':config.get('openweather', 'api_key'), 'units': 'metric'})
    return (address, resp.json())

def get_city_forecasts(addresses):
    config = get_config()
    pool = Pool(processes=4)
    return pool.map(upcoming_forecast, [(config, addy) for addy in addresses])

my_weather = get_city_forecasts(['Los Angeles, CA', 'New York, NY', 'Berlin, Germany'])

print(type(my_weather))

for item in my_weather:
    print(item[0])
