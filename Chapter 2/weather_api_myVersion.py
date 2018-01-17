from pprint import pprint
from configparser import ConfigParser
import requests

def upcoming_forecast (api_key, lat, lon):
    """ pulls upcoming forecasts base don latitude and longitude"""
    resp = requests.get('http://api.openweathermap.org/data/2.5/forecast',
                        params={'lat': lat, 'lon': lon, 'appid':api_key,
                        'units':'imperial'})
    return resp.json()

def get_config():
    """returns my config object"""
    conf = ConfigParser()
    conf.read('config/prod.cfg')
    return conf

config = get_config()

pprint(upcoming_forecast(
config.get('openweather', 'api_key'),41.279507, -72.949183))
