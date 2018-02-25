
# coding: utf-8

# In[2]:


import requests
import Parallelizing
from multiprocessing import Pool
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser
try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus
import logging
from pprint import pprint as pp





def upcoming_forecast(args):
    """ Pulls upcoming forecast based on address. """
    config, address = args
    lat, lon = get_lat_long(config, address)
    logging.debug('Have lat and long for %s', address)
    resp = requests.get('http://api.openweathermap.org/data/2.5/forecast',
                        params={'lat': lat, 'lon': lon,
                                'appid': config.get('openweather', 'api_key'),
                                'units': 'metric'})
    return (address, resp.json())


# In[4]:


def get_config():
    """ Return my config object. """
    conf = ConfigParser()
    conf.read('config/prod.cfg')
    return conf


# In[5]:


def get_lat_long(config, address):
    """ Returns lat and long from Google geocode API based on address. """
    qs_dict = {'address': quote_plus(address),
               'key': config.get('google', 'api_key'),
    }
    logging.debug('Requesting weather data from google for %s', address)
    resp = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=qs_dict)
    try:
        lat, lon = resp.json().get('results')[0].get('geometry').get('location').values()
    except KeyError:
        raise Exception('Could not find address: %s', address)
    return lat, lon


# In[6]:


def get_city_forecasts(addresses):
    """ Returns forecasts when given a list of string addresses based on Google geocoding and openweather data. """
    config = get_config()
    pool = Pool(processes=4)
    return pool.map(upcoming_forecast, [(config, addy) for addy in addresses])


# In[7]:
if __name__ == '__main__':
    my_weather = get_city_forecasts(['Ansonia, CT',	'Avon, CT',	'Beacon Falls, CT',	'Berlin, CT',	'Bethel, CT',	'Bloomfield, CT',	'Branford, CT',	'Bridgeport, CT',	'Bristol, CT',	'Brookfield, CT',	'Brooklyn, CT',
    'Burlington, CT',	'Canton, CT',	'Central Manchester, CT',	'Cheshire, CT',	'Colchester, CT',	'Conning Towers-Nautilus Park, CT',	'Cos Cob, CT',	'Coventry, CT',	'Cromwell, CT',	'Danbury, CT',	'Darien, CT',	'Derby, CT',
    'East Haddam, CT',	'East Hartford, CT',	'East Haven, CT',	'East Lyme, CT',	'East Windsor, CT',	'Easton, CT',	'Ellington, CT',	'Enfield, CT',	'Essex, CT',	'Fairfield, CT',	'Farmington, CT',
    'Glastonbury Center, CT',	'Glastonbury, CT',	'Granby, CT',	'Greenwich, CT',	'Griswold, CT',	'Groton, CT',	'Guilford, CT',	'Haddam, CT',	'Hamden, CT',	'Hartford, CT',	'Hebron, CT',	'Kensington, CT',
    'Killingly, CT',	'Killingworth, CT',	'Lebanon, CT',	'Ledyard, CT',	'Madison, CT',	'Manchester, CT',	'Mansfield, CT',	'Marlborough, CT',	'Meriden, CT',	'Middlebury, CT',	'Middletown, CT',	'Milford, CT',
    'Monroe, CT',	'Montville, CT',	'Naugatuck, CT',	'New Britain, CT',	'New Canaan, CT',	'New Fairfield, CT',	'New Hartford, CT',	'New Haven, CT',	'New London, CT',	'New Milford, CT',	'Newington, CT',
    'North Branford, CT',	'North Haven, CT',	'Norwalk, CT',	'Norwich, CT',	'Oakville, CT',	'Old Greenwich, CT',	'Old Lyme, CT',	'Old Saybrook, CT',	'Orange, CT',	'Oxford, CT',	'Plainfield, CT',
    'Plainville, CT',	'Plymouth, CT',	'Prospect, CT',	'Putnam District, CT',	'Putnam, CT',	'Redding, CT',	'Ridgefield, CT',	'Riverside, CT',	'Rockville, CT',	'Rocky Hill, CT',	'Seymour, CT',
    'Shelton, CT',	'Simsbury, CT',	'Somers, CT',	'South Windsor, CT',	'Southbury, CT',	'Southington, CT',	'Southwood Acres, CT',	'Stafford, CT',	'Stamford, CT',	'Storrs, CT',	'Stratford, CT',
    'Suffield, CT',	'Thomaston, CT',	'Thompsonville, CT',	'Thompson, CT',	'Tolland, CT',	'Torrington, CT',	'Trumbull, CT',	'Vernon, CT',	'Wallingford Center, CT',	'Wallingford, CT',
    'Waterbury, CT',	'Waterford, CT',	'Watertown, CT',	'West Hartford, CT',	'West Haven, CT',	'Westbrook, CT',	'Weston, CT',	'Westport, CT',	'Wethersfield, CT',	'Willimantic, CT',
    'Willington, CT',	'Wilton, CT',	'Winchester, CT',	'Windham, CT',	'Windsor Locks, CT',	'Windsor, CT',	'Winsted, CT',	'Wolcott, CT',	'Woodbridge, CT',	'Woodbury, CT',	'Woodstock, CT'])

    type(my_weather)

    for item in my_weather:
        pp(item)
