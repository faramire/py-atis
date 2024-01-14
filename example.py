# ========================================
# 
# Py-ATIS
# (c) Fabio Ramirez Stern, 2023-2024
# 
# ========================================

# CONFIG

version = '0.1' # version number
lgfilename = f'YOUR-LOG-NAME_LOG_{version}_' # Logfile name

owmAPIkey = 'YOUR-OWM-KEY' # OpenWeatherMap API key
wxapikey = 'YOUR-WX-KEY' # checkWXapi key
wxurl = "https://api.checkwx.com/metar/XXXX/" # WX API url

atislocation = 'YOUR-LOCATION-STRING' # Location
lat =  '12.34'
long = '56.78'

# IMPORTS


from atis import createATIS()

import datetime
import time
import logging


# LOGGING
lgfilename = lgfilename + f'{datetime.datetime.now()}'
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG, filename=lgfilename)
logging.info(f'Py-ATIS LOG {version}')


# ========================================

# SETUP

letterc = 0 # Alpha

# ========================================
      
# RUNTIME

cATIS = createATIS(wxurl, wxapikey, owmAPIkey, atislocation, lat, long, letterc)

print(cATIS[0])
print("\n=============================\n")
print(cATIS[1])

#END
